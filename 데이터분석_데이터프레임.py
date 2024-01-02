#!/usr/bin/env python
# coding: utf-8

# In[2]:
import pandas as pd
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
df.index.name = '지원번호'
df

# In[7]:
df.to_csv('score.csv') # 한글 깨짐

# In[4]:
df.to_csv('score.csv', encoding = 'utf-8-sig') # 한글 인식 

# In[8]:
df.to_csv('score.csv', encoding = 'utf-8-sig', index = False) # 인덱스 삭제 

# In[14]:
df.to_csv('score.xlsx')

# In[11]:
df = pd.read_csv('score.csv') # csv 파일 열기
df

# In[12]:
# 특정 행 개수 제외하고 열기, row 0부터 시작됨
df = pd.read_csv('score.csv', skiprows=1) # 마지막 행 1개 제외하고 열기 
df

# In[15]:
# 특정 행 지정된 갯수만큼 제외하고 열기 
df = pd.read_csv('score.csv', skiprows=[1,3,5]) 
df

# In[17]:
# 특정 행 지정된 갯수만큼만 열기
df = pd.read_csv('score.csv', nrows=4) # 행 4개만 가져와서 열기 (0~3)
df

# In[43]:
# Dataframe 확인
df = pd.read_csv('score.csv') # csv 파일 열기
df
df.describe() # 계산 가능한 데이터에 대하여 컬럼별로 자동 계산 

# count: 데이터 갯수 / mean: 평균 / std: 표준 편차 / min: 최소값 / 25%~75%: 상위 퍼센트 값 / max: 최대값

# In[44]:
df.info() 
# entry 값: 8개 (0~7)

# In[45]:
df.head() # 처음 5개의 row를 가져옴 (0~4)

# In[46]:
df.head(7) # 처음 7개의 row를 가져옴 

# In[47]:
df.tail() # 마지막 5개의 row를 가져옴 (7~3)

# In[48]:
df.tail(3) # 마지막 3개의 row를 가져옴 (7~5)

# In[49]:
df.values # 데이터 프레임의 value 값을 가져옴 

# In[52]:
df.index # 데이터 프레임의 index 값을 가져옴 

# In[53]:
df.columns # 데이터 프레임의 column 값을 가져옴 

# In[54]:
df.shape # 데이터 프레임의 row, column 개수를 가져옴 

# In[57]:
# series 확인 
df['키'].describe() # 키 열의 데이터 프레임을 확인 

# In[58]:
df['키'].min() # 키 열의 최소값을 확인 

# In[59]:
df['키'].nlargest(3) # 키 열에서 가장 큰 순서대로 3개의 값을 가져옴 

# In[61]:
df['키'].mean(),df['키'].sum() # 키 열의 데이터 평균, 데이터 총합을 가져옴 

# In[62]:
df['학교'].unique() # 학교 열의 데이터 중에서 중복 제거 

# In[64]:
df['학교'].nunique() # 학교 열의 데이터 중에서 중복 제거 개수 
