Proposal of an App to report Survey on Mental Health in the Tech Workplace in 2014
================

* Authors: Jason Chang, Siqi Zhou, Bruhat Musunuru 

-   [Section 1: Motivation and
    Purpose](#section-1-motivation-and-purpose)
-   [Section 2: Description of the
    data](#section-2-description-of-the-data)
-   [Section 3: Research questions and usage scenarios](#section-3-research-questions-and-usage-scenarios)
-   [Reference](#reference)
# Section 1: Motivation and Purpose
Who we are: Non-Profit Mental Health Organization

Target Audience: Employers in the technology sector around the world

With the overabundance of information and stress in our modern society, more and more people are affected by some kind of mental illness. These mental illness include anxiety, depression, bipolar disorder, and personality disorder etc. One of the many contributors to developing a mental illness is the stress faced in the workplace. Out of all different industry, one can argue that working in the technology industry would be the most stress-inducing. With our fast-changing technology in modern society, employers in the tech industry often force their employees to work unreasonable hours or develop new technology in a short amount of time without considering their employee's mental state. Hence, the poor working environment can often become the number one contributor to developing mental illness. This is particularly true in most Asian countries where the employers will often demand overtime from their workers. Thus, our app aims to present the statistics of people who worked in the tech sector and the frequency of mental illness among these people across different demographics and work cultures. We hope that by presenting these statistics, employers around the world can stop overlooking this issue and create a less stress-inducing workplace.




# Section 2: Description of the data

This app will visualize the dataset that contains information on approximately 1200 individuals who work in the tech industry around the world. In the dataset, each row represents an individual and has information regarding their demographics, workplace environment, and their initiatives in dealing with mental illness. Whether the person has a mental illness is indicated by the `treatment` column. In our app, we will investigate the distribution of the counts of mental illnesses across different countries as well as other demographics among these individuals. Another interesting aspect that is worth investigating is whether these individuals who are afflicted by mental illnesses have a family history since the illness could be possibly passed down from the parents. Next, we will explore the relationship between mental illness and attributes of the workplace environment. Finally, we want to see whether these individuals sought any help regarding their illnesses. In terms of demographic information, we will be using the columns `Age`, `Country`, `Gender`, and `family history` etc. Columns that describe workplace environment include `no_employees`, `remote_work`, `benefits`, `care_options`, `mentalhealthconsequence` and `mentalvsphysical` etc. Finally, we will use the `sought help` column to investigate whether employers sought any help.

# Section 3: Research questions and usage scenarios

## Research questions

Some research questions that could be answered by this dashboard are:

- Given the date, which country has the most survey participants regarding mental illness problem and did they seek any help?

- Based on the country(countries) and year, what is the proportion of participants whose families have history of mental illness. In addition, is there a difference in this proportion given gender.

- Based on the country(countries) and year, what is the proportion of participants who sought help. In addition, is there a difference in this proportion given gender.

- Based on the country(countries) and year, do companies provide workplace benefits to help combat mental illness. In addition, is there a difference in this distribution given gender.

## Usage scenarios 

Jack is working as a software engineer and recently received a promotion. In addition, Jack has the ability to choose which country to relocate before starting his new position. Despite this great news, Jack is also a person who is affected by severe mental illness. In addition, Jack's wife also works in the tech industry and is willing to move with Jack as well.

This APP has a dashboard that summarizes the information given by the participants who took the mental health survey. The right panel includes 4 plots that describes the relationships between location, family history, workplace benefits, gender, and whether an individual sought help. Jack can utilize the filters in the left panel to filter for the countries that he wants to relocate to. Given the selected countries, the distributions of the plots will change accordingly. In addition, Jack can also filter the data given dates to see whether there are changes in distributions among the above relationships over time.

In the right panel, there are 4 bar plots to represent the proportion of participants based on country, family history of mental illness, workplace benefits, and whether the individual sought any help. In addition, the distributions of family history, sought help, and workplace benefits are further separated by gender. From the plots, Jack can obtain an understanding on which country has the highest mental survey participation. Next, given the countries selected, Jack will be able to see the distribution of family history of mental illness in the tech industry. Third, Jacky will be able to see whether the participants sought any help and decipher which country has very stressful work environment in the tech industry. Finally, using the fourth plot, Jack will be able to see which countries' tech industry provides more benefits to help battle mental health.  With these information, Jack can decide the best country to move to that accounts for his mental illness and start a new life with his wife.

# Reference 

- [Mental Health in Tech Survey dataset](https://www.kaggle.com/osmi/mental-health-in-tech-survey)