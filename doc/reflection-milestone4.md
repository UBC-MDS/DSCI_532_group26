# Reflection

## Implementation of the dashboard with feedback from TA and peers:

Using the feedbacks received from peers and TA, our team has completed a dashboard that has 9 plots and they correspond to *whether an individual seeks treatment for mental illness or not*, *whether the employer takes mental illness seriously*, *the easiness to leave work due to mental reason*, *the workplace benefits between states*, *whether an individual's mental illness interferes with work*, *how often that an individual talk to his/her supervisors*, *Remote work proportion*, *Gender Distribution*, and *Age Distribution*. The dashboard has achieved all the functionalities that we have proposed and addressed most of the feedbacks from TA and peers.

In terms of the information that our dashboard provides, we increased the bar plots from *4* to *6* to answer our research questions. To save space, we created 3 additional tabs and distributed our plots evenly among these tabs. After speaking with the TA and reviewing the feedbacks, we decided to re-investigate our data and redesigned our research questions. The new research question can be found in the proposal document. On the other hand, we replaced the percentage of the survey participants from previous plots and decided to use count instead so that it will be less confusing for the user to understand. To address our peer's feedback regarding country, we realized the majority of the participants are coming from the USA. Hence, we decided to solely concentrate our analysis on the participants in the USA and use state instead of country.

In terms of the new features developed, we removed the selection of dates in the left panel since most of the data are from 2014. We replaced the data selector with two additional filters Gender and Remote Work and they work the same as State.



## Issues encountered and fixed:

- One of the big hurdles we encountered early on was with the rendering of the dashboard. The dashboard rendered aesthetically as expected on Apple devices but failed on other operating systems. After rigorous debugging, we concluded that it was an issue with wrapping the content with dbcContainer.

- One group member noticed that people with different monitor sizes will see different layouts. For example, people with smaller screens will not be able to see the full graph because the screen won't fit. To accommodate this, we used tabs to evenly distribute our plots and the issue has been resolved.

## Additional Reflection:

- The dashboard is very easy and straightforward to use. We did not include sophisticated widgets and kept everything as simple as possible so that our user won't be overwhelmed. In addition, the load time for our app is fast as well so the users won't be twiddling their thumbs waiting for the app to respond. In terms of reoccurring feedbacks, both the TA and our peer wanted to see a trend line given our data. However, after investigating the data, we realized that it will not be ideal to include a trend line given that most of the participants responded in the year 2014. After doing some research, we found out the organization that provided the data does have additional data that spanned from 2015 to 2020. However, we would need to download each of them and merge them into our dataset, which unfortunately we do not have time for. Overall, it has been a fun ride and we really enjoyed having the ability to give life to our data and share our findings to more people.