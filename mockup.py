"""A clickable mockup of the four screens drawn in design.md.

Run it with:  streamlit run mockup.py

Every number here is fixed and made up (some borrow the spec's figures so the
layout looks realistic). This file never connects to the database. Every
headline, tile, and chart goes through dashboard/charts.py.
"""

import pandas as pd
import streamlit as st

from dashboard import charts

st.set_page_config(page_title="Vinyl Vault mockup", layout="wide")

PERIOD = "Jan 2021 - 22 Dec 2025"
TOTAL = 2328.60
YEARS = {2021: 449.46, 2022: 481.45, 2023: 469.58, 2024: 477.53, 2025: 450.58}
GENRES = {"Rock": 826.65, "Latin": 382.14, "Metal": 261.36,
          "Alternative & Punk": 241.56, "TV Shows": 93.53}
COUNTRIES = {"USA": 523.06, "Canada": 303.96, "France": 195.10,
             "Brazil": 190.10, "Germany": 156.48}
COMBOS = {"USA - Rock": 155.43, "Canada - Rock": 105.93, "USA - Latin": 90.09,
          "France - Rock": 62.37, "Brazil - Rock": 58.41, "Germany - Rock": 49.50,
          "USA - Metal": 46.53, "USA - Alternative & Punk": 43.56,
          "Canada - Latin": 40.59, "Brazil - Latin": 37.62}
CUSTOMERS = {"Customer A": (52.62, 5), "Customer B": (50.62, 4),
             "Customer C": (49.62, 4), "Customer D": (47.62, 3),
             "Customer E": (46.62, 5), "Customer F": (45.62, 4),
             "Customer G": (43.62, 3), "Customer H": (42.62, 4),
             "Customer I": (36.62, 3), "Customer J": (35.62, 4)}
REPS = {"Jane": (833.04, 21), "Margaret": (775.40, 20), "Steve": (720.16, 18)}
MONTH_SHAPE = [0.92, 0.85, 1.00, 1.05, 0.95, 1.10, 0.90, 1.00, 1.08, 0.97, 1.05, 1.13]


def money(text: str) -> str:
    """Escape dollar signs so Streamlit does not read them as math."""
    return text.replace("$", "\\$")


def tiles(items: list[dict]) -> None:
    charts.kpi_row(items)
    st.caption(money(f"{PERIOD} | ties to Finance, gap $0.00"))


def ranked(names_values: dict, total: float, label: str, top: int = 10) -> None:
    """Ranked bars where each label also carries the item's share."""
    df = pd.DataFrame({label: list(names_values), "Revenue": list(names_values.values())})
    df[label] = [f"{n} ({v / total:.1%})" for n, v in zip(df[label], df["Revenue"])]
    charts.show(charts.ranked_bar(df, label, "Revenue", top=top))


# ---------------------------------------------------------------- sidebar
st.sidebar.title("Vinyl Vault")
screen = st.sidebar.radio(
    "Screen",
    ["1. Where the money comes from", "2. Growth", "3. Customers", "4. Sales reps"],
)
year = None
if screen.startswith("1"):
    pick = st.sidebar.selectbox("Year", ["All years", *YEARS])
    year = None if pick == "All years" else pick

st.warning("Mockup: made-up numbers")

# --------------------------------------------------------------- screen 1
if screen.startswith("1"):
    scale = 1.0 if year is None else YEARS[year] / TOTAL
    total = TOTAL * scale
    genres = {k: v * scale for k, v in GENRES.items()}
    countries = {k: v * scale for k, v in COUNTRIES.items()}
    combos = {k: v * scale for k, v in COMBOS.items()}
    g1, g2 = list(genres)[:2]
    both = (genres[g1] + genres[g2]) / total
    scope = "all years" if year is None else str(year)

    charts.headline(
        money(f"{g1} and {g2} bring in {both:.0%} of our revenue"),
        f"Revenue = unit price x quantity. Period: {scope}.",
    )
    tiles([
        {"label": "Total revenue", "value": total, "kind": "money"},
        {"label": f"Top genre share ({g1})", "value": genres[g1] / total, "kind": "percent"},
        {"label": f"Top country share ({list(countries)[0]})",
         "value": list(countries.values())[0] / total, "kind": "percent"},
    ])

    charts.headline(
        f"{g1} earns {genres[g1] / total:.0%} of revenue",
        f"Revenue by genre, top 5. Period: {scope}. Question 1.",
    )
    ranked(genres, total, "Genre", top=5)

    c1 = list(countries)[0]
    charts.headline(
        f"The {c1} earns {countries[c1] / total:.0%} of revenue",
        f"Revenue by billing country, top 5. Period: {scope}. Question 2.",
    )
    ranked(countries, total, "Country", top=5)

    top_combo = list(combos)[0]
    charts.headline(
        f"{top_combo.replace(' - ', ' ')} is our biggest single combination",
        f"Revenue by billing country and genre, top 10. Period: {scope}. Question 3.",
    )
    ranked(combos, total, "Country and genre", top=10)

