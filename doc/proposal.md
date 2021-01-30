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

This app will visualize the dataset that contains information on approximately 1200 individuals who work in the tech industry around the world. In the dataset, each row represents an individual and has information regarding their demographics, workplace environment, and their initiatives in dealing with mental illness. Whether the person has a mental illness is indicated by the `treatment` column. In our app, we will investigate the distribution of the counts of mental illnesses across different countries as well as other demographics among these individuals. Another interesting aspect that is worth investigating is whether these individuals who are afflicted by mental illnesses have a family history since the illness could be possibly passed down from the parents. Next, we will explore the relationship between mental illness and attributes of the workplace environment. Finally, we want to see whether these individuals sought any help regarding their illnesses. In terms of demographic information, we will be using the columns `Age`, `Country`, `Gender`, and `family history` etc. Columns that describe workplace environment include `no_employees`, `remote_work`, `benefits`, `care_options`, `mentalhealthconsequence` and `mentalvsphysical` etc. Finally, we will use columns such as `coworkers`, `supervisor`, and `mentalhealthinterview` etc to investigate whether employers sought any help.

# Section 3: Research questions and usage scenarios

## Research questions

Some research questions that could be answered by this dashboard are:

- Which country has the most survey participants regarding mental illness problem in 2014?

- What is the percentage that an individual sought for help by geographic location in 2014?

- How many survey participants have a family history of mental illness problem?

- What is the percentage that a survey participant's company provides workplace benefits?

## Usage scenarios 

Jack is working as a software engineer and he has a strong interest in mental health and frequency of mental health disorders in the tech workplace.

This APP has completed a dashboard including 4 plots corresponding to the relationship among location, family history, workplace benefits, gender, whether an individual sought help. Jack can utilize the buttons from the menu on the left panel, he can filter the appropriate factors that affect mental health by year or by geographic location. The location filter affects the first bar plot in the top left and Jack can choose the countries that he wants to see. For example, Jack can filter the USA, Canada, the UK, France, etc. By changing the date, all the 4 plots will only include the corresponding input date range. Hence, Jack can fix a certain period that they are extremely interested in. Jack can also filter the plots for a particular gender by clicking on the corresponding gender on the legend.

In the right panel, there are 4 bar plots to represent the proportion of the population based on country, family history, workplace benefits, whether an individual sought help, separately. All the plots are divided by gender using facets as well. From the distribution display on the right-hand side, he can get information about the percentage of all the survey participants with illnesses by demographics, the influence an employee's family history has on their mental illnesses, the influence workplace mental health benefits have on the employee's mental health and finally whether the employee sought help for their illness or not. Jack can also further analyze the distribution display the role gender has on an employee's mental health which can further be filtered by the options mentioned above.

# Reference 

- [Mental Health in Tech Survey dataset](https://www.kaggle.com/osmi/mental-health-in-tech-survey)