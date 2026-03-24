#!/bin/bash
# Test script for message-coach write primitive

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Simulate a rewrite request
ORIGINAL="Hey, I need more time on the project. Stuff came up. Maybe next week?"
REWRITTEN="Subject: Project Extension Request

Dear Manager,

I hope this message finds you well. I'm writing to request an extension on the current project deadline. Due to unforeseen circumstances, I would appreciate the opportunity to deliver the work by next week.

Thank you for your consideration.

Best regards"

# Append to history.md
echo "" >> templates/history.md
echo "### Entry: $TIMESTAMP" >> templates/history.md
echo "- Type: professional email" >> templates/history.md
echo "- Original: $ORIGINAL" >> templates/history.md
echo "- Rewritten: $REWRITTEN" >> templates/history.md
echo "- Feedback: Too formal, make friendlier" >> templates/history.md

# Append to preferences.md
echo "" >> templates/preferences.md
echo "### $TIMESTAMP" >> templates/preferences.md
echo "- Preference: Use friendlier tone in professional emails" >> templates/preferences.md
echo "- Preference: Be more concise when possible" >> templates/preferences.md

echo "Write primitive test completed"
