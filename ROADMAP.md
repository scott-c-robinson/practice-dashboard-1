# Roadmap

Phases in critical-path order: each one needs the one before it. Every task
is a GitHub Issue small enough to finish in one fresh session, with its
acceptance criteria and the tests that prove it.

| Phase | Goal | Issues |
|---|---|---|
| 1. Data connection | The app reads the team's database, locally and on Community Cloud | |
| 2. Data layer | Every metric in the spec has a tested function in `dashboard/metrics.py` | |
| 3. Views | Each stakeholder question has a screen section that answers it, built as `design.md` draws it | |
| 4. Filters | The interactions the spec lists work, and the numbers still reconcile | |
| 5. Polish and deploy | The app follows every rule in `design.md`; `mockup.py` is gone; the live app link is in the README | |

## Critical path

<Which Issues block which; filled in from the spec.>

---

## Dashboard review

When the dashboard is finished, the Pitch Lead runs the final review. Each fix
becomes a GitHub Issue labeled `phase-1` through `phase-5`, for the phase it
belongs to, and each review adds one line below.

<Filled in by /dashkit:review-dashboard: one line per review, "- YYYY-MM-DD: fixes in #n, #n".>

---

## Task draft

| # | Phase | Task | AC IDs | Tests that prove it (or criteria) | Depends on | Assignee |
|---|---|---|---|---|---|---|
| T1 (#3) | 1 | Connect the app to `vinyl_vault` locally | none | Criteria: the app shows the database connection and the existing connection tests pass. Tests: none new; the full suite stays green | none | scott-c-robinson |
| T2 (#4) | 1 | Put a hello-world version live on Community Cloud | none | Criteria: the live link opens and shows the connection. Tests: none new; the full suite stays green | T1 | scott-c-robinson |
| T3 (#5) | 2 | Total revenue and the Finance gap (optional year) | AC-11 | `test_ac11_total_is_2328_60`, `test_ac11_gap_is_zero` | T1 | scott-c-robinson |
| T4 (#6) | 2 | Genre revenue and share (optional year) | AC-1 | `test_ac1_top_five_genres`, `test_ac1_genre_revenue_reconciles` | T3 | scott-c-robinson |
| T5 (#7) | 2 | Country revenue and share (optional year) | AC-3 | `test_ac3_top_five_countries`, `test_ac3_country_revenue_reconciles` | T3 | scott-c-robinson |
| T6 (#8) | 2 | Genre-and-country combinations (optional year) | AC-4 | `test_ac4_top_three_combinations`, `test_ac4_combinations_reconcile` | T3 | scott-c-robinson |
| T7 (#9) | 2 | Yearly revenue and change from prior year | AC-5 | `test_ac5_yearly_revenue`, `test_ac5_year_over_year_change` | T3 | scott-c-robinson |
| T8 (#10) | 2 | Monthly revenue | AC-6 | `test_ac6_sixty_months`, `test_ac6_january_2021_is_35_64` | T3 | scott-c-robinson |
| T9 (#11) | 2 | Top-10 customers and their share of revenue | AC-7 | `test_ac7_top_ten_revenue`, `test_ac7_top_ten_share_reconciles` | T3 | scott-c-robinson |
| T10 (#12) | 2 | Years active for the top-10 customers | AC-8 | `test_ac8_years_active_distribution` | T9 | scott-c-robinson |
| T11 (#13) | 2 | Revenue per sales rep | AC-9 | `test_ac9_rep_revenue`, `test_ac9_rep_revenue_reconciles` | T3 | scott-c-robinson |
| T12 (#14) | 2 | Customers per rep and revenue per customer | AC-10 | `test_ac10_rep_customers`, `test_ac10_revenue_per_customer` | T11 | scott-c-robinson |
| T13 (#15) | 2 | All breakdowns add up to the grand total | AC-12 | `test_ac12_genre_country_year_rep_each_sum_to_total` | T4, T5, T7, T11 | scott-c-robinson |
| T14 (#16) | 3 | Shared page frame: screen menu, total tile, period and "ties to Finance" caption | AC-11 | `test_ac11_every_screen_shows_total_and_period` | T3 | scott-c-robinson |
| T15 (#17) | 3 | Screen 1 view: genres, countries, combinations | AC-1, AC-3, AC-4 | `test_ac1_screen1_shows_top_genres`, `test_ac3_screen1_shows_top_countries`, `test_ac4_screen1_shows_top_combinations` | T4, T5, T6, T14 | scott-c-robinson |
| T16 (#18) | 3 | Screen 2 view: Growth | AC-5, AC-6 | `test_ac5_screen2_shows_yearly_and_change`, `test_ac6_screen2_shows_sixty_months` | T7, T8, T14 | scott-c-robinson |
| T17 (#19) | 3 | Screen 3 view: Customers | AC-7, AC-8 | `test_ac7_screen3_shows_top_ten_share`, `test_ac8_screen3_shows_years_bought` | T9, T10, T14 | scott-c-robinson |
| T18 (#20) | 3 | Screen 4 view: Sales reps | AC-9, AC-10 | `test_ac9_screen4_shows_rep_revenue`, `test_ac10_screen4_shows_customers_and_average` | T11, T12, T14 | scott-c-robinson |
| T19 (#21) | 4 | Year picker on Screen 1 | AC-2 | `test_ac2_year_2023_total_and_top_genre` | T15 | scott-c-robinson |
| T20 (#22) | 4 | Other screens ignore the year picker | AC-13 | `test_ac13_screens_2_3_4_stay_full_period` | T16, T17, T18, T19 | scott-c-robinson |
| T21 (#23) | 5 | Check every style rule in `design.md` holds on all four screens | none | Criteria: headlines state a number, number formats follow `design.md`, accent color only on the highlighted item. Tests: none new; the full suite stays green | T20 | scott-c-robinson |
| T22 (#24) | 5 | Delete `mockup.py`, add the live link to the README, final deploy | none | Criteria: `mockup.py` is gone, the README's live link opens the app. Tests: none new; the full suite stays green | T21, T2 | scott-c-robinson |
