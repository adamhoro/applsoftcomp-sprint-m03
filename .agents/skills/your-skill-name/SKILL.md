---
name: your-skill-name
description: <One sentence — what does this assistant do and for whom?>
---

Shared files: `memory.md` (<what it stores>), `progress.txt` (done/remaining), `results/` (per-query outputs).

<!-- ============================================================
  INSTRUCTIONS FOR STUDENTS
  Replace every <placeholder> with your own design.
  Delete these comment blocks when you are done.
  ============================================================ -->

## Lead Agent

<!-- The Lead Agent is the loop controller. It spawns sub-agents and coordinates the workflow.
     It should NOT do the actual work itself — delegate everything to sub-agents.
     Describe: (1) what it does on first run (init), (2) when/how it spawns sub-agents,
     (3) what order things happen in, (4) how it knows when to stop. -->

1. **Init** (first run only): copy `templates/memory.md` into working dir if not present. <Any other setup steps?>
2. **Spawn <Sub-Agent Name>** for each <unit of work> in parallel via Task tool. Wait for all.
3. <Next orchestration step — e.g., spawn a synthesis agent, update progress, ask the user?>
4. Stop when <condition>.

## Sub-Agents (spawned via Task tool)

<!-- Define each type of sub-agent. For each one, describe:
     - When it is spawned (by the Lead Agent step above)
     - Exactly what it reads, what it does, and what it writes
     - The schema of anything it appends to memory files
     Sub-agents must WRITE to shared files — that is how they communicate results back. -->

### <Sub-Agent Type 1> (parallelizable / sequential — pick one)

1. Receive: `<what input does this agent get?>` (e.g., a search query, a file path).
2. Do: `<what action does it take?>` (e.g., `uv run python3 tools/search_openalex.py "<query>" --n 5`).
3. Write: append results to `<filename>` using the schema in `templates/<filename>`.

### <Sub-Agent Type 2>

1. Read: `<what does it read first?>` (e.g., `memory.md` for prior context).
2. Do: `<what action?>`.
3. Write: `<what does it write and where?>`.

## Memory Schema

<!-- This is the most important design decision you make.
     Define every persistent file your skill uses:
     - What is the filename?
     - What does each entry look like? (show an example row/block)
     - When is it written vs read?
     - Append-only, or can it be overwritten?
     See templates/ for starter schemas you can copy and modify. -->

**`memory.md`** — <one-line description of what this file accumulates>
- Written by: <which sub-agent(s)>
- Read by: <Lead Agent? Synthesis agent?>
- Schema: see `templates/memory.md`

**`progress.txt`** — tracks which items are done/remaining
- Each entry: `[DONE|TODO] <item identifier> — <one-line note>`
- Append only; do not remove entries.

## Retrieval Strategy

<!-- Describe how your assistant looks things up.
     Rule: always check memory.md first. Only go to the internet if the answer is not there.
     Describe: (1) what the agent reads before searching, (2) the condition that triggers a live search,
     (3) which tool it uses for the live search (WebSearch, WebFetch, search_openalex.py, etc.) -->

1. Before any search, read `memory.md` — if the query is already covered, return the cached result.
2. If not found, call `<tool>` with the query: `<exact command or tool invocation>`.
3. After retrieval, append the new result to `memory.md` using the schema above.

## Output Format

<!-- What does the final answer look like? Describe length, structure, and tone.
     Example: "Write 1–2 paragraphs in conversational tone. No bullet points. Cite the source URL." -->

- Length: <e.g., 1–2 paragraphs, a numbered list, a short story>
- Tone: <e.g., academic, funny, friendly>
- Citation: <how to reference sources, if any>

## Stop Conditions

- <Primary completion condition — e.g., "All queries answered and results written to output.md">
- Sub-agent fails repeatedly → escalate to user
- User cancels
