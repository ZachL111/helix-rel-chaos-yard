# Review Journal

The repository goal stays the same: develop a Solidity command-oriented project for chaos scenarios with framed sample traffic, bounds and ordering tests, and offline replay mode. This note explains the added review angle.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its reliability focus without claiming live deployment or external usage.

## Cases

- `baseline`: `budget pressure`, score 188, lane `ship`
- `stress`: `failure width`, score 108, lane `watch`
- `edge`: `recovery gap`, score 215, lane `ship`
- `recovery`: `runbook drift`, score 215, lane `ship`
- `stale`: `budget pressure`, score 214, lane `ship`

## Note

A future change should add new cases before it changes the scoring rule.
