import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html

df = pd.read_csv("new_data.csv")
df["date"] = pd.to_datetime(df["date"])
df_daily = df.groupby("date")["sales"].sum().reset_index().sort_values("date")

PRICE_INCREASE_DATE = "2021-01-15"

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_daily["date"],
    y=df_daily["sales"],
    mode="lines",
    line=dict(color="red"),
    name="Daily Sales"
))

fig.add_vline(
    x=pd.Timestamp(PRICE_INCREASE_DATE).timestamp() * 1000,
    line_dash="dash",
    line_color="gray",
    annotation_text="Price Increase (Jan 15, 2021)",
    annotation_position="top left"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales ($)",
    plot_bgcolor="white",
    paper_bgcolor="white",
    xaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
    yaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Visualiser",
        style={"textAlign": "center", "fontFamily": "Arial, sans-serif", "color": "#333"}
    ),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
