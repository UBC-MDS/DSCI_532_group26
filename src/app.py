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
all_states = m_data['state'].unique()
some_states = all_states[:3]
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

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
            html.Label(['States:', dcc.Dropdown(id = 'state_wid', value = some_states,
         options=[{'label': st, 'value': st } for st in all_states], multi = True, style = {'color': 'black'})]),
        html.Hr(),
        # Filter by Dates Widget
        html.Label(['Dates:', dcc.DatePickerRange(id='date_range', start_date = sdate, end_date= edate, style = {'display' : "inline-block"})]) 
    ],
)], style=SIDEBAR_STYLE,)

CONTENT_STYLE = {
    "margin-left": "6rem",
    "padding": "2rem 1rem",
}

# Organize Charts into Grid Style
content = dbc.Container([dbc.Row([dbc.Col([html.Iframe(id = 'state_bar', style={'border-width': '0', 'width': '100%', 'height': '400px'})]),
                       dbc.Col([html.Iframe(id = 'fam_hist', style={'border-width': '0', 'width': '150%', 'height': '450px'})])]),
                    dbc.Row([dbc.Col([html.Iframe(id = 'sought_help', style={'border-width': '0', 'width': '150%', 'height': '450px'})]),
                       dbc.Col([html.Iframe(id = 'benefits', style={'border-width': '0', 'width': '150%', 'height': '450px'})])]),
                    dbc.Row([dbc.Col([html.Iframe(id = 'interfere', style={'border-width': '0', 'width': '150%', 'height': '450px'})]),
                             dbc.Col([html.Iframe(id = 'supervisor', style={'border-width': '0', 'width': '150%', 'height': '450px'})])])])

overall = html.Div(dbc.Container([dbc.Row([dbc.Col([html.H3("Tech Worker Mental Health Tracker"), html.Label(['States:', dcc.Dropdown(id = 'state_wid', value = some_states,
                                 options=[{'label': st, 'value': st } for st in all_states], multi = True, style = {'color': 'black'})])], md = 2,
                                  style={'background-color': '#e6e6e6',
                                         'padding': 10,
                                         'border-radius': 3,
                                         'left': 0,
                                         "position": "fixed",
                                         "top": 0, "bottom": 0}),
                                  dbc.Col([dbc.Row([dbc.Col(dbc.Card([dbc.CardHeader('Did You Seek Treatment for Mental Illness', style={'fontWeight': 'bold'}),
                                                                     dbc.CardBody(html.Iframe(id = 'state_bar', style={'border-width': '0', 'width': '100%', 'height': '400px'}))]), width = 'auto'),
                                                   dbc.Col(dbc.Card([dbc.CardHeader('Does Employer Take Mental Illness Seriously', style={'fontWeight': 'bold'} ),
                                                                     dbc.CardBody(html.Iframe(id = 'fam_hist', style={'border-width': '0', 'width': '150%', 'height': '400px'}))], style={"width": "30rem"}), width = 'auto')]),
                                                   html.Br(),
                                           dbc.Row([dbc.Col(dbc.Card([dbc.CardHeader('Easiness to Leave Work Due to Mental Reason', style={'fontWeight': 'bold'}),
                                                                    dbc.CardBody(html.Iframe(id = 'sought_help', style = {'border-width': '0', 'width': '100%', 'height': '400px'}))], style={"width": "38rem"}), width = 'auto'),
                                                    dbc.Col(dbc.Card([dbc.CardHeader('Workplace Benefits Between States', style={'fontWeight': 'bold'}),
                                                                    dbc.CardBody(html.Iframe(id = 'benefits', style = {'border-width': '0', 'width': '100%', 'height': '400px'}))], style={"width": "21rem"}))]),
                                                    html.Br(),
                                           dbc.Row([dbc.Col(dbc.Card([dbc.CardHeader('Does Your Mental Illness Interfere With Work',style={'fontWeight': 'bold'}),
                                                                    dbc.CardBody(html.Iframe(id = 'interfere', style = {'border-width': '0', 'width': '100%', 'height': '400px'}))], style={"width": "32rem"})),
                                                    dbc.Col(dbc.Card([dbc.CardHeader('Do You Talk to Your Supervisors?', style={'fontWeight': 'bold'}),
                                                                    dbc.CardBody(html.Iframe(id = 'supervisor', style ={'border-width': '0', 'width': '100%', 'height': '400px'}))]))])], style = CONTENT_STYLE )])]))



