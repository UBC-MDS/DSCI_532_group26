# An App to report Survey on Mental Health in the Tech Workplace in 2014 

Contributors | Github | 
--- | --- |
Bruhat Musunuru| @bruhatM |
Siqi Zhou | @roycezhou  |
Chun Chieh(Jason) Chang| @jachang0628  | 

## Dashboard link
https://mental-health-dashboard-ubc.herokuapp.com

## About
Our app aims to present the statistics of people who worked in the tech sector and the frequency of mental illness among these people across different demographics and work cultures. We hope that by presenting these statistics, employers around the world can stop overlooking this issue and create a less stress-inducing workplace.

## Description
This is the landing page for our app that shows the distribution of data set factors that affect an employee in the tech sector's mental health and mental illnesses. From the menu on the left, the user can filter the appropriate factors that affect mental health by year or by category. From the distribution display, the user can get information about the proportion of workers with illnesses by demographics, the influence an employee's family history has on their mental illnesses, the influence workplace mental health benefits have on the employee's mental health and finally whether the employee sought help for their illness or not. The user can also further analyze the distribution display the role gender has on an employee's mental health which can further be filtered by the options mentioned above.

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
