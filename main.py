#no gpts
from jamo import h2j, j2hcj
import csv

f = open('서울교통공사 노선별 지하철역 정보.csv','r')
rdr = csv.reader(f)
print('자리가 확정되지 않은 자음/모음에 "_"를 넣으세요.')
print('답이 "행당"일때 "ㅎ"과 "ㅏ"의 자리만 확정되었다면 "ㅎ___ㅏ_"이라고 적으시면 됩니다.')
target = input()
target=j2hcj((h2j(target)))
pos=[]



# '-'가 있는 인덱스 확인
target_index = []
cnt = 0
for i in target:
    if i == '_':
        target_index.append(cnt)
    cnt += 1

for line in rdr:
    temp= j2hcj(h2j(line[1])) #역이름
    temp = list(temp) #바꾸는 이유 : 인덱스 찾아서 '-'으로 치환하려고

    for z in target_index: #인덱스 값에 맞게 치환
        if len(temp) != len(target):
            continue        #글자수 안맞으면 스킵
        
        temp[int(z)]='_'


    temp=''.join(temp)
    if target == temp:
        pos.append(line[1])


pos = set(pos)

if len(pos) ==0:
    print('다시 확인해보세요.')
else:
    print(pos)


f.close()