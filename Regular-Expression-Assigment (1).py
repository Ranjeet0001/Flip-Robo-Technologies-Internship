#!/usr/bin/env python
# coding: utf-8

# In[48]:


# #solution-1

def replace_chars_with_colon(text):
    chars_to_replace = [' ', ',', '.']
    
    for char in chars_to_replace:
        text = text.replace(char, ':')
    
    return text

sample_text = 'Python Exercises, PHP exercises.'
result = replace_chars_with_colon(sample_text)
print(result)


# In[49]:


# #solution-2
import re

def find_words_starting_with_a_or_e(text):
    words = re.findall(r'\b[aAeE]\w+', text)
    return words

sample_text = " 'apple','bananna','graphes','aeroplane','trees','elephant','eagle','worker','earth','factory','energy'"
result = find_words_starting_with_a_or_e(sample_text)
print(result)


# In[50]:


# #solution-3

def find_words_at_least_4_characters(text):
    pattern = re.compile(r'\b\w{4,}\b')
    words = pattern.findall(text)
    return words

sample_text = "Virat Kohli is an Indian international cricketer who is widely regarded as one of the best batsmen."
result = find_words_at_least_4_characters(sample_text)
print(result)


# In[51]:


# solution-4

def find_words_with_length(text):
    pattern = re.compile(r'\b\w{3,5}\b')
    words = pattern.findall(text)
    return words

sample_text = "Virat Kohli is an Indian international cricketer who is widely regarded as one of the best batsmen"
result = find_words_with_length(sample_text)
print(result)


# In[52]:


#solution-5

def remove_parentheses(strings_list):
    pattern = re.compile(r'\(|\)')
    result = [pattern.sub('', s) for s in strings_list]
    return result
input_strings = [
    "example (.com)",
    "hr@fliprobo (.com)",
    "github (.com)",
    "Hello (Data Science World)",
    "Data (Scientist)"]
output_strings = remove_parentheses(input_strings)
for output in output_strings:
    print(output)


# In[53]:


#solution-6

with open("C:/Users/91770/Documents/input_text.txt.txt", 'r') as file:
    text = file.read()
pattern = r'\s*\([^)]+\)'
cleaned_text = re.sub(pattern, '', text)
cleaned_list = cleaned_text.strip('[]').split(', ')
print(cleaned_list)


# In[54]:


#solution-7

sample_text = "ImportanceOfRegularExpressionsInPython"
pattern = r'[A-Z][a-z]*'
uppercase_words = re.findall(pattern, sample_text)
print(uppercase_words)


# In[55]:


#solution-8

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
pattern = r'(?<=\d)(?=[A-Z])'
spaced_text = re.sub(pattern, ' ', sample_text)
print(spaced_text)


# In[56]:


#solution-9

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
pattern = r'(?<=[A-Z\d])(?=[A-Z])'
spaced_text = re.sub(pattern, ' ', sample_text)
print(spaced_text)


# In[57]:


#solution-10

sample_text = "Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com. Please contact us at hr@fliprobo.com for further information."

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
emails = re.findall(email_pattern, sample_text)

for email in emails:
    print(email)


# In[58]:


#solution-11

sample_text = "Hello_Datatrained_123"

pattern = r'^[A-Za-z0-9_]+$'
is_valid = bool(re.match(pattern, sample_text))
print(is_valid)


# In[59]:


#solution-12

sample_string = "123Datatrained"

pattern = r'^123'
starts_with_number = bool(re.match(pattern, sample_string))
print(starts_with_number)


# In[60]:


#solution-13

ip_address = "192.168.001.001"

pattern = r'\b0+(\d+)\b'
cleaned_ip = re.sub(pattern, r'\1', ip_address)
print(cleaned_ip)


# In[61]:


#solution-14

sample_text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

date_pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}(?:st|nd|rd|th)?\s\d{4}\b'
dates = re.findall(date_pattern, sample_text)
print(dates)


# In[62]:


#solution-15

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']

for word in searched_words:
    if re.search(word, sample_text):
        print(f"'{word}' found")
    else:
        print(f"'{word}' not found")


# In[63]:


#solution-16

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

match = re.search(searched_word, sample_text)
if match:
    print(f"'{searched_word}' found at position:", match.start())
else:
    print(f"'{searched_word}' not found")


# In[64]:


#solution-17

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = r'exercises'

substrings = re.findall(pattern, sample_text)
print(substrings)


# In[65]:


#solution-18

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = r'exercises'

matches = [(match.group(), match.start()) for match in re.finditer(pattern, sample_text)]
print(matches)


# In[66]:


#solution-19

def convert_date_format(date):
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    new_date = re.sub(pattern, r'\3-\2-\1', date)
    return new_date

date_yyyy_mm_dd = "2023-08-15"
date_dd_mm_yyyy = convert_date_format(date_yyyy_mm_dd)
print(date_dd_mm_yyyy)


# In[67]:


#solution-20

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
pattern = r'\b\d+(\.\d{1,2})?\b'
decimal_numbers = re.findall(pattern, sample_text)
print(decimal_numbers)


# In[68]:


#solution-21

sample_text = "the banana price 60,and the apple price is 70,or milk price is 65 rupee ltr."

numbers = re.findall(r'\d+', sample_text)
positions = [match.start() for match in re.finditer(r'\d+', sample_text)]

for num, pos in zip(numbers, positions):
    print(f"Number: {num}, Position: {pos}")


# In[69]:


#solution-22

sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
numbers = re.findall(r'\b\d+\b', sample_text)
max_number = max(map(int, numbers))
print(max_number)


# In[70]:


# solution-23

sample_text = "RegularExpressionIsAnImportantTopicInPython"
pattern = r'(?<=[a-z])(?=[A-Z])'
spaced_text = re.sub(pattern, ' ', sample_text)
print(spaced_text)


# In[71]:


#solution-24

sample_text = "AaBbcCcDdEfG"
pattern = r'(?<=[a-z])(?=[A-Z])'
matches = re.split(pattern, sample_text)
print(matches)


# In[72]:


#solution-25

sample_text = "Hello hello world world"
pattern = r'\b(\w+)\s+\1\b'
cleaned_text = re.sub(pattern, r'\1', sample_text)
print(cleaned_text)


# In[73]:


#solution-26

sample_string = "Datatrained123"

pattern = r'^.*[a-zA-Z0-9]$'
ends_with_alphanumeric = bool(re.match(pattern, sample_string))
print(ends_with_alphanumeric)


# In[74]:


#solution-27

sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
hashtags = re.findall(r'#\w+', sample_text)
print(hashtags)


# In[75]:


#solution-28

sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
pattern = r'<U\+[A-Za-z0-9]+>'
cleaned_text = re.sub(pattern, '', sample_text)
print(cleaned_text)


# In[76]:


#solution-29

with open('C:/Users/91770/Documents/sample_text.txt', 'r') as file:
    text = file.read()
pattern = r'\b\d{2}-\d{2}-\d{4}\b'
dates = re.findall(pattern, text)
for date in dates:
    print(date)


# In[77]:


#solution-30

import re

def remove_words_of_length(text, min_length, max_length):
    pattern = re.compile(r'\b\w{%d,%d}\b' % (min_length, max_length))
    cleaned_text = pattern.sub('', text)
    return cleaned_text

sample_text = "The following example creates an ArrayList with a capacity of 50 elements.4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
cleaned_text = remove_words_of_length(sample_text, 2, 4)
print(cleaned_text)

