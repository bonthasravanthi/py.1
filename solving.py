 #Write a program to check whether the digits in-between the first and last digit are less than first and last digit, if yes then print true, otherwise print  false.  
#Testcase1 : 1672  
#Output : false

case=str(1672)
if int(case[1])<int(case[0])and int(case[1])<int(case[3]) and\
   int(case[2])<int(case[0])and int(case[2])<int(case[3]):
   print(True)
else:
    print(False)
#------------------------------------------------------------------------
input=str(9876549)
for i in range(0,1):
    for j in range(6,7):
        for k in range(1,6):
          
          if int(input[k])>int(input[i])and int(input[k])>int(input[j]):
             print(True)
          else:
             print(False)
             break

