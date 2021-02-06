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
    "margin-left": "6rem"
}

seek_treat = dbc.Col(dbc.Card([dbc.CardHeader('Did You Seek Treatment for Mental Illness', style={'fontWeight': 'bold'}),
                                dbc.CardBody(dcc.Loading(children = html.Iframe(
                                    id = 'state_bar', style={'border-width': '0', 'width': '150%', 'height': '400px'}) ))]), style={"width": "100%", "height": "100%"})


seriousness = dbc.Col(dbc.Card([dbc.CardHeader('Does Employer Take Mental Illness Seriously', style={'fontWeight': 'bold'} ),
                              dbc.CardBody(dcc.Loading(children = html.Iframe(
                                  id = 'serious', style={'border-width': '0', 'width': '150%', 'height': '400px'})))],
                                   style={"width": "30rem"}),  style={"width": "100%", "height": "100%"})

workplace_bene = dbc.Col(dbc.Card([dbc.CardHeader('Workplace Benefits Between States', style={'fontWeight': 'bold'}),
dbc.CardBody(dcc.Loading(children = html.Iframe(id = 'benefits', style = {'border-width': '0', 'width': '100%', 'height': '400px'})))]))

leave = dbc.Col(dbc.Card([dbc.CardHeader('Easiness to Leave Work Due to Mental Reason', style={'fontWeight': 'bold'}),
                        dbc.CardBody(dcc.Loading(
                            children = html.Iframe(
                            id = 'leave_work', style = {'border-width': '0', 'width': '100%', 'height': '400px'}) ))])
                            , style={"width": "150%", "height": "100%"})

work_in = dbc.Col(dbc.Card([dbc.CardHeader('Does Your Mental Illness Interfere With Work',style={'fontWeight': 'bold'}),
                         dbc.CardBody(dcc.Loading(children = html.Iframe(
                             id = 'interfere', style = {'border-width': '0', 'width': '100%', 'height': '400px'})))], style={"width": "32rem"}))

supervisor = dbc.Col(dbc.Card([dbc.CardHeader('Do You Talk to Your Supervisors?', style={'fontWeight': 'bold'}),
                        dbc.CardBody(dcc.Loading(children = html.Iframe(
                            id = 'supervisor', style ={'border-width': '0', 'width': '100%', 'height': '400px'}) ))]))




# Organize Charts into Grid Style
#content = dbc.Container([dbc.Row([dbc.Col([html.Iframe(id = 'state_bar', style={'border-width': '0', 'width': '100%', 'height': '400px'})]),
 #                      dbc.Col([html.Iframe(id = 'fam_hist', style={'border-width': '0', 'width': '150%', 'height': '450px'})])]),
  #                  dbc.Row([dbc.Col([html.Iframe(id = 'sought_help', style={'border-width': '0', 'width': '150%', 'height': '450px'})]),
   #                    dbc.Col([html.Iframe(id = 'benefits', style={'border-width': '0', 'width': '150%', 'height': '450px'})])]),
    #                dbc.Row([dbc.Col([html.Iframe(id = 'interfere', style={'border-width': '0', 'width': '150%', 'height': '450px'})]),
     #                        dbc.Col([html.Iframe(id = 'supervisor', style={'border-width': '0', 'width': '150%', 'height': '450px'})])])])

