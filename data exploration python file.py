#!/usr/bin/env python
# coding: utf-8

# DATA VISUALISATION
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mlt
import seaborn as sns
from matplotlib import pylab
import plotly.express as px


# READING OF DATA AS CSV [START]

# In[2]:


VenueSpend = pd.read_csv(r"C:\Users\pc\Desktop\001186932\VenueSpend.csv")


# In[3]:


VenueAge = pd.read_csv(r"C:\Users\pc\Desktop\001186932\VenueAge.csv")


# In[4]:


VenueDistance = pd.read_csv(r"C:\Users\pc\Desktop\001186932\VenueDistance.csv")


# In[5]:


VenueDuration = pd.read_csv(r"C:\Users\pc\Desktop\001186932\VenueDuration.csv")


# In[6]:


VenueGender = pd.read_csv(r"C:\Users\pc\Desktop\001186932\VenueGender.csv")


# In the data "VenueDailyVisitors" below, "parse_dates" has been used to convert "Date" column to DateTimeIndex format

# In[7]:


VenueDailyVisitors = pd.read_csv(r"C:\Users\pc\Desktop\001186932\VenueDailyVisitors.csv", parse_dates=True , index_col="Date" )


# READING OF DATA AS CSV [END]

# THE FIRST FEW DATA POINTS IN "VenueDailyVisitor"

# In[8]:


VenueDailyVisitors.head() #This shows that some branches did not open at the start of the year


# LAST FEW DATAPOINTS IN "VenueDailyVisitor"

# In[9]:


VenueDailyVisitors.tail() #This shows that some branches closed down before the end of the year


# In[10]:


VenueDailyVisitors.describe()


# In[11]:


VenueDailyVisitors.shape


# In[12]:


VenueDailyVisitors.columns #To show all branches


# PLOT OF DAILY VISIT OF EACH VENUE TO DATE [START]

# In[13]:


VenueDailyVisitors.plot(subplots=True , figsize = (20, 25)) #To show the branches that didnot open at the start of the year 
# and the branches that closed down before the year ends


# PLOT OF DAILY VISIT OF EACH VENUE TO DATE [END]

# SHOWING THE COUNT OF ZEROS(DAYS EACH VENUE DID NOT OPEN) , CALCULATING THE DAYS EACH BRANCH OPEN AND THEN CALCULATING EXPECTED TOTALYEARLYVISIT  [START]

# In[14]:


VenueDailyVisitors['ZJB'].value_counts()


# In[15]:


#FROM THE ABOVE , 'ZJB' OPENED FOR 171 DAYS 
VenueDailyVisitors['ZJB'].sum()


# TOTALVISIT for ZJB IS 17247 
# AVERAGE VISIT IS 17247/171 = 100.85 APPROX. 101 VISIT PER DAY
# SO , EXPECTED TOTALYEARLYVISIT IS 101*365 = 36,865

# In[16]:


VenueDailyVisitors['BKI'].value_counts()


# In[17]:


#FROM THE ABOVE , 'BKI' OPENED FOR 156 DAYS 
VenueDailyVisitors['BKI'].sum()


# TOTALVISIT for BKI IS 9909 
# AVERAGE VISIT IS 9909/156 = 63.5 APPROX. 64 VISIT PER DAY
# SO , EXPECTED TOTALYEARLYVISIT IS 64*365 = 23360

# In[18]:


VenueDailyVisitors['YDI'].value_counts()


# In[19]:


#FROM THE ABOVE , 'YDI' OPENED FOR 164 DAYS 
VenueDailyVisitors['YDI'].sum()


# TOTALVISIT for YDI IS 7217 
# AVERAGE VISIT IS 9909/164 = 60.4 APPROX. 60 VISIT PER DAY
# SO , EXPECTED TOTALYEARLYVISIT IS 60*365 = 21900

# In[20]:


VenueDailyVisitors['BQV'].value_counts()


# In[21]:


#FROM THE ABOVE , 'BQV' OPENED FOR 207 DAYS 
VenueDailyVisitors['BQV'].sum()


# TOTALVISIT for BQV IS 17250 
# AVERAGE VISIT IS 17250/207 = 83.3 APPROX. 83 VISIT PER DAY
# SO , EXPECTED TOTALYEARLYVISIT IS 83*365 = 30295

