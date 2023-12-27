#!/usr/bin/env python
# coding: utf-8

# In[1]:


input ('2019년 사고 건수: ')
input ('2019년 사망자수: ')


# In[2]:


# 사고건수와 사망자 입력 후 치명률 구하기 
accident = input('2019년 사고건수 입력')
dead = input('2019년 사망자수 입력')
rate = dead / accident * 100 


# In[15]:


year = input('연도를 입력하세요: ')
accident = int(input('사고건수를 입력하세요: '))
dead = int(input('사망자수를 입력하세요: '))
rate = dead / accident * 100 
print(rate)
print(f" ★{year}년도 사고건수: {accident}건, 사망자수: {dead}명 -> 치명률: {rate: .2f} 입니다")


# In[ ]:





# In[ ]:




