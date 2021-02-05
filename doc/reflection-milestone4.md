# Reflection

## Implementation of the dashboard with feedback from TA and peers:

By developing from the feedback received from peers and TA, our team has completed a dashboard including 6 plots corresponding to *whether an individual seeks treatment for mental illness or not*, *whether the employer takes mental illness seriously*, *the easiness to leave work due to mental reason*, *the workplace benefits between states*, *whether an individual's mental illness interferes with work*, *how often that an individual talk to his/her supervisors*. The dashboard has reached all the functionalities we proposed and addressed all the feedback from TA and peers.

In terms of the information that our dashboard provides, we increased the bar plots from *4* to *6* to fit better with our proposal, aimed to provide more meaningful mental health survey results within a limited space. We have implemented bar plots using *work_interfere* variable according to TA's feedback, as this variable does add some helpful information for dashboard users. Our team re-explored the raw data to digest more meaningful variables hence we replace them from gender to the corresponding legends, for instance, to add states such as IL, TN and TX, and to add work_interfere such as never, often, rarely, etc. Besides, we replaced the percentage of the survey participants as the count number as Y-axis since it is more straightforward. From milestone 3, we realized the majority of the participants is coming from the USA, weighted more than 60%, which might be ambiguous for users who are interested in further information if only providing the whole USA data. To finalize this dashboard, we break the USA as states to provide more details of mental health illness. More revisions can be found from our dashboard link under README. 

In terms of the features developed by dash, we removed the selection of the calendar in the left panel since our raw data is not huge and most of the survey results are done in 2014. Moving forward, we added two types of choice selection button, gender (male and female) and remote work (yes or no). As for the location dropdown feature, we replaced the country filter as a state filter to illustrate USA data with more details.

## Feature introduction:

In the left panel, the users can filter the states they are interested in. All filters will directly affect the 6 plots produced on the right. By choosing a state, the plot will only show the data that is restricted to that particular state. By selecting the gender, all 6 plots will only include the specific gender (male, female, all) with the corresponding mental health data. Hence, users can fix a certain gender that they are extremely interested in. Similarly, users can select the remote work button to filter data for all 6 plots as well. They can also choose to show or hide the columns of the plots by clicking on the corresponding legends.

## Issues encountered and fixed:

- One of the big hurdles we encountered early on was with the rendering of the dashboard. The dashboard rendered aesthetically as expected on Apple devices but failed on other operating systems. After rigorous debugging, we concluded that it was an issue with wrapping the content with dbcContainer.

- One group member noticed that on a big screen, there will be a lot of space between the plots and the widgets on the left. We have fixed it by changing dash layout settings.

## Improvements and additions for the dashboard:

- After re-understanding the raw data, our team found the field work_interfere hints us whether an individual has a mental illness or not. work_interfere includes levels, 'Often', 'Rarely', 'Never', 'Sometimes', and nan. By adding work_interfere in the processed data, our dashboard now can reveal useful information such as which state might have the highest possibility to encounter mental illness problem or stress for living in 2014 and do female have a higher chance to face much working pressure leading to mental illnesses compared with a male, etc.

- We have improved the user experience of the dashboard to make it easy to be used, and we used more meaningful colour to interpret the processed data in the dashboard, as blue, red, and orange are all sensitive for human's eyes.

- From our analysis, the USA has a considerable amount of examples in the dataset. Our team has further breakdown our plots by the state in the USA to gain useful insights.

- We fixed the large white space between plots and widgets when viewing with a big screen.

- There are some insights that we have found particularly valuable during our final dashboard development. For instance, both TA and peers feedback that the proportion of the population is referring to a confusing axis title and counts would be better. Hence we re-wrote the data processing code and have implemented counts as Y-axis, labelled as count of participants.

