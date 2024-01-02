#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 


# In[20]:


data = {
    '이름' : ['홍길동', '정대만', '송경영', '서코딩', '강백호', '변인정', '황태산', '윤행복'],
    '학교' : ['부산고', '부산고', '부산고', '부산고', '부산고', '경남고', '경남고', '경남고'],
    '키' : [187, 174, 168, 187, 178, 165, 188, 180],
    'MIS' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '통계' : [100, 50, 70, 70, 10, 95, 45, 90],
    '파이썬' : [95, 55, 80, 75, 35, 85, 40, 95],
    '파워Query' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
df


# In[21]:


data['이름'] # 사전구조는 key, value로 구성 


# In[22]:


df.index.name = '지원번호'
df


# In[19]:


df.reset_index(drop=True) # 원래 쓰던 '지원번호' 인덱스 삭제 (drop=True)


# In[23]:


df.reset_index() # 새로운 인덱스가 생성되고, 기존 지원번호 인덱스는 새로운 column으로 변경됨 


# In[24]:


df.reset_index(drop=True, inplace=True)
df


# In[25]:


df.set_index('이름') # 인덱스를 이름으로 설정


# In[26]:


df.sort_index() # 올림 차순으로 인덱스 정렬 (0부터 7까지)


# In[27]:


df.sort_index(ascending=False) # 내림 차순으로 인덱스 정렬 (7부터 0까지)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




