#!/usr/bin/env python
# coding: utf-8

# In[67]:


#Question 1: Write a RegEx pattern in python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re

RegExpattern = r'^[a-zA-Z0-9]+$'

test_string = "Kehinde789!"
if re.match(RegExpattern, test_string):
    print("The String contains only a-z, A-Z, and 0-9.")
else:
    print("The String contains other characters.")


# In[68]:


#Question 2: Write a RegEx pattern that matches a string that has an 'a' followed by zero or more b's

import re

RegExpattern = r'ab*$'

test_string = "a"
if re.match(RegExpattern, test_string):
    print("Match detected.")
else:
    print("No match detected.")



# In[69]:


#Question 3: Write a RegEx pattern that matches a string that has an 'a' followed by one or more b's

import re

RegExpattern = r'ab+$'

test_string = "a"
if re.match(RegExpattern, test_string):
    print("Match located.")
else:
    print("No match located.")


# In[70]:


#Question 4: Write a RegEx pattern that matches a string that has an 'a' followed by zero or one 'b'

import re

RegExpattern = r'ab?$'

test_string = "abbb"
if re.match(RegExpattern, test_string):
    print("Match located.")
else:
    print("No match located.")


# In[71]:


#Question 5: Write a RegEx pattern in python program that matches a string that has an a followed by three 'b's.

import re

RegExpattern = r'abbb$'

test_string = "abbbb"
if re.search(RegExpattern, test_string):
    print("Match detected.")
else:
    print("No match detected.")


# In[72]:


#Question 6: Write a RegEx pattern in python program that matches a string that has an a followed by two to three 'b's.

import re

RegExpattern = r'ab{2,3}$'

test_string = "ab"
if re.search(RegExpattern, test_string):
    print("Match detected.")
else:
    print("No match detected.")




# In[73]:


#Question 7: Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

RegExpattern = r'a.*b$'

test_string = "axyzb"
if re.match(RegExpattern, test_string):
    print("Match found in string.")
else:
    print("No match found in string.")


# In[74]:


#Question 8: Write a RegEx pattern in python program that matches a word at the beginning of a string.

import re

RegExpattern = r'^\w+'

test_string = "Morning, beautiful people"
match = re.search(RegExpattern, test_string)
if match:
    print("Match found in string:", match.group())
else:
    print("No match found in string.")


# In[75]:


#Question 9: Write a RegEx pattern in python program that matches a word at the end of a string

import re

RegExpattern = r'\w+$'

test_string = "Morning, beautiful people"
match = re.search(RegExpattern, test_string)
if match:
    print("Match detected in string:", match.group())
else:
    print("No match detected in string.")


# In[76]:


#Question 10: Write a RegEx pattern in python program to find all words that are 4 digits long in a string. 
#Sample text- '01 0132 231875 1458 301 2725.'

import re

RegExpattern = r'\b\d{4}\b'

string = '01 0132 231875 1458 301 2725.'

matches = re.findall(RegExpattern, string)

print(matches)

