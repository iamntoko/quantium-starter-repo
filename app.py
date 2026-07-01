import dash
from dash import html, dcc
import pandas as pd

# Load and preprocess the data
df = pd.read_csv('pink_morsel_sales.csv')
df['Date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Aggregate sales by date
daily_sales = df.groupby('date', as_index=False)['sales'].sum()

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard"),
    dcc.Graph(
        id='sales-line-chart',
        figure={
            'data': [
                {'x': daily_sales['date'], 'y': daily_sales['sales'], 'type': 'line', 'name': 'Sales'},
            ],
            'layout': {
                'title': 'Pink Morsel Sales Over Time',
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Sales ($)'},
            },
        },
    ),
])    

if __name__ == '__main__':
    app.run(debug=True)