import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback

df = pd.read_csv("new_data.csv")
df["date"] = pd.to_datetime(df["date"])

PRICE_INCREASE_DATE = "2021-01-15"
BRAND_PINK = "#38bdf8"       # sky blue accent
BRAND_BLUE = "#818cf8"       # indigo accent
GRAY_100 = "#1e293b"         # card/panel background
GRAY_200 = "#334155"         # borders
GRAY_500 = "#94a3b8"         # muted text
GRAY_700 = "#cbd5e1"         # secondary text
GRAY_900 = "#f1f5f9"         # primary text
WHITE = "#0f172a"            # page/plot background

app = Dash(__name__, title="Soul Foods — Pink Morsel Sales")

app.layout = html.Div(
    style={
        "fontFamily": "'Inter', 'Segoe UI', Arial, sans-serif",
        "backgroundColor": GRAY_100,
        "minHeight": "100vh",
        "margin": "0",
        "padding": "0",
    },
    children=[

        # Top navigation bar
        html.Div(
            style={
                "backgroundColor": WHITE,
                "borderBottom": f"1px solid {GRAY_200}",
                "padding": "0 40px",
                "height": "60px",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "space-between",
                "boxShadow": "0 1px 3px rgba(0,0,0,0.06)",
            },
            children=[
                html.Div(
                    style={"display": "flex", "alignItems": "center", "gap": "12px"},
                    children=[
                        html.Div(
                            style={
                                "width": "8px",
                                "height": "28px",
                                "backgroundColor": BRAND_PINK,
                                "borderRadius": "2px",
                            }
                        ),
                        html.Span(
                            "Soul Foods",
                            style={"fontWeight": "700", "fontSize": "1rem", "color": GRAY_900, "letterSpacing": "-0.2px"}
                        ),
                        html.Span(
                            "Analytics",
                            style={"fontWeight": "400", "fontSize": "1rem", "color": GRAY_500}
                        ),
                    ]
                ),
                html.Span(
                    "Pink Morsel Sales Report",
                    style={"fontSize": "0.82rem", "color": GRAY_500, "letterSpacing": "0.3px"}
                ),
            ]
        ),

        # Page content
        html.Div(
            style={"padding": "36px 40px", "maxWidth": "1400px", "margin": "0 auto"},
            children=[

                # Page title block
                html.Div(
                    style={"marginBottom": "32px"},
                    children=[
                        html.H1(
                            "Pink Morsel Sales Performance",
                            style={
                                "color": GRAY_900,
                                "fontSize": "1.75rem",
                                "fontWeight": "700",
                                "margin": "0 0 6px 0",
                                "letterSpacing": "-0.5px",
                            }
                        ),
                        html.P(
                            "Analysing daily sales revenue across regions to evaluate the impact of the January 2021 price increase.",
                            style={"color": GRAY_500, "fontSize": "0.92rem", "margin": "0"}
                        ),
                    ]
                ),

                # KPI cards
                html.Div(
                    id="kpi-row",
                    style={
                        "display": "grid",
                        "gridTemplateColumns": "repeat(4, 1fr)",
                        "gap": "16px",
                        "marginBottom": "24px",
                    }
                ),

                # Chart card
                html.Div(
                    style={
                        "backgroundColor": WHITE,
                        "borderRadius": "10px",
                        "border": f"1px solid {GRAY_200}",
                        "boxShadow": "0 1px 4px rgba(0,0,0,0.05)",
                        "overflow": "hidden",
                    },
                    children=[

                        # Chart header
                        html.Div(
                            style={
                                "padding": "20px 24px 16px 24px",
                                "borderBottom": f"1px solid {GRAY_200}",
                                "display": "flex",
                                "justifyContent": "space-between",
                                "alignItems": "center",
                                "flexWrap": "wrap",
                                "gap": "12px",
                            },
                            children=[
                                html.Div([
                                    html.H2(
                                        "Daily Revenue Over Time",
                                        style={"color": GRAY_900, "fontSize": "1rem", "fontWeight": "600", "margin": "0 0 2px 0"}
                                    ),
                                    html.P(
                                        "Segmented by region — dashed line marks the price increase on 15 Jan 2021",
                                        style={"color": GRAY_500, "fontSize": "0.78rem", "margin": "0"}
                                    ),
                                ]),

                                # Region filter
                                html.Div(
                                    style={"display": "flex", "alignItems": "center", "gap": "10px"},
                                    children=[
                                        html.Span(
                                            "Region",
                                            style={"fontSize": "0.8rem", "color": GRAY_500, "fontWeight": "500"}
                                        ),
                                        dcc.RadioItems(
                                            id="region-filter",
                                            options=[
                                                {"label": "All", "value": "all"},
                                                {"label": "North", "value": "north"},
                                                {"label": "East", "value": "east"},
                                                {"label": "South", "value": "south"},
                                                {"label": "West", "value": "west"},
                                            ],
                                            value="all",
                                            inline=True,
                                            inputStyle={
                                                "marginRight": "4px",
                                                "accentColor": BRAND_PINK,
                                                "cursor": "pointer",
                                            },
                                            labelStyle={
                                                "marginRight": "14px",
                                                "color": GRAY_700,
                                                "cursor": "pointer",
                                                "fontSize": "0.82rem",
                                                "fontWeight": "500",
                                            },
                                        ),
                                    ]
                                ),
                            ]
                        ),

                        dcc.Graph(
                            id="sales-chart",
                            config={"displayModeBar": False},
                            style={"padding": "0"},
                        ),
                    ]
                ),

                # Footer
                html.Div(
                    style={"marginTop": "24px", "display": "flex", "justifyContent": "space-between", "alignItems": "center"},
                    children=[
                        html.P(
                            "Data sourced from Soul Foods internal transaction records (2018–2021)",
                            style={"color": GRAY_500, "fontSize": "0.75rem", "margin": "0"}
                        ),
                        html.P(
                            "Soul Foods Analytics — Confidential",
                            style={"color": GRAY_500, "fontSize": "0.75rem", "margin": "0"}
                        ),
                    ]
                ),
            ]
        ),
    ]
)


