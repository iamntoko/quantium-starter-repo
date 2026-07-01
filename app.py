import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd

# Load and preprocess the data
df = pd.read_csv('pink_morsel_sales.csv')
df['Date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Aggregate sales by date
daily_sales = df.groupby('date', as_index=False)['sales'].sum()

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    style={
        "fontFamily": "'Segoe UI', Arial, sans-serif",
        "textAlign": "center",
        "backgroundColor": "#fff0f5",
        "padding": "40px",
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"color": "#d6336c", "marginBottom": "10px"},
        ),
        html.P(
            "Explore how Pink Morsel sales changed after the January 2021 price increase.",
            style={"color": "#495057", "marginBottom": "30px"},
        ),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all",
            inline=True,
            labelStyle={"marginRight": "20px", "fontSize": "16px"},
            style={"marginBottom": "30px"},
        ),
        dcc.Graph(id="sales-line-chart"),
    ],
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(region):
    filtered = df if region == "all" else df[df["region"] == region]
    daily_sales = filtered.groupby("date", as_index=False)["sales"].sum()
    return {
        "data": [
            {
                "x": daily_sales["date"],
                "y": daily_sales["sales"],
                "type": "line",
                "name": "Sales",
                "line": {"color": "#d6336c"},
            }
        ],
        "layout": {
            "title": f"Pink Morsel Sales — {region.title() if region != 'all' else 'All Regions'}",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "Sales ($)"},
            "plot_bgcolor": "#fff",
            "paper_bgcolor": "#fff0f5",
        },
    }

if __name__ == "__main__":
    app.run(debug=True)