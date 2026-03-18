# Plan: Personalized Assistant Skill Exercise

## Concept

Students design a personalized Claude Code **skill** by writing a `Skill.md` file.
The skill defines agent behavior — what it does, when to spawn sub-agents, how to
remember things, and how to look things up. Students choose their own topic freely.

The instructor pre-builds HTTP tool wrappers (e.g., OpenAlex, news APIs) and makes
them available. Students who want external data can use those tools.

---

## Deliverable: `agents/skills/<skill-name>/Skill.md`

Each student submits one `Skill.md` that defines their assistant.

---

## Three Required Components (graded by presence + quality)

### C1 — Sub-agent spawning (isolation)
Skill.md must contain explicit instructions for *when* to spawn a sub-agent
and what task to hand off to it (e.g., "spawn an isolated agent to fetch each paper").

### C2 — Memory write
Skill.md must contain explicit instructions for writing persistent information
to `memory.md` — including what to write, in what schema, and when to write it.
**Students design the schema themselves.**

### C3 — Retrieval (memory + internet)
Skill.md must contain explicit instructions for reading from `memory.md` first,
and/or when to trigger an internet / API search.

---

## Suggested Topics (examples only — students may choose their own)

- Literature assistant (uses OpenAlex HTTP API to find papers; writes 1–2 paragraph summaries)
- News storyteller with funny tone
- Binghamton trip advisor
- *Anything the student finds useful*

---

## Pre-built Tools (instructor provides)

HTTP wrappers students can reference in their Skill.md:

| Tool | Description |
|------|-------------|
| `openalex_search` | Search papers by keyword/topic via OpenAlex REST API |
| `web_fetch` | Fetch content from a URL |
| `web_search` | Search the web |
| *(others TBD)* | ... |

---

## Timeline

| Phase | Time | Activity |
|-------|------|----------|
| In-class session | 60 min | Read assignment, design schema, draft Skill.md skeleton |
| Take-home | 2 weeks | Refine Skill.md, test it, peer assess two classmates |

---

## Grading

- **Instructor**: Checks presence and quality of C1, C2, C3 in Skill.md. Generous score if all three are solid.
- **Peer assessment**: Each student evaluates 2–3 classmates' Skill.md files against the same rubric.

---

## Rubric (draft)

| Component | 0 | 1 | 2 |
|-----------|---|---|---|
| C1 Sub-agent spawning | Missing | Present but vague | Clear trigger condition + isolated task defined |
| C2 Memory write | Missing | Present but no schema | Schema defined + write trigger specified |
| C3 Retrieval | Missing | Memory OR internet only | Both memory-first and internet fallback specified |
| Overall coherence | Incoherent | Partially coherent | Skill makes sense as a useful assistant |

---

## Open Questions

1. What goes in `memory.md` header/structure — any constraints, or fully freeform per student?
2. Should `Skill.md` follow a fixed section template, or free prose with required keywords?
3. Do students submit a demo transcript as evidence the skill works?
4. How many pre-built tools do we provide at minimum for the in-class session?
5. Where do the pre-built tools live in the repo — `libs/` or `agents/tools/`?
