# Design

How the dashboard looks: each screen as drawn, and the style rules every
chart follows. `/dashkit:design` draws the screens from `spec.md` and builds
`mockup.py`; `/dashkit:review-dashboard` checks the finished app against this
file. The rules live in code in `dashboard/charts.py` and
`.streamlit/config.toml`; change a rule here and there together.

---

## Screens

### Chart choices

| # | Framed question | Chart | Why |
|---|---|---|---|
| **Screen 1: Where the money comes from** (year picker) | | | |
| 1 | Top 5 genres and their share | Ranked horizontal bars, % share on each bar | Ranking by size; bars, not a pie |
| 2 | Top 5 countries and their share | Ranked horizontal bars, % share on each bar | Same look as genres so the two read together |
| 3 | Top genre-and-country combinations | Ranked horizontal bars, top 10, labelled "USA · Rock" | A ranking; the spec commits to the top three, ten gives context |
| **Screen 2: Growth** | | | |
| 4 | Revenue per year and % change | Line over the five years, % change on each point | Change over time is a line |
| 5 | Monthly revenue | Line over the 60 months | The pattern behind the yearly line |
| **Screen 3: Customers** | | | |
| 6 | Top-10 customers' share of revenue | Ranked bars of the top 10, share as a headline tile | The tile gives the answer; the bars show who they are |
| 7 | Years each top-10 customer bought | Table (customer, years bought out of 5) | Exact values to look up |
| **Screen 4: Sales reps** | | | |
| 8 | Revenue per rep | Ranked horizontal bars | Comparing three reps by size |
| 9 | Customers and revenue per customer, per rep | Table (rep, customers, revenue per customer) | Exact values, three rows |
| **All screens** | | | |
| 10 | Does everything tie out with Finance? | Tile on every screen: grand total plus date range, with a small "ties to Finance, gap 0.00" caption | One number Morgan can quote |

### Headline tiles

| Screen | Tiles |
|---|---|
| 1. Where the money comes from | Total revenue for the chosen years · Top genre's share · Top country's share |
| 2. Growth | Total revenue · Best year · Latest year's % change (2025 ends 22 Dec, flagged as a partial year) |
| 3. Customers | Total revenue · Top-10 share of revenue · Top-10 customers who bought in all 5 years |
| 4. Sales reps | Total revenue · Total customers · Average revenue per customer |

### Screen drawings

Each headline states its takeaway with a number computed from the data; the
figures below are the spec's, shown as examples. The caption under each
headline gives the metric, period and filters.

**Screen 1: Where the money comes from**

```
+-----------------+--------------------------------------------------+
| SIDEBAR         | Rock and Latin bring in over half our revenue    |
|                 |                                                  |
| Year            | [Total revenue] [Top genre share] [Top country   |
| [ All years v ] |  $2,329          35.5% Rock        share] 22.5% USA|
|                 |  Jan 2021 - 22 Dec 2025 | ties to Finance, gap 0 |
|                 |                                                  |
| (picker changes | Rock earns 35% of revenue                        |
|  every number   |   Revenue by genre, top 5, selected years        |
|  on this screen)|   Rock         ################  $827  35.5%     |
|                 |   Latin        #######           $382  16.4%     |
|                 |   Metal        #####             $261  11.2%     |
|                 |   Alt & Punk   #####             $242  10.4%     |
|                 |   TV Shows     ##                 $94   4.0%     |
|                 |   > Q1 | ranked horizontal bars                  |
|                 |                                                  |
|                 | The USA earns 22% of revenue                     |
|                 |   Revenue by billing country, top 5             |
|                 |   USA / Canada / France / Brazil / Germany      |
|                 |   (same bars and labels as genres)              |
|                 |   > Q2 | ranked horizontal bars                  |
|                 |                                                  |
|                 | USA Rock is our biggest single combination      |
|                 |   Revenue by country and genre, top 10          |
|                 |   USA - Rock  ####  $155   Canada - Rock  ###   |
|                 |   USA - Latin ###   $90    ...                  |
|                 |   > Q3 | ranked horizontal bars                  |
+-----------------+--------------------------------------------------+
```

**Screen 2: Growth** (no filters, always the full period)

```
+-----------------+--------------------------------------------------+
| SIDEBAR         | Revenue is flat: $449 in 2021, $451 in 2025      |
| (none)          |                                                  |
|                 | [Total revenue] [Best year]  [Latest year change]|
|                 |  $2,329          2022 $481    -5.6% (partial yr) |
|                 |  Jan 2021 - 22 Dec 2025 | ties to Finance, gap 0 |
|                 |                                                  |
|                 | Revenue peaked in 2022 and has not grown since   |
|                 |   Revenue per year                               |
|                 |   $481 .       .                                 |
|                 |   $449   .  .     .  .   (% change on points:    |
|                 |   2021 2022 2023 2024 2025  +7.1% -2.5% +1.7%    |
|                 |   2025 ends 22 Dec            -5.6%)             |
|                 |   > Q4 | line                                    |
|                 |                                                  |
|                 | Monthly revenue moves in a narrow band           |
|                 |   Revenue per month, Jan 2021 - Dec 2025         |
|                 |   (line across 60 months)                        |
|                 |   > Q5 | line                                    |
+-----------------+--------------------------------------------------+
```

