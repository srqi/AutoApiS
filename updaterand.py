# -*- coding: UTF-8 -*-
import json,sys,time,random
#先注册azure应用,确保应用有以下权限:
#files:	Files.Read.All、Files.ReadWrite.All、Sites.Read.All、Sites.ReadWrite.All
#user:	User.Read.All、User.ReadWrite.All、Directory.Read.All、Directory.ReadWrite.All
#mail:  Mail.Read、Mail.ReadWrite、MailboxSettings.Read、MailboxSettings.ReadWrite
#注册后一定要再点代表xxx授予管理员同意,否则outlook api无法调用
#以下空行不要删除，以便运行时插入机密

slice1 = [0]*4
randomapi=[1,2,6,7,21,22]
list1 = [[3,4,5],[8,9,10,11],[23,24,25,26,27,28],[14,15,16,17],[18,19,20]]
list2 = [1,2,2,2,2]
path=sys.path[0]+r'/randomapi.txt'

for i in range(0,3):
    slice1[i] = random.sample(list1[i], list2[i])
b = random.randint(0,3)
if b == 0 :
    slice1[3]=[12,13]
if b == 1 :
    slice1[3]=random.sample(list1[3], list2[3])
if b == 2 :
    slice1[3]=random.sample(list1[4], list2[4])
ga = slice1[0]
randomapi.append(ga[0])
for a in range(1,3):
    gg = slice1[a]
    for c in range(0,2):
        randomapi.append(gg[c])

random.shuffle(randomapi)
str2 = ','.join([str(x) for x in randomapi])
with open(path, 'w+') as f:
     f.write(str2)
