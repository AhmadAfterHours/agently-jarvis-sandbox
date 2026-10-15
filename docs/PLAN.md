# Plan (fictional)

1. Add `arcwell/alerts.py`: `runway_alert(cash, expenses, revenue, threshold_months=6)` returns "ok", "watch" (under
   twice the threshold) or "act" (under the threshold), with tests.
2. Make `monthly_burn` reject mismatched month lists (different lengths) with a clear error, with a test.
3. Add a "Runway alerts" section to the README describing the levels.
4. Record any defect found during review in `docs/DEFECTS.md`.
