# Agent Integration Prompt

Please help me integrate our linters with my existing project.

## What These Linters Do

These linters are opinionated, Clean Code-first configurations designed to help AI coding agents produce readable, maintainable, and correct code by default.

They enforce strict standards for:
- Code structure and organization
- Naming conventions
- Function complexity and size
- Dead code elimination
- Import ordering
- Explicit over clever implementations
- Safety measures (denying panics, unsafe patterns, unwraps)

## What to Check

Please review the following files that were installed:

  - .pylintrc
  - .pytest_cache/.gitignore
  - .pytest_cache/CACHEDIR.TAG
  - .pytest_cache/README.md
  - .pytest_cache/v/cache/nodeids
  - .ruff_cache/.gitignore
  - .ruff_cache/0.15.12/15162454857600723852
  - .ruff_cache/0.15.7/13011942872033280993
  - .ruff_cache/CACHEDIR.TAG
  - ruff.toml
  - tests/cleancode/__pycache__/test_no_provably_unnecessary_fallback.cpython-314-pytest-9.0.3.pyc
  - tests/cleancode/__pycache__/test_no_suspicious_fallback.cpython-314-pytest-9.0.3.pyc
  - tests/cleancode/test_no_provably_unnecessary_fallback.py
  - tests/cleancode/test_no_suspicious_fallback.py

For each linter config you find, please:

1. Understand the specific rules it enforces
2. Scan the project's source code for violations
3. Fix violations systematically where possible
4. If a violation requires architectural changes, document your reasoning

## Integration Considerations

- These configs are self-contained when used at their documented paths
- You may need to adjust specific rules to match project conventions
- Consider the Boy Scout Rule: every lint run should leave the code cleaner than it found it
- Focus on high-signal rules; false negatives in edge cases are acceptable
- Make code self-explanatory by default; avoid code comments explaining obvious intent

## Action Items

After reviewing:
- Identify any direct violations
- Suggest architectural improvements if violations require them
- Run the configured linters and confirm they pass
- Update documentation if the project needs additional setup instructions