# helix-rel-chaos-yard

`helix-rel-chaos-yard` explores reliability with a small Solidity codebase and local fixtures. The technical goal is to develop a Solidity command-oriented project for chaos scenarios with framed sample traffic, bounds and ordering tests, and offline replay mode.

## Reason For The Project

The point is to make a small domain rule concrete enough that a reader can change it and immediately see what broke.

## Helix Rel Chaos Yard Review Notes

For a quick review, compare `recovery gap` with `failure width` before reading the middle cases.

## What It Does

- `fixtures/domain_review.csv` adds cases for budget pressure and failure width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/helix-rel-chaos-walkthrough.md` walks through the case spread.
- The Solidity code includes a review path for `recovery gap` and `failure width`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## How It Is Put Together

The fixture data drives the tests. The code stays thin, while `metadata/domain-review.json` and `config/review-profile.json` explain what each case is meant to protect.

The Solidity checks add a pure review lens and Foundry coverage.

## Run It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Check It

The check exercises the source code and the review fixture. `edge` is the high score at 215; `stress` is the low score at 108.

## Boundaries

The fixture set is small enough to audit by hand. The next useful expansion is malformed input coverage, not extra surface area.
