import dash
import dash_html_components as html
import pandas as pd
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import numpy as np
from datetime import date
from datetime import datetime as dt
import dash_bootstrap_components as dbc

# load the data and transform date time column
m_data = pd.read_csv("data/processed/processed_survey.csv")
m_data['Timestamp'] = pd.to_datetime(m_data['Timestamp'])
sdate = m_data['Timestamp'].min()
edate = m_data['Timestamp'].max()
all_countries = m_data['Country'].unique()
some_countries = all_countries[:5]
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define content style
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "15rem",
    "padding": "2rem 1rem",
    "background-color": "#15599e",
    "color": "white"
}


sidebar = html.Div(
    [
        html.H5("Tech Worker Mental Health Tracker"),
        html.Hr(),
        html.P(
            "Filter By: ", className="lead"
        ),
        html.Div([ # Filter by Countries Widget
            html.Label(['Countries:', dcc.Dropdown(id = 'country_wid', value = some_countries,
         options=[{'label': con, 'value': con } for con in all_countries], multi = True, style = {'color': 'black'})]),
        html.Hr(),
        # Filter by Dates Widget
        html.Label(['Dates:', dcc.DatePickerRange(id='date_range', start_date = sdate, end_date= edate, style = {'display' : "inline-block"})]) 
    ],
)], style=SIDEBAR_STYLE,)

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Organize Charts into Grid Style
content = html.Div([dbc.Row([dbc.Col([html.Iframe(id = 'country_bar', style={'border-width': '0', 'width': '150%', 'height': '450px'})]),
                       dbc.Col([html.Iframe(id = 'fam_hist', style={'border-width': '0', 'width': '150%', 'height': '450px'})])]),
               dbc.Row([dbc.Col([html.Iframe(id = 'sought_help', style={'border-width': '0', 'width': '150%', 'height': '450px'})]),
                        dbc.Col([html.Iframe(id = 'benefits', style={'border-width': '0', 'width': '150%', 'height': '450px'})])])], style = CONTENT_STYLE)



app.layout = html.Div([sidebar, content])



@app.callback(
    Output('country_bar', 'srcDoc'),
    Input('country_wid', 'value'),
    Input('date_range', 'start_date'),
    Input('date_range', 'end_date')
)

# plot the Country Frequency Bar Chart
def plot_country_bar(countries, start_date, end_date):
    data = m_data[m_data['Country'].isin(countries)]
    data = data[(data['Timestamp'] >= start_date) & (data['Timestamp'] <= end_date)]
    chart = alt.Chart(data, title = 'Location of Respondent and Whether They Sought Help').mark_bar().encode(
        x = alt.X('Country', sort = '-y'),
        y = alt.Y('sum(prop)', axis=alt.Axis(format='%'), title='Proportion of population'), 
        tooltip = 'sum(prop)', 
        color = alt.Color('seek_help', title = 'Sought Help')).properties(width=300)
    return chart.to_html()


@app.callback(
    Output('fam_hist', 'srcDoc'),
    Input('country_wid', 'value'),
    Input('date_range', 'start_date'),
    Input('date_range', 'end_date')
)

# Plot Family History Bar Chart
def plot_fam_hist_bar(countries, start_date, end_date):
    data = m_data[m_data['Country'].isin(countries)]
    data = data[(data['Timestamp'] >= start_date) & (data['Timestamp'] <= end_date)]
    chart = alt.Chart(data, title = 'Family History of Mental Illness').mark_bar().encode(
        x = alt.X('family_history', title = 'Whether Family Has History of Mental Illness'),
        y = alt.Y('sum(prop)', axis=alt.Axis(format='%'), title='Proportion of population'), 
        tooltip = 'sum(prop)',
        color = 'Gender').properties(width=150)
    return chart.to_html()


@app.callback(
    Output('sought_help', 'srcDoc'),
    Input('country_wid', 'value'),
    Input('date_range', 'start_date'),
    Input('date_range', 'end_date')
)

# Plot Sought Help Bar Chart
def plot_sought_help(countries, start_date, end_date):
    data = m_data[m_data['Country'].isin(countries)]
    data = data[(data['Timestamp'] >= start_date) & (data['Timestamp'] <= end_date)]
    chart = alt.Chart(data, title = 'Sought Help').mark_bar().encode(
        x = alt.X('seek_help', title = 'Seeked Help'),
        y = alt.Y('sum(prop)', axis=alt.Axis(format='%'), title='Proportion of population'), 
        tooltip = 'sum(prop)',
        color = 'Gender').properties(width = 150)
    return chart.to_html()

@app.callback(
    Output('benefits', 'srcDoc'),
    Input('country_wid', 'value'),
    Input('date_range', 'start_date'),
    Input('date_range', 'end_date')
)

# Plot Benefits Bar Chart
def plot_benefits(countries, start_date, end_date):
    data = m_data[m_data['Country'].isin(countries)]
    data = data[(data['Timestamp'] >= start_date) & (data['Timestamp'] <= end_date)]
    chart = alt.Chart(data, title = 'Workplace Benefits').mark_bar().encode(
        x = alt.X('benefits', title = 'Workplace Benefits'),
        y = alt.Y('sum(prop)', axis=alt.Axis(format='%'), title='Proportion of population'), 
        tooltip = 'sum(prop)',
        color = 'Gender').properties(width=150)
    return chart.to_html()










if __name__ == '__main__':
    app.run_server(debug=True)