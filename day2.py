#  Testcase1 : 75547  
# Output : equal  
# Explanation : In the given number 7557, first digit and last digit sum  that is sum(7,7)=14 is equal to sum of remaining numbers that is  sum(5,5,4) = 14. So both sums are equal.  
digits=str(75547)
sum=14
for i in range(0,1):
    for j in range(4,5):
        middle_sum=0

        for k in range(1,4):
            middle_sum+=int(digits[k])

            if int(digits[i])+int(digits[j])==sum:
                if middle_sum==sum:
                    print("equal")
#----------------------------------------------------------------------------------------
# Testcase1 : 765  
# Output : not equal  
# Explanation : Sum(7,5)=12 and Sum(6)=6, both sums are not equal.  

num=str(765)
sum=12
for i in range(0,1):
    for j in range(2,3):
        middle_sum=0

        for k in range(1,2):
            middle_sum+=int(num[k])

            if int(num[i])+int(num[j])==middle_sum:
             print("equal")
            else:
             print("not equal")
#-------------------------------------------------------------------------------
digit=str(3528)
sum=11
for i in range(0,1):
    for j in range(3,4):
        middle_sum=0

        for k in range(1,3):
            middle_sum+=int(digit[k])

        if int(digit[i])+int(digit[j])==middle_sum:
                print("equal")
        else:
                print("not equal")







