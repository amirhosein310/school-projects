#تمرین شماره یک
list1 = ['hello','hi','love','iran','2']
list2 = ['hi','hello','iran','iran','2']
duplicates = set(list1) & set(list2)
print('\n number of duplicates in lists:',len(duplicates))