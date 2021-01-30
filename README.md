# An App to report Survey on Mental Health in the Tech Workplace in 2014 

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
This APP has a dashboard that summarizes the information given by the participants who took the mental health survey. In the right panel, there are 4 bar plots to represent the proportion of participants based on country, family history of mental illness, workplace benefits, and whether the individual sought any help. In addition, the distributions of family history, sought help, and workplace benefits are further separated by gender. On the left panel, the user can utilize the filters to filter for the countries that he or she is interested in. Given the selected countries, the distributions of the plots will change accordingly. In addition, the user can also filter the data given dates to see whether there are changes in distributions among the above relationships over time. With these information, we hope to present the users on which country has the highest rate of mental illness in the tech industry as well as whether the employers take this issue seriously. In addition, the user can also see whether the tech industries' view on mental illness as well as the rate of mental illness changed over time given the selected countries.

![Alt text](updated_dashboard.jpg?raw=true "Title")

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