overall = html.Div(dbc.Container([dbc.Row([dbc.Col([html.H3("Tech Worker Mental Health Tracker"), html.Hr(),
                                                    html.P("Filter By: ", className="lead"),
                                                    html.Br(),
                                                    html.Label(['States:', dcc.Dropdown(id = 'state_wid', value = some_states,
                                 options=[{'label': st, 'value': st } for st in all_states], multi = True, style = {'color': 'black'})]),
                                                    html.Br(),
                                                    html.Br(),
                                                    html.Label(['Gender:', dbc.RadioItems(id = 'gender_radio',
                                                                                           options = [{'label': 'All', 'value':['F','M']},
                                                                                                      {'label': 'Male', 'value': ['M']},
                                                                                                      {'label': 'Female', 'value': ['F']}
                                                                                                     ],  value = ['F','M'])]),
                                                    html.Br(),
                                                    html.Br(),
                                                    html.Label(['Remote Work:', dbc.RadioItems(id = 'remote_work',
                                                                                              options = [{'label': 'All', 'value':['Yes','No']},
                                                                                                      {'label': 'Yes', 'value': ['Yes']},
                                                                                                      {'label': 'No', 'value': ['No']}],
                                                                                                       value = ['Yes', 'No'])])],
                                  style={'background-color': '#15599e',
                                         "color": "white",
                                         }, md = 2),
                                  dbc.Col([dbc.Tabs([dbc.Tab([dbc.Row([seek_treat, seriousness]),dbc.Row([leave])], label = 'tab1'),
                                                     dbc.Tab([dbc.Row([workplace_bene, supervisor]),dbc.Row([work_in])] , label = 'tab2')])])])], fluid = True))


#dbc.Row([seek_treat, seriousness]),
#                                                   html.Br(),
 #                                          dbc.Row([]),
  #                                                  html.Br(),
   #                                        dbc.Row([])





app.layout = html.Div([overall])



@app.callback(
    Output('state_bar', 'srcDoc'),
    Input('state_wid', 'value'),
    Input('gender_radio', 'value'),
    Input('remote_work', 'value')
)

# plot the Country Frequency Bar Chart
def plot_state_bar(states, gender, remote):
    """Plot the Country Frequency Bar Chart
    
    Use mental health csv file to plot the country frequency bar chart 
    by state, gender and remote work status.

    Parameters
    ----------
    states : string
        the abbreviation of the USA states
    gender : string
        male or female
    remote : string
        the remote work status of an employee, yes or no

    Returns
    -------
    chart
        the country frequency bar chart

    """
    click = alt.selection_multi(fields=['state'], bind='legend')
    data = m_data[m_data['state'].isin(states)]
    data = data[data['Gender'].isin(gender)]
    data = data[data['remote_work'].isin(remote)]
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
    Output('serious', 'srcDoc'),
    Input('state_wid', 'value'),
    Input('gender_radio', 'value'),
    Input('remote_work', 'value')
)

# Plot the Family History Bar Chart
def plot_seriousness_bar(states, gender, remote):
    """Plot the Family History Bar Chart
    
    Use mental health csv file to plot the family history bar chart 
    by state, gender and remote work status.

    Parameters
    ----------
    states : string
        the abbreviation of the USA states
    gender : string
        male or female
    remote : string
        the remote work status of an employee, yes or no

    Returns
    -------
    chart
        the family history bar chart 

    """

    # filter data
    click = alt.selection_multi(fields=['state'], bind='legend')
    data = m_data[m_data['state'].isin(states)]
    data = data[data['Gender'].isin(gender)]
    data = data[data['remote_work'].isin(remote)]
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
    Output('leave_work', 'srcDoc'),
    Input('state_wid', 'value'),
    Input('gender_radio', 'value'),
    Input('remote_work', 'value')
)

# Plot the Sought Help Bar Chart
def plot_sought_help(states, gender, remote):
    """Plot the Sought Help Bar Chart
    
    Use mental health csv file to plot the sought help bar chart 
    by state, gender and remote work status.

    Parameters
    ----------
    states : string
        the abbreviation of the USA states
    gender : string
        male or female
    remote : string
        the remote work status of an employee, yes or no

    Returns
    -------
    chart
        the sought help bar chart 

    """
    click = alt.selection_multi(fields=['state'], bind='legend')
    data = m_data[m_data['state'].isin(states)]
    data = data[data['Gender'].isin(gender)]
    data = data[data['remote_work'].isin(remote)]
    chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('state', axis = None),
        y = alt.Y('count()', title='Count of Participants'), 
        tooltip = 'count()', column = alt.Column('leave', title = 'Easy or Difficult', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom')),
        color = 'state', opacity = alt.condition(click, alt.value(0.9), alt.value(0.2))).add_selection(click).properties(width = 70)
    return chart.to_html()