**Screen 3: Customers** (no filters, always the full period)

```
+-----------------+--------------------------------------------------+
| SIDEBAR         | No small group carries the business: top 10 = 19%|
| (none)          |                                                  |
|                 | [Total revenue] [Top-10 share] [Bought all 5 yrs]|
|                 |  $2,329          19.4%         2 of 10 customers |
|                 |  Jan 2021 - 22 Dec 2025 | ties to Finance, gap 0 |
|                 |                                                  |
|                 | Our top 10 customers bring in 19% of revenue     |
|                 |   Revenue by customer, top 10                    |
|                 |   (ranked horizontal bars, one per customer)     |
|                 |   > Q6 | ranked bars + Top-10 share tile         |
|                 |                                                  |
|                 | Only 2 of our top 10 bought in all five years    |
|                 |   Years bought, top 10 customers                 |
|                 |   Customer          | Years bought (of 5)        |
|                 |   ...               | 5 / 4 / 3                  |
|                 |   > Q7 | table                                   |
+-----------------+--------------------------------------------------+
```

**Screen 4: Sales reps** (no filters, always the full period)

```
+-----------------+--------------------------------------------------+
| SIDEBAR         | Every rep's customers are worth about $39 each   |
| (none)          |                                                  |
|                 | [Total revenue] [Total customers] [Avg per cust.]|
|                 |  $2,329          59               $39.47         |
|                 |  Jan 2021 - 22 Dec 2025 | ties to Finance, gap 0 |
|                 |                                                  |
|                 | Jane's customers bring in the most: $833         |
|                 |   Revenue from each rep's customers              |
|                 |   Jane     ################  $833                |
|                 |   Margaret ###############   $775                |
|                 |   Steve    ##############    $720                |
|                 |   > Q8 | ranked horizontal bars                  |
|                 |                                                  |
|                 | Each rep's customers are worth about $39 each    |
|                 |   Rep         | Customers | Revenue per customer |
|                 |   Jane        | 21        | $39.67               |
|                 |   Margaret    | 20        | $38.77               |
|                 |   Steve       | 18        | $40.01               |
|                 |   > Q9 | table                                   |
|                 |   (context only; says nothing about cause)       |
+-----------------+--------------------------------------------------+
```

Question 10 (does it tie out with Finance?) appears on every screen as the
total tile and its "ties to Finance, gap 0.00" caption.

---

## Style rules

### Page

- Each screen opens with one sentence stating the main takeaway, then a row
  of three or four headline numbers (`charts.kpi_row`), each shown against a
  comparison: last year, a target, or the average.
- Then one section per framed question, in the order the stakeholder's
  decision needs them.
- Filters sit in the sidebar and apply to the whole screen. Their defaults
  show the most recent complete period.

### Choosing a chart

| The question compares | Chart | Helper |
|---|---|---|
| Items ranked by size | Horizontal bars, largest at the top | `charts.ranked_bar` |
| Change over time | A line | `charts.trend_line` |
| Shares of a whole (up to five parts) | Horizontal bars of percentages, not a pie | `charts.ranked_bar(kind="percent")` |
| Exact values someone will look up | A table | `st.dataframe` |

Anything else (a distribution, two measures against each other): agree on
the chart with the team before building it, and add a row here.

### Words

- Every section's headline states its takeaway with the number, computed
  from the data: "Rock earns 35% of revenue", not "Revenue by genre"
  (`charts.headline`).
- Under the headline, one caption: the metric, its period, and its filters,
  as `spec.md` defines them.
- Labels in plain words, never column names: "Revenue", not
  `total_revenue`. Sentence case.

### Numbers

- Money in whole dollars ($1,234), with cents under $10 ($5.65); counts
  with separators (1,234); percentages to one decimal (12.3%).
- Bars start at zero.

### Color

- One accent color for what the headline is about; neutral gray for
  everything else; red only for a loss or a miss.
- A category keeps the same color on every chart.
- Color never carries a meaning alone: the headline or a label says it too.
- Nothing decorative: no 3-D, no background images, gridlines only where
  reading a value needs them.

### When there is nothing to show

- A filter that leaves no rows shows a short note (`charts.nothing_to_show`)
  in place of an error or an empty chart.
