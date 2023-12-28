#!/usr/bin/env python
# coding: utf-8

# In[29]:


# 데이터프레임 구조
a= [5,4,3,2,1] # a 리스트에 요소값 5,4,3,2,1 대괄호 [] 사용
a[0:5] # 리스트의 첫 번째 값은 0부터 시작함 


# In[16]:


# 연도별 자료 리스트 저장
year = ['2019', '2020','2021']
tAccident = [4223, 4039, 4883]
tDead = [206, 223, 191]
rAccident = [28, 33, 27]
rDead = [5, 3, 2]

# 2019년 자료 가져오기 
print(f'{year[0]}년') # print(year[0],"년")
print(f'전체 사고건수 : {tAccident[0]}')
print(f'전체 사망자수 : {tDead[0]}')
print(f'역주행 사고건수 : {rAccident[0]}')
print(f'역주행 사망자수 : {rDead[0]}')


# In[15]:


# 2020년 2021년 자료 가져오기

print(f'{year[1:]}년')
print(f'전체 사고건수 : {tAccident[1:]}')
print(f'전체 사망자수 : {tDead[1:]}')
print(f'역주행 사고건수 : {rAccident[1:]}')
print(f'역주행 사망자수 : {rDead[1:]}')


# In[35]:


# 3년간 평균자료 산출 
print(f'3년간 평균')
print(f'전체 사고건수 : {sum(tAccident)/len(tAccident) : .2f}') # 소수점 둘째자리까지만 표현 
print(f'전체 사망자수 : {sum(tDead)/len(tDead) : .2f}')
print(f'역주행 사고건수 : {sum(rAccident)/len(rAccident) : .2f}')
print(f'역주행 사망자수 : {sum(rDead)/len(rDead) : .2f}')


# In[20]:


print(f'전체 사고건수: {tAccident[0]}') # 중괄호로 묶어야 변수로 인식함 
print(f'전체 사망자수: {tDead[0]}')
print(f'역주행 사고건수: {rAccident[0]}')
print(f'역주행 사망자수: {rDead[0]}')


# In[32]:


print(f'{year[0:2]}년')
print(f'{year[0:3]}년')
print(f'{year[1:3]}년')
print(f'{year[0:]}년')
print(f'{year[1:]}년')
print(f'{year[2:]}년')


# In[41]:


# 빈리스트 형성 
tRate = []

# 리스트에 자료 추가
tRate.append(tDead[0]/tAccident[0] * 100)  # list.append(object): 리스트에 자료를 추가하는 함수 
tRate.append(tDead[1]/tAccident[1] * 100)
tRate.append(tDead[2]/tAccident[2] * 100)

# 리스트 자료 수정
tRate[0]=round(tRate[0],2) # 소수 둘째자리까지 반올림
tRate[1]=round(tRate[1],2)
tRate[2]=round(tRate[2],2)

# 리스트 삭제
# tRate.pop(1) # 위치값으로 삭제 -> 리스트 1번에 있는 자료를 삭제한다 (5.52)
#tRate.remove(4,88) # 값을 기준으로 삭제 -> 값이 4.88인 자료를 삭제한다 (4.88)

print(tRate)


# In[50]:


# 치명률 빈리스트 생성
tRate = []
rRate = []

# 치명률 구하기 (for, round 함수 이용)
for i in range(len(year)):
    tRate.append(round(tDead[i] /tAccident[i] * 100, 2))
    rRate.append(round(rDead[i] /rAccident[i] * 100, 2))

# 자료 확인
print(f'전체 치명률: {tRate}, 3년 평균: {sum(tRate) / len(tRate) : .2f}')
print(f'역주행 치명률: {rRate}, 3년 평균: {sum(rRate) / len(rRate) : .2f}')


# In[52]:


# 연도별 전체 치명률
print(year)
print(tRate)

dt = {'2019': 4.88, '2020': 5.52, '2021': 3.95}
print(dt)


# In[53]:


dt = {'2019' : 4.88, '2020' : 5.52, '2021' : 3.95}
dt = dict(zip(year, tRate)) # zip으로 묶기
print(dt['2020'])


# In[55]:


# 3년간 치명률
for item in dt: # dt.keys()가 생략된 형태 
    print(item)
    
for item in dt:
    print(dt[item]) # dt의 key 값으로 가져오기 


# In[56]:


# 3년간 치명률 평균
print(f'3년간 치명률 평균 : {sum(dt.values()) / len(dt) : .2f}')

# key 값과 value 값 중요하다


# In[59]:


# 연도별 전체 치명률 
print(year)
print(tRate)

# dt = {'2019' : 4.88, '2020': 5.52, '2021' : 3.95}
dt = dict(zip(year, tRate)) # zip으로 묶기
print(dt['2020'])

# 3년간 치명률 
for item in dt.values(): 
    print(item)

# 3년간 치명률 평균
print(f'3년간 치명률 평균:{sum(dt.values()) / len(dt) : .2f}')


# In[ ]:




