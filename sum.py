
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