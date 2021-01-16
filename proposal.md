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

- Which country has the highest possibility to encounter mental illness problem for living in 2014?

- Does female have a higher chance to face much working pressure leading to mental illnesses compared with a male?

- Do self-employed people work under much more pressure than others? 

- Does family history pose a threat to mental health?

## Usage scenarios 

Jack is deciding where to move for working as a software engineer.

Jack will relocate to North America or Europe and he wants to understand which country might provide a better work-life balance for him since IT workers usually undertake too much pressure. To work under a healthy mental environment is one of the most important indicators that he cares about. Hence he wants to be able to explore a dataset of mental illness records among different countries to give him a reference before moving. When Jack logs onto this App, he will see an overview of the distribution of the counts of mental illnesses across different countries such as USA, Canada, France, etc, indicating which country might have higher possibility to work under more pressure. Therefore, our dashboard can provide him with a sense of relocation. Jack can also filter for the certain countries that he has a strong interest in and understand more details in terms of one country. For instance, as we know that there are lots of states in the USA and each state might form a different distribution as well as the chance to encounter mental illnesses. If Jack is more concerned about what reasons causing a higher rate of mental illnesses, he can also utilize other filters of our App, such as the filter to differentiate whether the individuals work for a tech company or not, whether the companies those individuals work accept remote work or not, whether the family history leads to a mental health problem, etc. Jack can also filter for data in 2014 or any other available year according to the source data to see more recent and relevant mental illness statistics. Finally, Jack hypothesizes that country X provide his the best work-life balance to live in. Jack decides he needs to do further research on rental prices in this country to determine if he could afford to live there.

# Reference 

- [Mental Health in Tech Survey dataset](https://www.kaggle.com/osmi/mental-health-in-tech-survey)