# In[22]:


VenueDailyVisitors['AEQ'].value_counts()


# In[23]:


#FROM THE ABOVE , 'AEQ' OPENED FOR 88 DAYS 
VenueDailyVisitors['AEQ'].sum()


# TOTALVISIT for AEQ IS 4766 
# AVERAGE VISIT IS 4766/88 = 54.15 APPROX. 54 VISIT PER DAY
# SO , EXPECTED TOTALYEARLYVISIT IS 54*365 = 19710

# In[24]:


VenueDailyVisitors['YVW'].value_counts()


# In[25]:


#FROM THE ABOVE , 'YVW' OPENED FOR 69 DAYS 
VenueDailyVisitors['YVW'].sum()


# TOTALVISIT for YVW IS 7128 
# AVERAGE VISIT IS 7128/69 = 103.3 APPROX. 103 VISIT PER DAY
# SO , EXPECTED TOTALYEARLYVISIT IS 103*365 = 37595

# SO , EXPECTED TOTALYEARLYVISIT IS 103*365 = 37595FOR THE VENUES THAT CLOSED DOWN, ZPL AND XXQ , 
# WE WILL ALSO CALCULATE THEIR EXPECTED 

# In[26]:


VenueDailyVisitors['ZPL'].value_counts()


# In[27]:


#FROM THE ABOVE , 'ZPL' OPENED FOR 181 DAYS 
VenueDailyVisitors['ZPL'].sum()


# TOTALVISIT for ZPL IS 10616 
# AVERAGE VISIT IS 10616/181 = 58.65 APPROX. 59 VISIT PER DAY
# SO , EXPECTED TOTALYEARLYVISIT IS 59*365 = 21535

# In[28]:


VenueDailyVisitors['XXO'].value_counts()


# In[29]:


#FROM THE ABOVE , 'XXO' OPENED FOR 365-184 DAYS =  181 DAYS
VenueDailyVisitors['XXO'].sum()


# TOTALVISIT for XXO IS 16384 
# AVERAGE VISIT IS 16384/181 = 90.51 APPROX. 91 VISIT PER DAY
# SO , EXPECTED TOTALYEARLYVISIT IS 91*365 = 33215

# THE EXPECTED TOTAL YEARLY VISIT FOR THE VENUES THAT DID NOT OPEN AT THE START OF THE YEAR AND THE ONES THAT CLOSED DOWN BEFORE THE YEAR RUNS OUT ARE BELOW:
# ZJB =36865
# BKI = 23360
# YDI = 21900
# BQV = 30295
# AEQ = 19710
# YVW = 37595
# ZPL = 21535
# XXO = 33215

# SHOWING THE COUNT OF ZEROS(DAYS EACH VENUE DID NOT OPEN)CALCULATING THE DAYS EACH BRANCH OPEN AND THEN CALCULATING EXPECTED TOTALYEARLYVISIT  [END]

# MERGING THE DATA INTO A DATAFRAME[START]

# In[30]:


SummaryData1 = pd.merge(VenueSpend , VenueDuration)


# In[31]:


SummaryData2 = pd.merge( SummaryData1, VenueDistance)


# In[32]:


SummaryData3 = pd.merge(SummaryData2 , VenueGender)


# In[33]:


SummaryData4 = pd.merge(SummaryData3 , VenueAge)


# THE FOLLOWING DATA HAVE BEEN MERGED [VenueSpend , VenueDuration ,VenueDistance ,VenueGender VenueAge] into SummaryData4

# WE NEED TO MANIPULATE THE DATA TO INCLUDE THE TOTAL VENUE DAILY VISITORS FOR THE YEAR IN THE MERGED DATA.

# TO GET THE TOTAL VENUE DAILY VISITORS FOR THE YEAR 2019, WE NEED TO REMOVE THE FIRST COLUMN(The Dates).

# In[34]:


TotalVenueDailyVisitor = VenueDailyVisitors.iloc[1: , :].sum()


# In[35]:


type(TotalVenueDailyVisitor.dtypes)

CONVERSION OF "TotalVenueVisitor" INTO DATAFRAME
# In[36]:


TotalVenueDailyVisitors = pd.DataFrame(TotalVenueDailyVisitor)


# In[37]:


type(TotalVenueDailyVisitors)


# RESETTING THE INDEX AND RENAMING THE COLUMNS, TO  FACILITATE MERGING

# In[38]:


TotalVenueDailyVisitors.reset_index(inplace=True)


# In[39]:


TotalVenueDailyVisitors.rename(columns = {'index' : 'Id'  , 0:'TotalYearlyVisit'} , inplace= True)


# In[40]:


TotalVenueDailyVisitors.head() # THE FIRST FIVE DATAPOINT IN "TotalYearlyVisit"


# In[41]:


SummaryData = pd.merge(TotalVenueDailyVisitors , SummaryData4)


# MERGING THE DATA INTO A DATAFRAME [END]

# VIEWING SOME DATAPOINTS AND SUMMARY [START]

# The first five rows of the SummaryData are below

# In[42]:


SummaryData.head()


# In[43]:


SummaryData.describe()


# In[44]:


SummaryData.sum()


# From the above summary , we can segment the venues into three categories according to their TotalYearlyVisit.
# The categories are:
#     Low volume venue for venues having TotalYearlyVisit visit less than or equal to 22746.5, which is the 25th percentile as   shown above
#     Medium volume venue for venues having TotalYearlyVisit visit less than 56584.5, and
#     High volume venue for vunues having TotalYearlyVisit greater than 56585

# In[45]:


SummaryData.tail()


# VIEWING SOME DATAPOINTS AND SUMMARY [END]

# Function to segment SummaryData based on the Total Volume of visit [START]

# In[46]:


def categories(x):
    if x <= 22746.75:
        return 'Low volume venue'
    elif x <= 56584.5:
        return 'Medium volume venue'
    else :
        return 'High volume venue'
    
SummaryData['TypeOfVenue'] = SummaryData['TotalYearlyVisit'].apply(categories)


# Function to segment SummaryData based on the Total Volume of visit [END]

# VIEWING SOME STATISTICS ABOUT SUMMARYDATA [START]

# SUMMARY DATA IN DESCENDING ORDER OF "TOTALYEARLYVISIT" 
# THIS WILL SHOW THE VENUES WITH THE HIGHEST VISITS FIRST

# In[47]:


SortedSummary = SummaryData.sort_values("TotalYearlyVisit" , ascending=False)


# In[48]:


SortedSummary.head(4) #showing the branches with highest TotalYearlyVisit


# In[49]:


SortedSummary.head(4).sum()


# In[50]:


SortedSummary.tail() #Showing the branches with the lowest TotalYearlyVisit


# In[51]:


SummaryData.sort_values("Max travel distance (mls)" , ascending=False).tail()


# INVESTIGATING "SummaryData" for correlation

# In[52]:


correlation = SummaryData.corr()


# In[53]:


correlation #To check relationships


# VISUALIZING THE RELATIONSHIPS

# In[54]:


sns.heatmap(correlation , xticklabels= correlation.columns , yticklabels = correlation.columns , annot=True)


# In[55]:


sns.pairplot(SummaryData , kind = "reg" )


# In[56]:


fig = px.line(SummaryData, x="Id", y=[SummaryData['TotalYearlyVisit']/1000 ,'Max travel distance (mls)'], 
              title='Plot of TotalYearlyVisit(in 1000) and Max travel distance(mls) to show correlation')
fig.show()


# In[57]:


fig = px.line(SummaryData, x="Id", y=['Avg spend (£)' , 'Avg age (yrs)'], 
              title='Plot of "Avg spend (£)" and "Avg age (yrs)" to show correlation')
fig.show()


# In[58]:


sns.distplot(SummaryData['Avg age (yrs)'])   


# Barplot of TotalYearlyVisit [Start]

# In[59]:


fig = px.bar(SummaryData.sort_values("TotalYearlyVisit" , ascending =False) , x ='Id' , y = ["TotalYearlyVisit"])
fig.show()


# Barplot of TotalYearlyVisit in descending order [End]

# pieplot of TotalYearlyVisit in order to show the percentage visit of each venue

# In[60]:


fig = px.pie(SummaryData.sort_values('TotalYearlyVisit' , ascending = False), values='TotalYearlyVisit', names='Id')
fig.show()


# SUMMARY OF DATA TotalYearlyVisit 

# In[61]:


SummaryData.sort_values('TotalYearlyVisit' , ascending = False).head(4).sum()


# In[62]:


SummaryData.groupby('TypeOfVenue').agg({'TotalYearlyVisit': ['count' ,'sum' , 'mean']})


# ESTIMATING THE REVENUE, CALCULATED BY MULTIPLYING TOTALYEARLYVISIT BY THE AVERAGESPEND[START]

# In[63]:


VenueRevenue = SummaryData.loc[: , SummaryData.columns.drop(['Avg visit duration (mins)' , 'Max travel distance (mls)' ,
                                                            'Proportion Female (%)' , 'Avg age (yrs)'])]
VenueRevenue['Revenue'] = VenueRevenue['TotalYearlyVisit'] * VenueRevenue['Avg spend (£)']


# In[64]:


VenueRevenue.head()


# In[65]:


SortedRevenue =VenueRevenue.sort_values('Revenue' , ascending =False)
SortedRevenue.head() #showing the branches with highest revenue


# In[66]:


SortedRevenue.tail() #showing the branches with lowest revenue


# TOTAL VISIT FOR THE YEAR 2019 FOR THE FOUR VENUES WITH HIGHEST TOTALYEARLYVISIT

# In[67]:


SummaryData.sort_values('TotalYearlyVisit' , ascending = False).head(4).sum()


# SHOWING LIST OF LOW VOLUME VENUES , MEDIUM VOLUME VENUES AND HIGH VOLUME VENUES [START]

# In[68]:


low =SummaryData.loc[SummaryData['TypeOfVenue']== 'Low volume venue']
low.iloc[: , :1]


# In[69]:


medium =SummaryData.loc[SummaryData['TypeOfVenue']== 'Medium volume venue']
medium.iloc[: , :1]


# In[70]:


high = SummaryData.loc[SummaryData['TypeOfVenue']== 'High volume venue']
high.iloc[: , :1]


# SHOWING LIST OF LOW VOLUME VENUES , MEDIUM VOLUME VENUES AND HIGH VOLUME VENUES [END]

# PIE PLOT OF THE ESTIMATED REVENUE
# THE ESTIMATED REVENUE WAS CALCULATED BY MULTIPLYING TOTALYEARLYVISIT BY THE AVERAGESPEND

# In[71]:


fig = px.pie(VenueRevenue, values='Revenue', names='Id')
fig.show()


# In[72]:


VenueRevenue.sum()


# In[73]:


VenueRevenue.head(4).sum() #TO GET SUM OF TOTALYEARLYVISIT AND ESTIMATED REVENUE FOR THE OUTLIER VENUES


# GROUPING VENUES BY ESTIMATED REVENUE

# In[74]:


VenueRevenue.groupby('TypeOfVenue').agg({'Revenue': ['count' ,'sum' , 'mean']})


# VIEWING THE EXPECTED CONTRIBUTION OF LOW VOLUME VENUES , MEDIUM VOLUME VENUES AND HIGH  VOLUME VENUES

# In[75]:


VenueRevenue.groupby('TypeOfVenue').sum().plot(
    kind = 'pie' ,y = 'Revenue' ,autopct='%1.0f%%' , figsize =(15 , 15))


# TO GET A TRUE PICTURE OF THE TOTAL YEARLY VISIT ,
# WE NEED TO PUT IN THE VALUES OF EXPECTED TOTAL YEARLY VISIT FOR THE VENUES THAT OPENED DURING THE YEAR.
# TO DO THAT A DEEP COPY OF THE SUMMARYDATA WILL BE DONE , THEN THE COPY WILL BE ALTERED

# In[76]:


CopySummaryData = SummaryData.copy(deep=True)


# INSERTING THE EXPECTED TOTAL YEARLY VISIT OF THE VENUES WE NEED TO PUT IN THE VALUES OF EXPECTED TOTAL YEARLY VISIT FOR THE VENUES THAT OPENED DURING THE YEAR.
# ZJB = 36865
# BKI = 23360
# YDI = 21900
# BQV = 30295
# AEQ = 19710
# YVW = 37595
# ZPL = 21535
# XXO = 33215

