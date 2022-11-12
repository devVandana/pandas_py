#!/usr/bin/env python
# coding: utf-8

# # Data Preparation- Pandas 
# 
# 

# ## Series

# A Series is very similar to a NumPy array . What differentiates the NumPy array from a Series, is that a Series can have axis labels, meaning it can be indexed by a label, instead of just a number location. It also doesn't need to hold numeric data, it can hold any arbitrary Python Object.

# In[124]:


import numpy as np
import pandas as pd
#from pandas import Series, DataFrame


# In[125]:


Series_obj = pd.Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'])
Series_obj


# Now we want to select an element with the label index of row 7:

# In[67]:


Series_obj['row 7']


# ## DataFrame

# Create a DataFrame object:
# 
# Here is an example of 36 random number in a 6x6 matrices.

# In[126]:


np.random.seed(25)
DF_obj = pd.DataFrame(np.random.rand(36).reshape((6,6)),
                   index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6'],
                   columns=['column 1', 'column 2', 'column 3', 'column 4', 'column 5', 'column 6'])
DF_obj


# ## Reading csv file

# In[ ]:


#pd.read_csv


# In[3]:


import pandas as pd

#How we read in a pandas dataframe. The header=0 means column names are in the first row
df=pd.read_csv('Downloads/mtcars.csv', header=0)
df


# ## The head() Method
# 

# In[4]:


#The head method returns the first five rows
df.head()


# ## Basic Features
# 

# In[76]:


#There are column names
df.columns


# In[77]:


#And there are row names
list(df.index)


# In[79]:


#Get the dimensions of the data frame with shape
dimensions = df.shape
dimensions


# In[80]:


#Get the data type of each column
df.dtypes


# In[81]:


#We can pick out a column by referencing its name. The result is a series or one dimensional data frame
df['mpg'].head()


# In[82]:


#You can similarly pick out columns as attributes with the '.'
df.mpg.head()


# Note that when we slice a series, the second entry in non-inclusive.

# In[83]:


#You can pick out multiple columns by specifying a list of column names
name_grade = df[['mpg', 'cyl','hp']].head()
name_grade


# ## Slicing and Indexing 
# 
# We will be using the .loc (just labels) approach.  You can also slice with .iloc (just indicies) or .ix (indices and labels).

# In[84]:


#Let's look at the data 
df.head()


# In[85]:


#Pick out a single entry
df.loc[3,"name"]


# In[87]:


#Select contiguous rows and columns 
df.loc[1:5, "disp":"wt"]


# In[88]:


#Select none continuguous rows
df.loc[[0,2,4], ["wt","am"]]


# ## Built in Functions
# 

# 
# 
# - Useful built in column methods.
# - Creating new columns and deleting existing ones.
# 

# In[89]:


#Read in the data frame
df=pd.read_csv("Downloads/mtcars.csv", header=0)

df.head()


# In[90]:


#Compute mean of carb column
avg_final = df["carb"].mean()
avg_final


# ## Creating New Columns
# 

# Next, we look at how to create new columns

# In[91]:


#Create a New Column that is a function of other columns
df["carb_new"] = df["carb"]/2
df.head()


# ## Deleting Columns (Drop Method)
# 

# In[92]:


#I can then delete it with the drop method
df.drop(["carb_new"], inplace = True, axis=1)
df.head()


# The inplace argument works as follows:
# 
#  - inplace = True : The dataframe itself will have the given column(s) deleted.
#  - inplace = False: Will return a dataframe with the column(s) deleted.
#  
#  The axis argument works as follows:
#  
#  - axis = 1 : delete columns given
#  - axis = 0 : delete rows given.
#  
#  Let's look at an example where we delete rows

# In[93]:


#Delete rows with index 0 and 2
drop_rows = df.drop([0,2], inplace = False, axis=0)
drop_rows.head()


# Let's have a look at df

# In[94]:


df.head()


# Note that df was not changed! This is what happens when you set inplace.

# Let's see how we can sort a data frame.  The inplace argument has the same affect as the drop method.

# In[95]:


#Sort the data frame according tothe mpg Column
#By setting inplace= False will just return the sorted dataframe and not chnage df 
df.sort_values(by = ["mpg"], inplace =False, ascending=False).head()


# Now let's sort by multiple columns, specifying more than one column is essentially specifying a tie break

# In[97]:


#Sort by Mini Exam 1 and tie breal with Previous Part

result_sorted = df.sort_values(by = ["mpg", "wt"], inplace =False, ascending=False)
result_sorted.head()


# 
# 
# In this part, we will a collection of important miscellaneous concepts that include:
# 
# - Changing columns names
# - Combining dataframes
# - Understanding the index
# - Missing Data
# 

# In[99]:


import pandas as pd

#Read in the data frame
df=pd.read_csv("Downloads/mtcars.csv", header=0)

df.head()


# Recall that we can get the column names through the attribute column

# In[100]:


#Get the column names
df.columns


# ## Changing Column Names
# 

# We can change column names through the rename method

# In[101]:


#Change the column names
df.rename(columns={"mpg":"mpg_1", "cyl":"cyl_1"}, inplace=True)

df.head()


# ## Concatenation

# In[ ]:


#pd.concat


# 
# 
# Next, we see how to combine or concatenate two (or more) data frames.

# In[102]:


#I can combine data frames with concat function
head = df.head()
tail = df.tail()


# In[103]:


#Have a look at the variable head
head


# In[104]:


#Have a look at the variable head
tail


# In[105]:


#axis=0 says stack them top to bottom. axis =1 stacks side to side 
dfConcat = pd.concat([head,tail], axis =0)
dfConcat


# ## Handling Missing Data
# 
# Missing data is common in most data analysis applications.  You have a number of options for filtering out missing data.  One option is doing it by hand or you can use the *dropna* method.

# With dataframes objects, things get a little more complex.  You may want to drop rows or columns which are all NA or just those containing any NAs. *dropna* by default drops any row containing a missing value.

# In[106]:


#Here we have two pieces of missing data
df_missing = pd.read_csv("Downloads/mtcars_missing.csv")
df_missing


# The isnull() method returns a series or dataframe of booleans corresponding to whether the particular entries are null or not.

# In[107]:


#isnull method for a data frame
df_missing.isnull()


# We can make sure they are all read in as NA values using the na_values input when we read in the file

# Now lets see how we can change/replace these NA values

# In[109]:


#Get rid of all rows with an NA
df_missing.dropna(axis=0)


# Rather than filtering ou missing data, you may want to fill in the "holes" in any number of ways. For most purposes, the *fillna* method with a constant relplaces missing values with that value.

# In[110]:


df_missing.fillna(0)


# In[112]:


#You can pass fillna a dict which gives the replacement value for each column
df_missing.fillna({"mpg":20,"hp":100})


# With *fillna* you can do lots of things with a little creativity.  For example, you might pass the mean of median value of a series.
# 

# In[113]:


#Replace with mean
df_missing.fillna(df_missing.mean())


# In[ ]:




