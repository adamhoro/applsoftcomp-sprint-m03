---
name: message coach skill 
description: Rewrite messages more proffesionally given specific contexts 
---

# Message Coach Skill
## Invocation
/message-coach "Rewrite this: [your rough message]"

## Shared Files
`templates/preferences.md` (tone/style), `templates/history.md` (log).

## Steps (execute in order)

### 1. Init
```bash
mkdir -p .agents/skills/message-coach/templates
touch .agents/skills/message-coach/templates/preferences.md
touch .agents/skills/message-coach/templates/history.md
```

### 2. Parse Input
Extract the message text from the invocation.

### 3. SELECT: Filter Context
```bash
cd .agents/skills/message-coach
grep -i "type:" templates/preferences.md
grep -A3 "type:" templates/history.md | head -10
```
Store filtered output as CONTEXT.

### 4. ISOLATE: Spawn Sub-Agents (sequential via Task tool)

**Planner** (Task tool, general):
```
You are Planner. Analyze this message: [message]
Context: [CONTEXT from step 3]
Output exactly 3 bullets:
1. Tone goal
2. Key points to preserve
3. Structure recommendation
```

**Drafter** (Task tool, general):
```
You are Drafter. Rewrite this message: [message]
Plan: [output from Planner]
Preferences: [CONTEXT]
Output: polished rewrite, max 3 sentences, conversational
```

**Reviewer** (Task tool, general):
```
You are Reviewer. Check this rewrite: [output from Drafter]
Criteria: tone match, clarity, max 3 sentences
Output: "APPROVE" or list 1-2 specific fixes
```

### 5. WRITE: Persist State
```bash
cd .agents/skills/message-coach
echo "## $(date +%Y-%m-%d) type=email" >> templates/history.md
echo "Original: [message]" >> templates/history.md
echo "Rewritten: [output from Reviewer]" >> templates/history.md
echo "Feedback: [if user gave feedback]" >> templates/history.md
```

If user gave new feedback:
```bash
echo "- $(date): [feedback]" >> templates/preferences.md
```

### 6. Output
Display the final rewritten message to user.

## Style Rules
- Max 3 sentences in rewrite
- Conversational tone
- Apply stored preferences from CONTEXT
