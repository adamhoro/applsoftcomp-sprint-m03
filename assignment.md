# Assignment: Design Your Own Personalized Assistant

**Course:** Applied Software Computing  •  **Due:** Two weeks from today  •  **In-class kickoff:** 60 minutes

---

## What You Are Building

You will design a **personalized Claude Code assistant** by writing a single `SKILL.md` file.
The skill defines how your assistant thinks, what it remembers, and when it delegates work.
You choose the topic — anything you find genuinely useful.

**Example topics** (pick one or invent your own):

| Topic | What it does |
|-------|-------------|
| Literature assistant | Searches papers via OpenAlex and writes paragraph summaries for natural-language queries |
| News storyteller | Fetches headlines and retells them in a funny, personalized tone |
| Binghamton trip advisor | Answers questions about things to do, eat, and see in Binghamton, NY |
| *Your own idea* | Anything useful to you — cooking assistant, study planner, code reviewer, ... |

---

## Your Deliverable

One folder submitted as a zip or Git repository:

```
.agents/skills/<your-skill-name>/
    SKILL.md              ← your main artifact
    templates/            ← your memory schema files (designed by you)
    tools/                ← any helper scripts (pre-built tools available, see below)
```

---

## Three Required Components

Your `SKILL.md` must contain all three of the following, written in free prose:

### 1. Sub-agent spawning (isolation)
Describe **when** your Lead Agent spawns a sub-agent, **what task** it hands off,
and how results come back. Sub-agents are spawned via the `Task` tool.
*Example: "Spawn one Search Sub-Agent per query in parallel. Each agent writes its results to `results/query-N.md`."*

### 2. Memory write
Describe **what** information gets written to persistent files, **when** it gets written,
and **what schema** each file follows. You design the schema.
*Example: "After each search, append the paper title, year, and a two-sentence summary to `memory.md`."*

### 3. Retrieval
Describe **how** your assistant reads from memory before going to the internet,
and **when** it falls back to a live search or API call.
*Example: "Before any search, read `memory.md` for previously seen results. Only call OpenAlex if the query is not already covered."*

---

## Pre-built Tools

The following tools are provided in `tools/`. You may use them in your `SKILL.md`
by referencing `uv run python3 tools/<tool>.py <args>`.

| Tool | Usage |
|------|-------|
| `search_openalex.py` | Search academic papers: `python3 tools/search_openalex.py "<query>" [--n 5]` |

You may also write your own tools or use the agent's built-in `WebFetch` / `WebSearch`.

---

## Evaluation

### Instructor (primary grade)

| Component | 0 | 1 | 2 |
|-----------|---|---|---|
| Sub-agent spawning | Missing | Present but vague trigger or task | Clear trigger condition and isolated task |
| Memory write | Missing | Mentioned but no schema | Schema defined and write trigger specified |
| Retrieval | Missing | Memory or internet only | Memory-first with internet fallback |
| Coherence | Incoherent | Partially works as an assistant | Reads as a genuinely useful, self-consistent skill |

**Scoring:** 2 pts each component + 2 pts coherence = **8 pts total**.
Full marks (8/8) if all three components are solid and the skill makes sense.

### Peer assessment (two classmates review your SKILL.md)

You will be assigned two classmates to evaluate using the same rubric above.
Peer scores are advisory — the instructor score is final.

---

## Constraints

- `SKILL.md` must be plain Markdown. No code inside `SKILL.md` itself.
- Tools go in `tools/`. Templates and schema files go in `templates/`.
- You may use any HTTP APIs or pre-built tools. No external libraries required beyond `uv`.
- You are encouraged (not required) to use an LLM to help you draft `SKILL.md`.

---

## In-Class Session (60 min)

| Time | Activity |
|------|----------|
| 0–10 min | Read this sheet; pick your topic |
| 10–25 min | Design your memory schema on paper — what files, what fields, what gets appended vs overwritten |
| 25–45 min | Draft `SKILL.md` skeleton using the starter template |
| 45–60 min | Share draft with a neighbor; give one piece of feedback |

By end of class: you should have a skeleton `SKILL.md` with all three sections drafted (even if rough).

---

## Submission

Submit a zip file (or Git repo link) containing your `.agents/skills/<your-skill-name>/` folder.
Include a brief `README.md` (3–5 sentences) explaining what your assistant does and one example interaction.
