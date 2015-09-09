# -*- coding: cp949 -*

data=['a','b',['ab','c']]

print(data)

for steps in data:
    if isinstance(steps,list) :
        for step in steps:
            print(step)
    else :
        print(steps)

print(data.pop())
print(data)
print(data.count('a'))

# 차이 extend는 리스트가 아니고 append 리스트로
score = [52,42,35,42,63,63,90]
score.extend([50,60])
score.append([50,60])
print(score)

