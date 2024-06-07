#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np


df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})


# In[14]:


# 1. Join based on the 'key' column
joined_df = df1.set_index('key').join(df2.set_index('key'), how='inner')
print("Joined DataFrame:")
joined_df


# In[15]:


# 2. Combine
df1 = pd.DataFrame({'A': [1, np.nan], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [np.nan, 8]})

combined_df = df1.combine_first(df2)
print("\nCombined DataFrame:")
combined_df


# In[16]:


# 3. Merge
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})

merged_df = pd.merge(df1, df2, on='key', how='inner')
print("\nMerged DataFrame:")
merged_df


# In[17]:


# 4. Melt
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
melted_df = pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])
print("\nMelted DataFrame:")
melted_df


# In[18]:


# 5. Replace
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 4]})
replaced_df = df.replace(4, 10)
print("\nReplaced Values DataFrame:")
replaced_df


# In[19]:


# 6. Filter
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
filtered_df = df[df['A'] > 1]
print("\nFiltered DataFrame:")
filtered_df


# In[20]:


# 7. Drop
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
dropped_df = df.drop(columns=['B'])
print("\nDropped Column DataFrame:")
dropped_df


# In[21]:


# 8. Concat
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

concat_df = pd.concat([df1, df2], axis=0)
print("\nConcatenated DataFrame:")
concat_df


# In[22]:


# 9. GroupBy
df = pd.DataFrame({'key': ['A', 'B', 'A', 'B'], 'value': [1, 2, 3, 4]})
grouped_df = df.groupby('key').sum()
print("\nGrouped DataFrame:")
grouped_df


# In[26]:


# 10. Handling Duplicates
df = pd.DataFrame({'A': [1, 2, 2, 3], 'B': [3, 4, 4, 5]})
# Check for duplicates
duplicates = df.duplicated()
print("\nDuplicates:")
duplicates


# In[27]:


# Drop duplicates
dropped_duplicates_df = df.drop_duplicates()
print("\nDropped Duplicates DataFrame:")
dropped_duplicates_df)


# In[ ]:




