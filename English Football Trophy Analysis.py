#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# df = pd.read_html('http://krysstal.com/trophies.html')
# df = df[1]

# df.to_csv("English Football Trophy List.csv")


# In[3]:


pl = pd.read_csv("English Football Trophy List.csv")


# In[4]:


pl["Rank"] = pl["Unnamed: 0"] + 1


# In[5]:


pl.set_index("Rank", inplace=True)


# In[6]:


pl.head()


# In[7]:


# Removing Unwanted Columns 
pl.drop("Unnamed: 0", axis=1, inplace=True)


# In[8]:


pl.head(10)


# How many Rows and Columns?

# In[9]:


pl.info()
# 53 rows and 9 columns 


# Which Clubs have won Champions League?

# In[10]:


pl[pl["UEFAChampions\'League"] >= 1][["Club", "UEFAChampions\'League"]].sort_values("UEFAChampions\'League", ascending =False)


# Only 5 clubs in England have won the Champions League

# In[11]:


len(pl[pl["UEFAChampions\'League"] >= 1])


# Which Clubs have the Premier League?

# In[12]:


pl[pl["League"] >= 1][["Club", "League"]].sort_values("League", ascending =False)


# 24 clubs in England have won the Premier League

# In[13]:


len(pl[pl["League"] >= 1])


# Which Clubs have won Europa League?

# In[14]:


pl[pl["EuropaLeague"] >= 1][["Club", "EuropaLeague"]].sort_values("EuropaLeague", ascending =False)


# Only 8 clubs in England have won the Europa League

# In[15]:


len(pl[pl["EuropaLeague"] >= 1])


# Which Clubs have an FA Cup?

# In[16]:


pl[pl["FA Cup"] >= 1][["Club", "FA Cup"]].sort_values("FA Cup", ascending =False)


# 43 clubs in England have a FA Cup

# In[17]:


len(pl[pl["FA Cup"] >= 1])


# Search for the club representing Oxford University

# In[18]:


pl[pl["Club"] == "Oxford University"]


# Search for Clubs with "Town", "City", "United" in their names

# In[19]:


def club_finder(name, club):
    if name in club.lower().split():
        return True
    else:
        return False


# Clubs with "Town"

# In[20]:


town = pl[pl["Club"].apply(lambda x : club_finder("town", x))]
town


# In[21]:


len(town)


# Clubs with "City"

# In[22]:


city = pl[pl["Club"].apply(lambda x : club_finder("city", x))]
city


# In[23]:


len(city)


# Clubs with "United"

# In[24]:


united = pl[pl["Club"].apply(lambda x : club_finder("united", x))]
united


# In[25]:


len(united)


# Which Clubs have recently won trophies?

# In[30]:


pl.sort_values("LastTrophySeason", ascending=False)[["Club", "LastTrophySeason"]]