app.layout = html.Div([overall])



@app.callback(
    Output('state_bar', 'srcDoc'),
    Input('state_wid', 'value'),
)

# plot the Country Frequency Bar Chart
def plot_state_bar(states):
    click = alt.selection_multi(fields=['state'], bind='legend')
    data = m_data[m_data['state'].isin(states)]
    chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('state', axis = None),
        y = alt.Y('count()', title='Count of Participants'), 
        tooltip = 'count()',
        color = 'state',
        column = alt.Column('treatment', title = 'Sought Treatment or Not', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom')),
        opacity = alt.condition(click, alt.value(0.9), alt.value(0.1))).add_selection(click).properties(width=100)
    return chart.to_html()


@app.callback(
    Output('fam_hist', 'srcDoc'),
    Input('state_wid', 'value'),
)

# Plot Family History Bar Chart
def plot_seriousness_bar(states):
    # filter data

    click = alt.selection_multi(fields=['state'], bind='legend')
    data = m_data[m_data['state'].isin(states)]
    chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('state', axis = None),
        y = alt.Y('count()', title='Count of Participants'), 
        tooltip = 'count()',
        color = 'state',
        column = alt.Column('mental_vs_physical', title = 'Does Employer Take Mental Illness Seriously', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom')),
        opacity = alt.condition(click, alt.value(0.9), alt.value(0.1))).add_selection(click).properties(width=100)
    return chart.to_html()




@app.callback(
    Output('sought_help', 'srcDoc'),
    Input('state_wid', 'value')
)

# Plot Sought Help Bar Chart
def plot_sought_help(states):
    click = alt.selection_multi(fields=['state'], bind='legend')
    data = m_data[m_data['state'].isin(states)]
    chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('state', axis = None),
        y = alt.Y('count()', title='Proportion of population'), 
        tooltip = 'count()', column = alt.Column('leave', title = 'Easy or Difficult', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom')),
        color = 'state', opacity = alt.condition(click, alt.value(0.9), alt.value(0.2))).add_selection(click).properties(width = 75)
    return chart.to_html()

@app.callback(
    Output('benefits', 'srcDoc'),
    Input('state_wid', 'value'),
)

# Plot Benefits Bar Chart
def plot_benefits(states):
    click = alt.selection_multi(fields=['state'], bind='legend')
    data = m_data[m_data['state'].isin(states)]
    chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('state', axis = None),
        y = alt.Y('count()', title='Proportion of population'), 
        tooltip = 'count()',
        color = 'state', column = alt.Column('benefits', title = 'Does Company Provide Benefits', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom')),
            opacity = alt.condition(click, alt.value(0.9), alt.value(0.2))).add_selection(click).properties(width=50)
    return chart.to_html()


@app.callback(
    Output('interfere', 'srcDoc'),
    Input('state_wid', 'value')
)

# Plot Benefits Bar Chart
def plot_interfere(states):
    click = alt.selection_multi(fields=['state'], bind='legend')
    data = m_data[m_data['state'].isin(states)]
    chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('state', axis = None),
        y = alt.Y('count()', title='Proportion of population'), 
        tooltip = 'count()',
        color = 'state', column = alt.Column('work_interfere', title = 'Does Your Mental Illness Interfere With Work?', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom')),
            opacity = alt.condition(click, alt.value(0.9), alt.value(0.2))).add_selection(click).properties(width=75)
    return chart.to_html()


@app.callback(
    Output('supervisor', 'srcDoc'),
    Input('state_wid', 'value')
)

def plot_supervisor(states):
    data = m_data[m_data['state'].isin(states)]
    chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('work_interfere', axis = None),
        y = alt.Y('count()', title='Proportion of population'), 
        tooltip = 'count()',
        color = 'work_interfere', column = alt.Column('supervisor', title = 'Have You Talked With Supervisor?', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom'))).properties(width=75)
    return chart.to_html()












if __name__ == '__main__':
    app.run_server(debug=True)