# Defects (fictional)

| ID | Found | Description | Status |
|----|-------|-------------|--------|
| D-001 | 2026-10-15 | Initial test labeled 10 months of runway as `ok`; the documented default requires `watch` below 12 months. | Fixed: test now covers the 12-month boundary. |
| D-002 | 2026-10-15 | `NaN` or infinity could bypass comparison checks and return a false `ok` alert. | Fixed: finite-value validation and tests now reject all non-finite inputs. |
