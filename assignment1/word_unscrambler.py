#!/usr/bin/env python
# coding: utf-8

# In[8]:


user_input = input("Please enter a word: ") #asks user for input
f = open('words.txt') #opens file 
data = f.readlines() #read in file line by line
sorted_user_input = sorted(user_input) #sorts alphabetically 
results = [] 


# In[9]:


for word in data:
    sorted_dict = sorted(word.strip().lower()) 
    if all(elem in sorted_user_input for elem in sorted_dict):  
        results.append(word.strip()) #if word exists in dict append to results 


# In[10]:


sorted_word_list = sorted(results, key = len) #sorts appended list into new sorted_word_list


# In[11]:


print("All 6 lettered words:") #print message all 6 lettered words - words created from unscrambled user input word
for word2 in sorted_word_list: 
    if (len(word2) == 6): #include only words that have 6 letters
        print(word2)


# In[12]:


print("All 5 lettered words:") #print message all 5 lettered words - words created from unscrambled user input word
for word3 in sorted_word_list:
    if (len(word3) == 5): #include only words that have 5 letters
        print(word3)


# In[13]:


print("All 4 lettered words:") #print message all 4 lettered words - words created from unscrambled user input word
for word4 in sorted_word_list:
    if (len(word4) == 4): #include only words that have 4 letters
        print(word4)


# In[14]:


print("All 3 lettered words:") #print message all 3 lettered words - words created from unscrambled user input word
for word5 in sorted_word_list:
    if (len(word5) == 3): #include only words that have 3 letters
        print(word5)


# In[ ]:





# In[ ]:





# In[ ]:

