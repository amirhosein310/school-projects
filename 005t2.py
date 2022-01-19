
list1 = ['98126125', '98125125', '98127125', '98127125', '98126125', '98126125','95125478', '96125478', '94125470','98125369' ]
EngCode = {127:'ind Eng', 126:'ele Eng', 125:'com Eng'}

list_num = len(list1)
code_num = len(EngCode)

ind_list = ['        ']*list_num
com_list = ['        ']*list_num
ele_list = ['        ']*list_num

# ***********************************************
ind_num = 0
ele_num = 0
com_num = 0
j = 0
# *****************
#while x <= code_num-1:
#    while j <= list_num-1:
#        if list1[j][4] == dic_keys[x][2]:
#            i += 1
#            countinglist[x] += 1
#            stu_list[x][i] = list1[j]
#        j += 1
#    x += 1
# ****************************
i = -1
while j <= list_num-1:
    if list1[j][4] == '7':
        i += 1
        ind_num += 1
        ind_list[i]=list1[j]
    j += 1
# *****************************
i = -1
j = 0
while j <= list_num-1:
    if list1[j][4] == '6':
        i += 1
        ele_num += 1
        ele_list[i] = list1[j]
    j += 1
# ****************************
j = 0
i = -1
while j <= list_num-1:
    if list1[j][4] == '5':
        i += 1
        com_num += 1
        com_list[i] = list1[j]
    j += 1
# ****************************
print(EngCode[125],'         ',EngCode[126],'         ',EngCode[127],
      '\n===============  ===============  ===============  ')

j=0
while j <= list_num-1:
    if com_list[j]!= '        ' or ele_list[j]!= '        ' or ind_list[j] != '        ' :
        print(com_list[j],'       ' ,ele_list[j],'       ' ,ind_list[j] )
    j += 1

print('===============  ===============  ===============  \n'
      ,com_num,'                ', ele_num,'                ', ind_num)
print("total students:",list_num)






