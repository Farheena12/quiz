#!/usr/bin/env python
# coding: utf-8

# # Quiz 

# In[1]:


class quiz:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer


# In[2]:


question_prompt = [
    "1.Convert the 22/7 fraction into mixed fraction.\n(a): 3 1/7\n(b): 2 2/7 \n(c): 2 1/7\n(d): 3 3/7 \n\n",
    "2.An equivalent fraction of 9/15 is. \n(a): 18/15 \n(b): 18/30 \n(c): 36/15 \n(d): 9/60 \n\n",
    "3.Find the value of 3 4/7 ÷ 7. \n(a): 12/7 \n(b): 21/28 \n(c): 25/7 \n(d): 25/49 \n\n"
]


# In[3]:


questions = [
    quiz(question_prompt[0], "a"),
    quiz(question_prompt[1], "b"),
    quiz(question_prompt[2], "d"),
]


# In[4]:


def take_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer :
            score +=1
    print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct")


# In[5]:


take_test(questions)


# In[ ]:




