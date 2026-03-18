#!/usr/bin/env python3
"""Search academic papers via the OpenAlex REST API (no API key required).

Usage:
    python3 search_openalex.py "<query>" [--n 5] [--format text|json]

Examples:
    python3 search_openalex.py "graph neural networks" --n 3
    python3 search_openalex.py "network science community detection" --n 5 --format json

Output (text, default):
    One paper per block: title, authors, year, venue, abstract, DOI URL.

Output (json):
    JSON array of paper objects.

Requires: Python 3.9+ standard library only (urllib).
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request


OPENALEX_API = "https://api.openalex.org/works"
EMAIL = "polite@pool.openalex.org"  # uses the polite pool — faster responses


def search(query: str, n: int = 5) -> list[dict]:
    params = urllib.parse.urlencode({
        "search": query,
        "per_page": n,
        "select": "title,authorships,publication_year,primary_location,abstract_inverted_index,doi",
        "mailto": EMAIL,
    })
    url = f"{OPENALEX_API}?{params}"

    req = urllib.request.Request(url, headers={"User-Agent": f"skill-agent/1.0 ({EMAIL})"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        sys.exit(f"OpenAlex API error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        sys.exit(f"Network error: {e.reason}")

    return data.get("results", [])


def reconstruct_abstract(inverted_index: dict | None) -> str:
    """OpenAlex stores abstracts as inverted index {word: [positions]}. Reconstruct."""
    if not inverted_index:
        return "(no abstract available)"
    positions = []
    for word, pos_list in inverted_index.items():
        for pos in pos_list:
            positions.append((pos, word))
    positions.sort()
    return " ".join(word for _, word in positions)


def format_text(papers: list[dict]) -> str:
    lines = []
    for i, p in enumerate(papers, 1):
        title = p.get("title") or "(no title)"
        year = p.get("publication_year") or "?"
        doi = p.get("doi") or "(no DOI)"

        authors = p.get("authorships", [])
        author_names = [
            a["author"]["display_name"]
            for a in authors[:3]
            if a.get("author", {}).get("display_name")
        ]
        author_str = ", ".join(author_names)
        if len(authors) > 3:
            author_str += " et al."

        location = p.get("primary_location") or {}
        source = location.get("source") or {}
        venue = source.get("display_name") or "(venue unknown)"

        abstract = reconstruct_abstract(p.get("abstract_inverted_index"))

        lines.append(f"[{i}] {title}")
        lines.append(f"    Authors : {author_str or '(unknown)'}")
        lines.append(f"    Year    : {year}  |  Venue: {venue}")
        lines.append(f"    DOI     : {doi}")
        lines.append(f"    Abstract: {abstract}")
        lines.append("")
    return "\n".join(lines)


def format_json(papers: list[dict]) -> str:
    out = []
    for p in papers:
        out.append({
            "title": p.get("title"),
            "authors": [
                a["author"]["display_name"]
                for a in p.get("authorships", [])
                if a.get("author", {}).get("display_name")
            ],
            "year": p.get("publication_year"),
            "venue": (
                (p.get("primary_location") or {})
                .get("source", {}) or {}
            ).get("display_name"),
            "doi": p.get("doi"),
            "abstract": reconstruct_abstract(p.get("abstract_inverted_index")),
        })
    return json.dumps(out, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description="Search papers via OpenAlex.")
    parser.add_argument("query", help="Natural language search query")
    parser.add_argument("--n", type=int, default=5, help="Number of results (default: 5)")
    parser.add_argument("--format", choices=["text", "json"], default="text",
                        help="Output format (default: text)")
    args = parser.parse_args()

    papers = search(args.query, args.n)
    if not papers:
        print("No results found.", file=sys.stderr)
        sys.exit(0)

    if args.format == "json":
        print(format_json(papers))
    else:
        print(format_text(papers))


if __name__ == "__main__":
    main()
