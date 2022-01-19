s = "Python is an incredibly efficient language: Python programs will do more in fewer lines of code than many other languages would require. Python ’s syntax will also help you write “clean” code. Python code will be easy to read, debug, extend and build upon compared to other languages"
print("sentence  : " + s)
res = len(s.split())
print(" \n number of words : " + str(res))
###################################################
d = dict()
for word in s.split(' '):
    if word in d:
        d[word] += 1
    else:
        d[word] = 0
k = sorted(list(d.items()), key = lambda x: (x[1], x[0]))
highest_freq = k[-1][1]
result = k[-1][0]
for i in reversed(range(len(k))):
    if k[i][1] < highest_freq:
        break
    else:
        result = k[i][0]
##################################################
print('\n most common word :',result)
