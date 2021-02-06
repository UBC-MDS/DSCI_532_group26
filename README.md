# An App to report Survey on Mental Health in the Tech Workplace

Contributors | Github | 
--- | --- |
Bruhat Musunuru| @bruhatM |
Siqi Zhou | @roycezhou  |
Chun Chieh(Jason) Chang| @jachang0628  | 

## Dashboard link
https://mental-health-dashboard-ubc.herokuapp.com

## About
Our app aims to present the statistics of people who worked in the tech sector and their views and intiatives taken on mental illness as well as workplace benefits regarding mental illness across different countries and time. We hope that by presenting these statistics, employers around the world can stop overlooking the issue of mental illness and create a less stress-inducing work environment.

## Description
This APP has a dashboard that summarizes the information given by the participants who took the mental health survey. In the right panel, there are multiple bar plots to represent *whether an individual seeks treatment for mental illness or not*, *whether the employer takes mental illness seriously*, *the easiness to leave work due to mental reason*, *the workplace benefits between states*, *whether an individual's mental illness interferes with work*, *how often that an individual talk to his/her supervisors*. Besides, the distributions are further separated by state and work interfere. 

In the left panel, the users can filter the states they are interested in. All filters will directly affect the 6 plots produced on the right. By choosing a state, the plot will only show the data that is restricted to that particular state. By selecting the gender, all 6 plots will only include the specific gender (male, female, all) with the corresponding mental health data. Hence, users can fix a certain gender that they are extremely interested in. Similarly, users can select the remote work button to filter data for all 6 plots as well. They can also choose to show or hide the columns of the plots by clicking on the corresponding legends. 

With these information, we hope to present the users on how many people sought treatments across states, how easy is it to leave work due to mental health issue, how does Work Benefits for mental health vary across states, do you feel comfortable talking with your supervisor regarding mental health issue, etc.

## Initial app sketch
![Alt text](updated_dashboard.jpg?raw=true "Title")

## Dashboard in action

## Usage

Access dashboard at https://mental-health-dashboard-ubc.herokuapp.com

### To build a local dashboard

**Step 1:**

Clone this repository to your local PC.

**Step 2:**

Create a conda environment using *environment.yaml* at the root of this project.

```bash
conda env create --file environment.yaml
```

**Step 3:**

Activate a conda environment by running the following command at the root directory of the project.

```bash
conda activate dash_env
```

**Step 4:**

Go to the root folder of the repo and execute `python src/app.py`.

## Reference

[Mental Health in Tech Survey dataset](https://www.kaggle.com/osmi/mental-health-in-tech-survey)
