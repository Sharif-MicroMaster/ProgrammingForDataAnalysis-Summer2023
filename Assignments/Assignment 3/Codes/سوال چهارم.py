import numpy as np

array = input().split(' ')
for i in range(0,100) :
    array[i]=(int)(array[i])

jamiat = np.array(array)
sum_all = jamiat.sum()
sum_up_60 = jamiat[61:].sum()

print("{0:.2f}".format(sum_all))
print("{0:.2f}".format(sum_up_60))

help = np.array(range(100))

print("{0:.2f}".format(np.inner(help,jamiat)/sum_all))
print("{0:.2f}".format(np.argmax(jamiat)))