# Arcwell Cash Watch (fictional)

A small sandbox project used to test Agently's Jarvis on real GitHub work: branches, commits, pull requests and CI.
All data and names here are fictional.

`arcwell/runway.py` estimates a company's cash runway from monthly figures. `docs/PLAN.md` lists planned work and
`docs/DEFECTS.md` records known defects.

## Runway alerts

`arcwell.alerts.runway_alert(cash, expenses, revenue, threshold_months=6)` classifies a company's cash runway
from its monthly net burn:

- `act`: runway is below the threshold, six months by default.
- `watch`: runway is at or above the threshold but below twice the threshold.
- `ok`: runway is at least twice the threshold, or the company has no net cash burn.
