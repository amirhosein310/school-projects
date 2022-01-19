list = ['run','iran','iran','24','a','orange','a']
list_2 = set(list)
dic = {}
for i in list :
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1
print(list_2) #without duplicates
print(dic)