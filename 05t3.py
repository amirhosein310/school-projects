import statistics as st
from termcolor import colored, cprint
dash = colored(' ---------------------------------------------------------------------','red')
error = colored(' error! ','red')
# main list ***********************
list1 = [[990101,[100,82]], [990102,[100,76]], [990105,[70,80]], [990322,[15,22]], [990405,[70,80]],[991105,[0.1,100]],[991215,[100,0.1]],[990127,[76,24]],[991107,[10,70]]]
# sorting by type ************************************
date_list = [i[0] for i in list1]
target_list = [i[1][0] for i in list1]
actual_list = [i[1][1] for i in list1]
# ****************************************************

# getting information in given period ***************
def count(list1, l, r):
    if r < l:
        print(error)
        exit()
    c = 0
    i = 0
    # traverse in the list1
    for x in list1:
        if x >= l and x <= r:
            c += 1
            ranege_dates[c-1]=list1[i]
            ranege_targets[c-1] = target_list[i]
            ranege_actuals[c-1] = actual_list[i]
        i += 1
    return c
# ***********************************

ranege_dates = [0]*len(list1)
ranege_targets = [0]*len(list1)
ranege_actuals = [0]*len(list1)

# getting period from user *********************
l = int(input('\nenter start date :'))
r = int(input('\nenter finish date: '))
# **********************************************
# first section of the report

print(dash)
print(' number of periods in the range given: ',count(date_list, l, r))
# removing zeros *********************************************************
ranege_dates = [i for i in ranege_dates if i != 0]
ranege_targets = [i for i in ranege_targets if i != 0]
ranege_actuals = [i for i in ranege_actuals if i != 0]
# ************************************************************************


# print('dates: ',ranege_dates)
# print('actuals: ',ranege_actuals)
# print('targets: ',ranege_targets)
print(' sum of actuals: ',sum(ranege_actuals))
print(' average of actulas is : ',st.mean(ranege_actuals))
print(' worst result :',min(ranege_actuals), 'best result: ', max(ranege_actuals))
# counting over average *********************************
over_average = 0
k = 0
while k <= len(ranege_actuals)-1:
    if ranege_actuals[k] > st.mean(ranege_actuals):
        over_average += 1
    k += 1
print(' number of results under average: ', over_average)

# counting under average ********************************

under_average = 0
k = 0
while k <= len(ranege_actuals)-1:
    if ranege_actuals[k] < st.mean(ranege_actuals):
        under_average += 1
    k += 1
print(' number of results over average: ', under_average)
# end of first section of report ******************************************************

# section 2:

b = int(input('\n each bar should be equal to (%):'))
print(dash)
print(' |    date    ', '|  progress %   |')
print(dash)

def hprint(section1, section2, section3,x):
    i=0
    while i <= len(section1)-1:
        neg_sgn = colored('-', 'red')
        pos_sgn= colored('+', 'green')
        progress_bar = round((section2[i] - section3[i])/x)
        progress_bar2 = (section2[i] - section3[i]) / x
        if progress_bar2 > 0:
            print('    ',section1[i],'      |', '%',section2[i]-section3[i],'      ','0',pos_sgn*progress_bar)
            i += 1
        if progress_bar2 < 0 :
            print('    ', section1[i], '      |', '%',section2[i] - section3[i], '      ', neg_sgn * -progress_bar,'0')
            i += 1
    return i

hprint (ranege_dates, ranege_targets, ranege_actuals, b)
print(dash)




