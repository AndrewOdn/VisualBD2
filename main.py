import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
date1 = [
datetime.datetime(2021, 2, 11),
datetime.datetime(2021, 2, 12),
datetime.datetime(2021, 2, 13),
datetime.datetime(2021, 2, 14),
datetime.datetime(2021, 2, 15),
datetime.datetime(2021, 2, 16),
datetime.datetime(2021, 2, 17),
datetime.datetime(2021, 2, 18),
datetime.datetime(2021, 2, 19),
datetime.datetime(2021, 2, 20),
datetime.datetime(2021, 2, 21),
datetime.datetime(2021, 2, 22),
datetime.datetime(2021, 2, 23),
datetime.datetime(2021, 2, 24),
datetime.datetime(2021, 3, 7),
datetime.datetime(2021, 3, 8),
datetime.datetime(2021, 3, 9),
datetime.datetime(2021, 3, 10),
datetime.datetime(2021, 3, 11),
datetime.datetime(2021, 3, 12),
datetime.datetime(2021, 3, 13),
datetime.datetime(2021, 3, 15),
datetime.datetime(2021, 3, 16),
datetime.datetime(2021, 3, 17),
datetime.datetime(2021, 3, 19),
datetime.datetime(2021, 3, 20),
datetime.datetime(2021, 3, 21),
datetime.datetime(2021, 3, 22),
datetime.datetime(2021, 3, 23),
datetime.datetime(2021, 3, 24),
datetime.datetime(2021, 3, 25),
datetime.datetime(2021, 3, 26),
datetime.datetime(2021, 3, 27),
datetime.datetime(2021, 3, 28),
datetime.datetime(2021, 3, 29),
datetime.datetime(2021, 3, 30),
datetime.datetime(2021, 3, 31),
datetime.datetime(2021, 4, 1),
datetime.datetime(2021, 4, 2),
datetime.datetime(2021, 4, 3),
datetime.datetime(2021, 4, 4),
datetime.datetime(2021, 4, 6),
datetime.datetime(2021, 4, 7),
datetime.datetime(2021, 4, 8),
datetime.datetime(2021, 4, 9),
datetime.datetime(2021, 4, 12),
datetime.datetime(2021, 4, 13),
datetime.datetime(2021, 4, 14),
datetime.datetime(2021, 4, 15),
datetime.datetime(2021, 4, 17),
datetime.datetime(2021, 4, 18),
datetime.datetime(2021, 4, 20),
datetime.datetime(2021, 5, 1),
datetime.datetime(2021, 5, 3),
datetime.datetime(2021, 5, 4),
datetime.datetime(2021, 5, 5),
datetime.datetime(2021, 5, 6),
datetime.datetime(2021, 5, 7),
datetime.datetime(2021, 5, 8),
datetime.datetime(2021, 5, 9),
datetime.datetime(2021, 5, 10),
datetime.datetime(2021, 5, 11),
datetime.datetime(2021, 5, 12),
datetime.datetime(2021, 5, 13),
datetime.datetime(2021, 5, 14),
datetime.datetime(2021, 5, 15),
datetime.datetime(2021, 5, 16),
datetime.datetime(2021, 5, 17),
datetime.datetime(2021, 5, 18),
datetime.datetime(2021, 5, 19),
datetime.datetime(2021, 5, 20),
datetime.datetime(2021, 5, 21),
datetime.datetime(2021, 5, 22),
datetime.datetime(2021, 5, 24),
datetime.datetime(2021, 5, 25),
datetime.datetime(2021, 5, 26),
datetime.datetime(2021, 5, 27),
datetime.datetime(2021, 5, 28),
datetime.datetime(2021, 5, 29),
datetime.datetime(2021, 5, 30),
datetime.datetime(2021, 5, 31),
datetime.datetime(2021, 6, 1),
datetime.datetime(2021, 6, 2),
datetime.datetime(2021, 6, 3),
datetime.datetime(2021, 6, 4),
datetime.datetime(2021, 6, 5),
datetime.datetime(2021, 6, 7),
datetime.datetime(2021, 6, 8),
datetime.datetime(2021, 6, 9),
datetime.datetime(2021, 6, 10),
datetime.datetime(2021, 6, 11),
datetime.datetime(2021, 6, 14),
datetime.datetime(2021, 6, 15),
datetime.datetime(2021, 6, 16)]
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
data = pd.read_csv(r"C:\Users\ElenaKulikova\Desktop\date.csv", parse_dates=['Date'], sep=';')
app = dash.Dash(__name__)
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Roboto:wght@300&display=swap",
        "rel": "stylesheet",
    },
]
id = ['25454', '26942']
Markets = ['Детский мир', 'Wildberries']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(children="Артикул", className="menu-title"),
                dcc.Dropdown(
                    id="id",
                    options=[
                        {"label": Id, "value": Id}
                        for Id in id
                    ],
                    value='25454',
                    clearable=False,
                    className="dropdown",
                ),
            ]
        ),
        html.Div(
            children=[
                html.Div(children="Маркет-плейс", className="menu-title"),
                dcc.Dropdown(
                    id="market",
                    options=[
                        {"label": market, "value": market}
                        for market in Markets
                    ],
                    value='Детский мир',
                    clearable=False,
                    className="dropdown",
                ),
            ]
        ),
        html.Div(
            children=[
                html.P(children="🥑", className="header-title"),
                html.H1(
                    children="AIRIS-PRESS Analytics", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of AIRIS-PRESS prices"
                    " between FEB and JUN",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children = dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False}
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="rating-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)
@app.callback(
    [Output("price-chart", "figure"), Output("volume-chart", "figure"), Output("rating-chart", "figure")],
    [Input("id", "value"), Input("market", "value"),])
def display_time_series(id, market):
    if id == '26942':
        data = pd.read_csv(r"C:\Users\ElenaKulikova\Desktop\gate.csv", parse_dates=['Date'], sep=';')
    elif id == '25454':
        data = pd.read_csv(r"C:\Users\ElenaKulikova\Desktop\date.csv", parse_dates=['Date'], sep=';')
    price_chart_figure = {
        "data": [
            {
                "x": date1,
                "y": data["Price"],
                "type": "markers+lines",
                "hovertemplate": "₽%{y:.2f}"
                                 "<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Price graph by "+str(id)+" id",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {
                "tickprefix": "₽",
                "fixedrange": True,
            },
            "colorway": ["#17B897"],
        },
    }
    volume_chart_figure = {
        "data": [
            {
                "x": date1,
                "y": data["Popular"],
                "type": "markers+lines",
            },
        ],
        "layout": {
            "title": {
                "text": "Popular graph by "+str(id)+" id",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    rating_chart_figure = {
        "data": [
            {
                "x": date1,
                "y": data["Rating"],
                "type": "markers+lines",
            },
        ],
        "layout": {
            "title": {
                "text": "Rating graph by "+str(id)+" id",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#FF9966"],
        },
    }
    return price_chart_figure, volume_chart_figure, rating_chart_figure
app.run_server(debug=True)