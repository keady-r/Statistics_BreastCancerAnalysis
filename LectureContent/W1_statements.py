# IF statements - week 1 

import datetime

print ("Check if it's Tuesday ")

today = datetime.datetime.today()
dayofweek = today.weekday()

if dayofweek == 1:
    print ("It's a Tuesday")
elif dayofweek == 2:
    print ("It's a Wednesday")
else:
    print("it's not a Tuesday")

#For loops - week 1 Data Programming for Data Analytics 

list = [0,1,2,3,4,5,6,7,8,9]

for i in list:
    print (i)
    print (i*i) #squared (i*i*i)= cubed 
    

print ("Loops is over")

for i in range (10):
    print (i)
    
print ("range is over")

#Functions - give ability to jump into one part of the code and execute in another data in - data out concept 

ages = [10,20,30]
incomes = [100, 200, 300, 400, 600]

def calculateAverage(list):
    sum = 0;
    for i in list:
        sum = sum + i;
    return sum/len(list)

print ("the average is ", calculateAverage(ages))
print ("the average is ",calculateAverage(incomes))

#End week 1 