# In[77]:


CopySummaryData.loc[0 , 'TotalYearlyVisit'] = 36865
CopySummaryData.loc[5 , 'TotalYearlyVisit'] = 23360
CopySummaryData.loc[18 , 'TotalYearlyVisit'] = 21900
CopySummaryData.loc[32 , 'TotalYearlyVisit'] = 30295
CopySummaryData.loc[34 , 'TotalYearlyVisit'] = 19710
CopySummaryData.loc[39 , 'TotalYearlyVisit'] = 37595
CopySummaryData.loc[16 , 'TotalYearlyVisit'] = 21535
CopySummaryData.loc[30 , 'TotalYearlyVisit'] = 33215


# BARPLOT OF TOTALYEARLYVISIT AFTER INSERTING THE EXPECTED TOTALYEARLYVISIT

# In[78]:


fig = px.bar(CopySummaryData.sort_values("TotalYearlyVisit" , ascending = False) , x ='Id' , y = ["TotalYearlyVisit"])
fig.show()


# Function to segment CopySummaryData based on the Total Volume of visit [START]

# In[79]:


def categories(x):
    if x <= 24578.75:
        return 'Low volume venue'
    elif x <= 56584:
        return 'Medium volume venue'
    else :
        return 'High volume venue'
    
CopySummaryData['TypeOfVenue'] = CopySummaryData['TotalYearlyVisit'].apply(categories)


# Function to segment CopySummaryData based on the Total Volume of visit [END]

# In[80]:


CopySummaryData.head()


# In[81]:


CopySummaryData.tail()


# In[82]:


CopySummaryData.describe()


# In[83]:


CopySummaryData.groupby('TypeOfVenue').agg({'TotalYearlyVisit': ['count' ,'sum' , 'mean']})


# VIEWING THE LOW VOLUME VENUES , MEDIUM VOLUME VENUES AND HIGH VOLUME VENUES AFTER PUTTING IN THE EXPECTED TOTALYEARLYVISIT

# In[84]:


lowCopySummaryData =CopySummaryData.loc[CopySummaryData['TypeOfVenue']== 'Low volume venue']
lowCopySummaryData.iloc[: , :1]


# In[85]:


#VIEWING THE NEW MEDIUM VOLUME VENUES
mediumCopySummaryData =CopySummaryData.loc[CopySummaryData['TypeOfVenue']== 'Medium volume venue']
mediumCopySummaryData.iloc[: , :1]


# In[86]:


HighCopySummaryData =CopySummaryData.loc[CopySummaryData['TypeOfVenue']== 'High volume venue']
HighCopySummaryData.iloc[: , :1]


# CALCULATING THE EXPECTED VENUE REVENUE FOR COPYSUMMARYDATA [START]

# In[87]:


ExpectedVenueRevenue = CopySummaryData.loc[: , CopySummaryData.columns.drop(['Avg visit duration (mins)' ,
                                                                             'Max travel distance (mls)' ,
                                                            'Proportion Female (%)' , 'Avg age (yrs)'])]
ExpectedVenueRevenue['Revenue'] = ExpectedVenueRevenue['TotalYearlyVisit'] * ExpectedVenueRevenue['Avg spend (£)']


# CALCULATING THE EXPECTEDVENUEREVENUE FOR COPYSUMMARYDATA [END]

# VIEWING THE COUNT , SUM AND MEAN EXPECTED REVENUE OF HIGH ,LOW AND MEDIUM VOLUME VENUES

# In[88]:


CopySummaryData.groupby('TypeOfVenue').agg({'TotalYearlyVisit': ['count' ,'sum' , 'mean']})


# In[89]:


ExpectedVenueRevenue.head()


# PLOT OF ESTIMATED CONTRIBUTION OF HIGH , LOW AND MUDIUM VOLUME VENUES

# In[90]:


ExpectedVenueRevenue.groupby('TypeOfVenue').sum().plot(
    kind = 'pie' ,y = 'Revenue' ,autopct='%1.0f%%' , figsize =(15 , 15))

