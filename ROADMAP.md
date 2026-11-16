# Roadmap

Phases in critical-path order: each one needs the one before it. Every task
is a GitHub Issue small enough to finish in one fresh session, with its
acceptance criteria and the tests that prove it.

| Phase | Goal | Issues |
|---|---|---|
| 1. Data connection | The app reads the team's database, locally and on Community Cloud | #3, #4 |
| 2. Data layer | Every metric in the spec has a tested function in `dashboard/metrics.py` | #5 to #15 |
| 3. Views | Each stakeholder question has a screen section that answers it, built as `design.md` draws it | #16 to #20 |
| 4. Filters | The interactions the spec lists work, and the numbers still reconcile | #21, #22 |
| 5. Polish and deploy | The app follows every rule in `design.md`; `mockup.py` is gone; the live app link is in the README | #23, #24 |

## Critical path

Each Issue waits for the ones listed; the longest chain sets the pace.

- **Connection first:** #3 (connect locally) blocks everything. #4 (hello-world deploy) follows #3 and must merge before the final deploy #24.
- **Data layer:** #5 (total revenue and Finance gap) blocks every other metric: #6 genre, #7 country, #8 combinations, #9 yearly, #10 monthly, #11 top-10 customers and #13 reps. Then #11 blocks #12 (years active), and #13 blocks #14 (customers per rep). #15 (breakdowns add up) waits for #6, #7, #9 and #13.
- **Views:** #16 (page frame) waits for #5 and blocks all four screens. #17 Screen 1 needs #6, #7, #8; #18 Screen 2 needs #9, #10; #19 Screen 3 needs #11, #12; #20 Screen 4 needs #13, #14.
- **Filters:** #21 (year picker) needs #17. #22 (other screens ignore it) needs #18, #19, #20 and #21.
- **Finish:** #23 (style check) needs #22. #24 (delete mockup, live link, final deploy) needs #23 and #4.

Longest chain: #3 -> #5 -> #6 -> #17 -> #21 -> #22 -> #23 -> #24.

---

## Dashboard review

When the dashboard is finished, the Pitch Lead runs the final review. Each fix
becomes a GitHub Issue labeled `phase-1` through `phase-5`, for the phase it
belongs to, and each review adds one line below.

<Filled in by /dashkit:review-dashboard: one line per review, "- YYYY-MM-DD: fixes in #n, #n".>