@app.callback(
    Output('benefits', 'srcDoc'),
    Input('state_wid', 'value'),
    Input('gender_radio', 'value'),
    Input('remote_work', 'value')
)

# Plot the Benefits Bar Chart
def plot_benefits(states, gender, remote):
    """Plot the Benefits Bar Chart
    
    Use mental health csv file to plot the benefits bar chart 
    by state, gender and remote work status.

    Parameters
    ----------
    states : string
        the abbreviation of the USA states
    gender : string
        male or female
    remote : string
        the remote work status of an employee, yes or no

    Returns
    -------
    chart
        the benefits bar chart 

    """
    click = alt.selection_multi(fields=['state'], bind='legend')
    data = m_data[m_data['state'].isin(states)]
    data = data[data['Gender'].isin(gender)]
    data = data[data['remote_work'].isin(remote)]
    chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('state', axis = None),
        y = alt.Y('count()', title='Count of Participants'), 
        tooltip = 'count()',
        color = 'state', column = alt.Column('benefits', title = 'Does Company Provide Benefits', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom')),
            opacity = alt.condition(click, alt.value(0.9), alt.value(0.2))).add_selection(click).properties(width=50)
    return chart.to_html()


@app.callback(
    Output('interfere', 'srcDoc'),
    Input('state_wid', 'value'),
    Input('gender_radio', 'value'),
    Input('remote_work', 'value')
)

# Plot the Work Interfere Bar Chart
def plot_interfere(states, gender, remote):
    """Plot the Work Interfere Bar Chart
    
    Use mental health csv file to plot the work interfere bar chart 
    by state, gender and remote work status.

    Parameters
    ----------
    states : string
        the abbreviation of the USA states
    gender : string
        male or female
    remote : string
        the remote work status of an employee, yes or no

    Returns
    -------
    chart
        the work interfere bar chart 

    """
    click = alt.selection_multi(fields=['state'], bind='legend')
    data = m_data[m_data['state'].isin(states)]
    data = data[data['Gender'].isin(gender)]
    data = data[data['remote_work'].isin(remote)]
    chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('state', axis = None),
        y = alt.Y('count()', title='Count of Participants'), 
        tooltip = 'count()',
        color = 'state', column = alt.Column('work_interfere', title = 'Does Your Mental Illness Interfere With Work?', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom')),
            opacity = alt.condition(click, alt.value(0.9), alt.value(0.2))).add_selection(click).properties(width=75)
    return chart.to_html()


@app.callback(
    Output('supervisor', 'srcDoc'),
    Input('state_wid', 'value'),
    Input('gender_radio', 'value'),
    Input('remote_work', 'value')
)

# Plot the Supervisor Bar Chart
def plot_supervisor(states, gender, remote):
    """Plot the Supervisor Bar Chart
    
    Use mental health csv file to plot the supervisor bar chart 
    by state, gender and remote work status.

    Parameters
    ----------
    states : string
        the abbreviation of the USA states
    gender : string
        male or female
    remote : string
        the remote work status of an employee, yes or no

    Returns
    -------
    chart
        the supervisor bar chart 

    """
    data = m_data[m_data['state'].isin(states)]
    data = data[data['Gender'].isin(gender)]
    data = data[data['remote_work'].isin(remote)]
    chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('work_interfere', axis = None),
        y = alt.Y('count()', title='Count of Participants'), 
        tooltip = 'count()',
        color = 'work_interfere', column = alt.Column('supervisor', title = 'Have You Talked With Supervisor?', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom'))).properties(width=75)
    return chart.to_html()












if __name__ == '__main__':
    app.run_server(debug=True)