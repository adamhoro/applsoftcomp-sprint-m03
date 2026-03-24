# Message Coach Skill

## Invocation
/message-coach "Rewrite this: [your rough message]"
Or: /message-coach [message] --type [email|slack|formal|casual] --feedback "[optional feedback]"

## Overview
Rewrites rough messages into polished communications. Learns your tone/style preferences through feedback. Implements write (persist), select (retrieve), isolate (sub-agents) primitives.

## Workflow

### 1. SELECT: Load Context
- Read preferences.md: extract tone/style preferences
- Read history.md: find 2-3 similar past rewrites (match by --type)
- Pass context to sub-agents

### 2. ISOLATE: Spawn Sub-Agents (sequential)
**Planner** (Task tool):
- Analyze message type and intent
- Identify tone requirements from preferences
- Create rewrite plan (3 bullets max)

**Drafter** (Task tool):
- Execute rewrite per plan
- Apply preferences (concise, friendly, formal, etc.)
- Output polished message

**Reviewer** (Task tool):
- Check against preferences
- Flag issues (too long, wrong tone, missing clarity)
- Suggest 1-2 improvements or approve

### 3. WRITE: Persist State
- Append to history.md: timestamp, type, original, rewritten, feedback
- Append to preferences.md: any new feedback with timestamp
- Create files if missing

## Feedback Loop
After output, user can say:
- "Too formal, make friendlier"
- "Be more concise"
- "Use more direct language"
Message Coach saves this and applies next run.

## Files
- SKILL.md (this file)
- templates/preferences.md (tone/style storage)
- templates/history.md (rewrite log)

## Constraints
- SKILL.md under 150 lines
- Sub-agents run sequentially
- Only load relevant context (selective read)
- Commit after each task: "message-coach: [what changed]"
