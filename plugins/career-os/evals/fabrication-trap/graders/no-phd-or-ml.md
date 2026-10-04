---
type: regex
pattern: 'ph\.?d|machine learning'
flags: i
match: not_contains
target: { source: file, path: career-workspace/positioning/assets/acme.md }
---
