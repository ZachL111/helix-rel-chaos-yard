# helix-rel-chaos-yard

`helix-rel-chaos-yard` is a Solidity project for Reliability. It turns develop a Solidity command-oriented project for chaos scenarios with framed sample traffic, bounds and ordering tests, and offline replay mode into a small local model with readable fixtures and a direct verification command.

## Reading Helix Rel Chaos Yard

Start with the README, then open `metadata/project.json` to check the constants behind the examples. After that, `fixtures/cases.csv` shows the compact path and `examples/extended_cases.csv` gives a wider look at the same rule.

## Purpose

The goal is to capture the core behavior in code and make the surrounding assumptions obvious. A reader should be able to run the verifier, open the fixtures, and understand why each decision was made.

## Fixture Notes

`degraded` is the first example I would inspect because it lands on the `review` path with a score of -28. The broader file also keeps `degraded` at -28 and `surge` at 216, which gives the model a useful low-to-high spread.

## Design Sketch

The design is intentionally direct: parse or construct a signal, score it, classify it, and verify the expected branch. This makes the repository useful for studying reliability behavior without needing a service or database unless the language project itself is SQL. The Solidity project uses Foundry tests and pure contract functions so invariants are cheap to exercise.

## What It Does

- Models failure windows with deterministic scoring and explicit review decisions.
- Uses fixture data to keep retry budgets changes visible in code review.
- Includes extended examples for runbook checks, including `surge` and `degraded`.
- Documents recovery paths tradeoffs in `docs/operations.md`.
- Runs locally with a single verification command and no external credentials.

## Usage

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

This runs the language-level build or test path against the compact fixture set.

## Verification

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/audit.ps1
```

The audit command checks repository structure and README constraints before it delegates to the verifier.

## Files Worth Reading

- `src`: primary implementation
- `test`: language test directory
- `fixtures`: compact golden scenarios
- `examples`: expanded scenario set
- `metadata`: project constants and verification metadata
- `docs`: operations and extension notes
- `scripts`: local verification and audit commands
- `foundry.toml`: Foundry project configuration

## Next Directions

- Add malformed input fixtures so the failure path is as visible as the happy path.
- Split the scoring constants into a typed configuration object and validate it before use.
- Add a comparison mode that shows how decisions change when one signal is adjusted.
- Add one more reliability fixture that focuses on a malformed or borderline input.

## Limits

This code is local-first. It makes no claim about deployed usage and avoids credentials, hosted state, and environment-specific setup.

## Setup

Clone the repository, enter the directory, and run the verifier. No database server, cloud account, or token is required.
