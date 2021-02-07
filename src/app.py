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
import plotly.express as px

# load the data and transform date time column
m_data = pd.read_csv("data/processed/processed_survey.csv")
m_data['Age Range'] = pd.cut(m_data['Age'],bins=[10,20,30,40,50], labels=["10-20","21-30","31-40", "41+"])
sdate = m_data['Timestamp'].min()
edate = m_data['Timestamp'].max()
all_states = m_data['state'].unique()
some_states = all_states[:3]
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Tech Worker Mental Health Stats"
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

#static Graph
pie_home = px.pie((m_data.groupby('remote_work', as_index = False).size()), values='size', names='remote_work', width = 100)
pie_gender = px.pie((m_data.groupby('Gender', as_index = False).size()), values='size', names='Gender', width = 100)
pie_age = px.pie(m_data.groupby('Age Range', as_index = False).size(), values='size', names='Age Range')

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



# Columns
seek_treat = dbc.Col(dbc.Card([dbc.CardHeader('Did You Seek Treatment for Mental Illness', style={'fontWeight': 'bold'}),
                                dbc.CardBody(dcc.Loading(children = html.Iframe(
                                    id = 'state_bar', style={'border-width': '0', 'width': '100%', 'height': '400px'}) ))])) #


seriousness = dbc.Col(dbc.Card([dbc.CardHeader('Does Employer Take Mental Illness Seriously', style={'fontWeight': 'bold'} ),
                              dbc.CardBody(dcc.Loading(children = html.Iframe(
                                  id = 'serious', style={'border-width': '0', 'width': '150%', 'height': '400px'})))]
                                   ))

workplace_bene = dbc.Col(dbc.Card([dbc.CardHeader('Workplace Benefits Between States', style={'fontWeight': 'bold'}),
dbc.CardBody(dcc.Loading(children = html.Iframe(id = 'benefits', style = {'border-width': '0', 'width': '100%', 'height': '400px'})))])) #

leave = dbc.Col(dbc.Card([dbc.CardHeader('Easiness to Leave Work Due to Mental Reason', style={'fontWeight': 'bold'}),
                        dbc.CardBody(dcc.Loading(
                            children = html.Iframe(
                            id = 'leave_work', style = {'border-width': '0', 'width': '100%', 'height': '400px'})))]))

work_in = dbc.Col(dbc.Card([dbc.CardHeader('Does Your Mental Illness Interfere With Work',style={'fontWeight': 'bold'}),
                         dbc.CardBody(dcc.Loading(children = html.Iframe(
                             id = 'interfere', style = {'border-width': '0', 'width': '100%', 'height': '400px'})))]))

supervisor = dbc.Col(dbc.Card([dbc.CardHeader('Did You Talk to Your Supervisors Regarding Mental Health?', style={'fontWeight': 'bold'}),
                        dbc.CardBody(dcc.Loading(children = html.Iframe(
                            id = 'supervisor', style ={'border-width': '0', 'width': '100%', 'height': '400px'}) ))])) #

pie_remote = dbc.Col(dbc.Card([dbc.CardHeader('Do You Work At Home?', style={'fontWeight': 'bold'}),
                        dbc.CardBody(dcc.Loading(children = dcc.Graph(
                            id = 'pie_chart', figure = pie_home, style ={'border-width': '0', 'width': '100%', 'height': '400px'}) ))])) #

pie_gender = dbc.Col(dbc.Card([dbc.CardHeader('Gender Proportion', style={'fontWeight': 'bold'}),
                        dbc.CardBody(dcc.Loading(children = dcc.Graph(
                            id = 'pie_Gender', figure = pie_gender, style ={'border-width': '0', 'width': '100%', 'height': '400px'}) ))]))

pie_age = dbc.Col(dbc.Card([dbc.CardHeader("Participant's Age Range", style={'fontWeight': 'bold'}),
                        dbc.CardBody(dcc.Loading(children = dcc.Graph(
                            id = 'pie_age', figure = pie_age, style ={'border-width': '0', 'width': '100%', 'height': '400px'})))]))  #








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
                                  dbc.Col([dbc.Tabs([dbc.Tab([dbc.Row([work_in, supervisor], justify= 'start', no_gutters= True),dbc.Row([seek_treat], justify= 'center')], label = 'Mental Illness History'),
                                                     dbc.Tab([dbc.Row([workplace_bene, seriousness], no_gutters = True),dbc.Row([leave])] , label = 'Company Culture'),
                                                     dbc.Tab([dbc.Row([pie_remote, pie_gender], no_gutters = True), dbc.Row([pie_age])], label = "Total Participants' Demography"),
                                                     dbc.Tab([html.Br(), html.P("""Hello! Thank you for visiting our App! This App is developed by Chun Chieh(Jason) Chang, Bruhat Musunuru, and Siqi Zhou.
                                                                        Our app aims to present the statistics of people who worked in the tech sector and their mental illness history versus employers' attitudes towards mental illness across different states in the USA.
                                                                       We hope that by presenting these statistics, employers around the world can stop overlooking the issue of mental illness and create a less stress-inducing work environment."""),
                                                                       html.Br(),
                                                                       html.P(
                                                                       """The data source can be found at https://www.kaggle.com/osmi/mental-health-in-tech-survey
                                                                        and the link to our github is https://github.com/UBC-MDS/DSCI_532_group26 """)], label = 'About This Dashboard')])])])], fluid = True))





app.layout = html.Div([overall])


#plotting function
@app.callback(
    Output('state_bar', 'srcDoc'),
    Input('state_wid', 'value'),
    Input('gender_radio', 'value'),
    Input('remote_work', 'value')
)

# plot the State Frequency Bar Chart
def plot_state_bar(states, gender, remote):
    """Plot the Country Frequency Bar Chart
    
    Use mental health csv file to plot the state frequency bar chart for seeking treatment, grouped by
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
        color = alt.Color('state', title = 'State'),
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

# Plot the Employer Attitude plot
def plot_seriousness_bar(states, gender, remote):
    """Plot the Employer Attitude plot
    
    Use mental health csv file to plot the employer attitude bar chart 
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
        the employer attitude bar chart 

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
        color = alt.Color('state', title = 'State'),
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
        color = alt.Color('state', title = 'State'), opacity = alt.condition(click, alt.value(0.9), alt.value(0.2))).add_selection(click).properties(width = 100)
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
        color = alt.Color('state', title = 'State'), column = alt.Column('benefits', title = 'Does Company Provide Benefits', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom')),
            opacity = alt.condition(click, alt.value(0.9), alt.value(0.2))).add_selection(click).properties(width=85)
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
        color = alt.Color('state', title = 'State'), column = alt.Column('work_interfere', title = 'Does Your Mental Illness Interfere With Work?', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom')),
            opacity = alt.condition(click, alt.value(0.9), alt.value(0.2))).add_selection(click).properties(width=65)
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
        x = alt.X('state', axis = None),
        y = alt.Y('count()', title='Count of Participants'), 
        tooltip = 'count()',
        color = alt.Color('state', title = 'State'), column = alt.Column('supervisor', title = 'Have You Talked With Supervisor?', header=alt.Header(
            titleOrient = 'bottom', labelOrient = 'bottom'))).properties(width=75)
    return chart.to_html()





  













if __name__ == '__main__':
    app.run_server()