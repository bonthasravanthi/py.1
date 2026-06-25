
nums=[2,4,6,8,9]
target=6
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
#--------------------------------------------------

nums=[5,6,7]
target=18
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==target:
                print(i,j,k)
print(target)

#-----------------------------------------------------------
# Write a program to print reverse of the given number.  
# Testcase1 : 721  
# Output : 127  
# Explanation : Reverse of the number 721 is 127

# using for loop
case=721
rev=""
for i in str(case):
    rev=i+rev
print(rev)

#----------------------------------------------------------------------------------
#without converting into str

num=896
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

#--------------------------------------------------------------------------------------
# #factorial

Testcase1 =3  
Output=6  
fact=1
for i in range(1,3+1):
    fact=fact*i
print(fact)

#------------------------------------------------------------------------


# The middle characters in the given word Wonder is nd.  
# using for loop

word="wonder"
outpu="nd"
for i in range(2,3):
    for j in range(3,4):
        print(word[i]+word[j])


#-----------------------------------------------------------------------

#by using slicing
    
ch="wonder"
output="nd"
result=ch[2:4]
print(result)

#-------------------------------------------------------------------------------

# finding middle character in the given word World is r

ch="world"
for i in range(2,3):
    print(ch[i])

 #-------------------------------------------------------------------------

# by using  string slicing function     
ch="world"
result=ch[2:3]
print(result)

#------------------------------------------------------------------------------

# by using if condition
ch="world"
ouput="r"
if ch[2]=="r":
    print(ch[2])
#--------------------------------------------------------------------------------
# Testcase1 : 75547  
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