# --------------------------------------------------------------- screen 2
elif screen.startswith("2"):
    first, last = YEARS[2021], YEARS[2025]
    best = max(YEARS, key=YEARS.get)
    change = YEARS[2025] / YEARS[2024] - 1

    charts.headline(
        money(f"Revenue is flat: ${first:,.0f} in 2021, ${last:,.0f} in 2025"),
        f"Revenue = unit price x quantity. Period: {PERIOD}.",
    )
    tiles([
        {"label": "Total revenue", "value": TOTAL, "kind": "money"},
        {"label": f"Best year ({best})", "value": YEARS[best], "kind": "money"},
        {"label": "Latest year vs 2024 (2025 ends 22 Dec)", "value": YEARS[2025], "kind": "money",
         "delta": YEARS[2025] - YEARS[2024], "versus": f"({change:+.1%})"},
    ])

    charts.headline(
        f"Revenue peaked in {best} and has not grown since",
        f"Revenue per year, {PERIOD}. Question 4.",
    )
    yearly = pd.DataFrame({"Year": [str(y) for y in YEARS], "Revenue": list(YEARS.values())})
    fig = charts.trend_line(yearly, "Year", "Revenue")
    values = list(YEARS.values())
    for i in range(1, len(values)):
        pct = values[i] / values[i - 1] - 1
        fig.add_annotation(
            x=str(list(YEARS)[i]), y=values[i], text=f"{pct:+.1%}", showarrow=False,
            yshift=-22, font={"color": charts.NEGATIVE if pct < 0 else charts.TEXT, "size": 12},
        )
    charts.show(fig)

    months, amounts = [], []
    for y, y_total in YEARS.items():
        norm = sum(MONTH_SHAPE) / 12
        for m, shape in enumerate(MONTH_SHAPE, start=1):
            months.append(pd.Timestamp(year=y, month=m, day=1))
            amounts.append(y_total / 12 * shape / norm)
    monthly = pd.DataFrame({"Month": months, "Revenue": amounts})
    charts.headline(
        "Monthly revenue moves in a narrow band",
        f"Revenue per month, {PERIOD}. Question 5.",
    )
    charts.show(charts.trend_line(monthly, "Month", "Revenue", kind="money"))

# --------------------------------------------------------------- screen 3
elif screen.startswith("3"):
    top10 = {name: rev for name, (rev, _) in CUSTOMERS.items()}
    share = sum(top10.values()) / TOTAL
    all5 = sum(1 for _, yrs in CUSTOMERS.values() if yrs == 5)

    charts.headline(
        f"No small group carries the business: the top 10 are {share:.0%} of revenue",
        f"Revenue = unit price x quantity. Period: {PERIOD}.",
    )
    tiles([
        {"label": "Total revenue", "value": TOTAL, "kind": "money"},
        {"label": "Top-10 customers' share of revenue", "value": share, "kind": "percent"},
        {"label": "Top-10 customers who bought in all 5 years", "value": all5, "kind": "count"},
    ])

    charts.headline(
        f"Our top 10 customers bring in {share:.0%} of revenue",
        f"Revenue by customer, top 10. Period: {PERIOD}. Question 6.",
    )
    df = pd.DataFrame({"Customer": list(top10), "Revenue": list(top10.values())})
    charts.show(charts.ranked_bar(df, "Customer", "Revenue"))

    charts.headline(
        f"Only {all5} of our top 10 bought in all five years",
        f"Years with at least one purchase, top 10 customers. Period: {PERIOD}. Question 7.",
    )
    table = pd.DataFrame(
        [(name, yrs) for name, (_, yrs) in CUSTOMERS.items()],
        columns=["Customer", "Years bought (of 5)"],
    )
    st.dataframe(table, hide_index=True, width="stretch")

# --------------------------------------------------------------- screen 4
else:
    customers = sum(n for _, n in REPS.values())
    per_customer = {rep: rev / n for rep, (rev, n) in REPS.items()}
    lead = max(REPS, key=lambda r: REPS[r][0])

    charts.headline(
        money(f"Every rep's customers are worth about ${TOTAL / customers:,.0f} each"),
        f"Revenue = unit price x quantity. Period: {PERIOD}.",
    )
    tiles([
        {"label": "Total revenue", "value": TOTAL, "kind": "money"},
        {"label": "Total customers", "value": customers, "kind": "count"},
        {"label": "Average revenue per customer", "value": TOTAL / customers, "kind": "money"},
    ])

    charts.headline(
        money(f"{lead}'s customers bring in the most: ${REPS[lead][0]:,.0f}"),
        f"Revenue from each rep's customers. Period: {PERIOD}. Question 8.",
    )
    df = pd.DataFrame({"Rep": list(REPS), "Revenue": [r for r, _ in REPS.values()]})
    charts.show(charts.ranked_bar(df, "Rep", "Revenue"))

    charts.headline(
        money(f"Each rep's customers are worth about ${TOTAL / customers:,.0f} each"),
        "Customers and revenue per customer, per rep. Context only: it does not show "
        f"that a rep caused the sales. Period: {PERIOD}. Question 9.",
    )
    table = pd.DataFrame({
        "Rep": list(REPS),
        "Customers": [n for _, n in REPS.values()],
        "Revenue per customer": [f"${per_customer[r]:,.2f}" for r in REPS],
    })
    st.dataframe(table, hide_index=True, width="stretch")