def kpi_card(label, value, detail, accent):
    return html.Div(
        style={
            "backgroundColor": WHITE,
            "borderRadius": "10px",
            "border": f"1px solid {GRAY_200}",
            "boxShadow": "0 1px 4px rgba(0,0,0,0.05)",
            "padding": "20px 24px",
        },
        children=[
            html.Div(
                style={"display": "flex", "justifyContent": "space-between", "alignItems": "flex-start", "marginBottom": "12px"},
                children=[
                    html.P(label, style={"color": GRAY_500, "fontSize": "0.78rem", "fontWeight": "500", "margin": "0", "textTransform": "uppercase", "letterSpacing": "0.6px"}),
                    html.Div(style={"width": "8px", "height": "8px", "borderRadius": "50%", "backgroundColor": accent, "marginTop": "4px"}),
                ]
            ),
            html.P(value, style={"color": GRAY_900, "fontSize": "1.6rem", "fontWeight": "700", "margin": "0 0 4px 0", "letterSpacing": "-0.5px"}),
            html.P(detail, style={"color": GRAY_500, "fontSize": "0.75rem", "margin": "0"}),
        ]
    )


@callback(
    Output("sales-chart", "figure"),
    Output("kpi-row", "children"),
    Input("region-filter", "value"),
)
def update(region):
    filtered = df if region == "all" else df[df["region"] == region]
    df_daily = filtered.groupby("date")["sales"].sum().reset_index().sort_values("date")

    price_date = pd.Timestamp(PRICE_INCREASE_DATE)
    before_df = df_daily[df_daily["date"] < price_date]
    after_df = df_daily[df_daily["date"] >= price_date]

    total = df_daily["sales"].sum()
    before_total = before_df["sales"].sum()
    after_total = after_df["sales"].sum()
    pct_change = ((after_df["sales"].mean() - before_df["sales"].mean()) / before_df["sales"].mean()) * 100
    cards = [
        kpi_card("Total Revenue", f"${total:,.0f}", f"{'All regions' if region == 'all' else region.capitalize()} · Full period", GRAY_500),
        kpi_card("Before Price Increase", f"${before_total:,.0f}", f"Up to 14 Jan 2021 · {len(before_df)} days", BRAND_BLUE),
        kpi_card("After Price Increase", f"${after_total:,.0f}", f"From 15 Jan 2021 · {len(after_df)} days", BRAND_PINK),
        kpi_card("Avg Daily Change", f"{pct_change:+.1f}%", "Mean daily revenue vs prior period", "#059669" if pct_change >= 0 else "#dc2626"),
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=before_df["date"], y=before_df["sales"],
        mode="lines", name="Before Increase",
        line=dict(color=BRAND_BLUE, width=1.8),
        fill="tozeroy", fillcolor="rgba(37,99,235,0.07)",
        hovertemplate="<b>%{x|%b %d, %Y}</b><br>Revenue: $%{y:,.0f}<extra></extra>",
    ))

    fig.add_trace(go.Scatter(
        x=after_df["date"], y=after_df["sales"],
        mode="lines", name="After Increase",
        line=dict(color=BRAND_PINK, width=1.8),
        fill="tozeroy", fillcolor="rgba(192,57,90,0.07)",
        hovertemplate="<b>%{x|%b %d, %Y}</b><br>Revenue: $%{y:,.0f}<extra></extra>",
    ))

    fig.add_vline(
        x=price_date.timestamp() * 1000,
        line_dash="dot",
        line_color=GRAY_500,
        line_width=1.5,
        annotation_text="Price increase",
        annotation_position="top",
        annotation_font_color=GRAY_500,
        annotation_font_size=11,
    )

    fig.update_layout(
        plot_bgcolor=WHITE,
        paper_bgcolor=WHITE,
        font=dict(family="'Inter', 'Segoe UI', Arial, sans-serif", color=GRAY_700, size=12),
        xaxis=dict(
            title=dict(text="Date", font=dict(size=11, color=GRAY_500)),
            showgrid=True,
            gridcolor=GRAY_100,
            gridwidth=1,
            zeroline=False,
            tickfont=dict(size=11, color=GRAY_500),
            showline=True,
            linecolor=GRAY_200,
        ),
        yaxis=dict(
            title=dict(text="Revenue (USD)", font=dict(size=11, color=GRAY_500)),
            showgrid=True,
            gridcolor=GRAY_100,
            gridwidth=1,
            zeroline=False,
            tickfont=dict(size=11, color=GRAY_500),
            tickprefix="$",
            tickformat=",",
            showline=False,
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=11, color=GRAY_700),
        ),
        margin=dict(t=40, b=48, l=64, r=24),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor=WHITE,
            bordercolor=GRAY_200,
            font_color=GRAY_900,
            font_size=12,
        ),
        height=420,
    )

    return fig, cards


if __name__ == "__main__":
    app.run(debug=True)
