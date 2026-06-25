# Testcase1 : Helloworld  
# Output : ooe  
# Explanation : Vowels in the given string Helloworld are e,o,o . The  reverse order of eoo is ooe.  
ch="helloword"
rev=""
for i in ch:
    if i in "aeiou":
        rev+=i
print(rev[::-1])

# Testcase1 : JackspArrow  
# Output : oAa  
# Explanation : Vowels in the given string JackspArrow are a,A,o . The  reverse order of aAo is oAa.  
s="jackspArrow"
vowels=""
for i in s:
    if i in "Aaeiou":
        vowels+=i
print(vowels[::-1])

# Write a program to print the vowels in the given string and repeated  vowel should be printed only single time.  
# Testcase1 : Helloworld  
# Output : eo  
# Explanation : Vowels in the given string Helloworld are e,o,o . The  single vowels among them are eo .  

case="helloworld"
ch=""
for i in case:
    if i in "aeiou" and i not in ch:
        ch+=i
print(ch)

# Testcase1 : Jacksparrow  
# Output : ao  
# Explanation : Vowels in the given string Helloworld are a,a,o . Among  them a is repeated more than once,
#  so consider it for one time , result is  ao.

s="Jacksparrow"
vowels=""
for i in s:
    if i in "aeiou" and  i not in vowels:
        vowels+=i
print(vowels)

# Write a program to print the string after removing the duplicate characters  in the string.  
# Testcase1 : madam  
# Output : d  

s="madam "
for i in s:
    if s.count(i)==1:
       print(i)


# Testcase1 : donkey  
# Output : donkey  
# Explanation : In the given string there is no duplicate character.  

s="donkey"
ch=""
for i in s:
    if i not in ch:
        ch+=i
print(ch)

s="donkey"
ch=""
for i in s:
    if s.count(i)==1:
        ch+=i
print(ch)


# Write a program to convert all the upper case letters in the given string to  lower case letter and vice versa.  
# Testcase1 : JohnWick  
# Output : jOHNwICK  
# Explanation : All the upper case letters changed to lower case and vise  versa.  

H="JohnWick"
ch=""
for i in H:
    if i.isupper():
     ch+=i.lower()
    else:
       ch+=i.upper()
print(ch)

# Testcase1 : Korean  
# Output : kOREAN  
# Explanation : All the upper case letters changed to lower case and vise  versa.  

s="Korean"
ch=""
for i in s:
   if i.islower():
      ch+=i.upper()
   else:
      ch+=i.lower()
print(ch)

# • Write a program to print all the Upper case letters in the string in reverse 
#  order and then followed by the lower case letters .  
# Testcase1 : NumberOne  
# Output : ONumberne  
# Explanation : In the given string NumberOne, Uppercase letters are N,O.  
# The reverse order of them are ON next it is followed by lowe case letters  (umberne). So final string is ONumberne.

l="NumberOne"
ch=""
for i in l:
    if i.isupper():
        ch=i+ch
for i in l:
    if i.islower():
        ch+=i
print(ch)



# Testcase1 : ClassLeader  
# Output : LClasseader  
# Explanation : In the given string ClassLeader, Uppercase letters are C,L.  The reverse order of them are LC next it is followed by lowe case letters  (lasseader). 
# So final string is LClasseader. 
s="ClassLeader"
ch=""
for i in s:
    if i.isupper():
        ch=i+ch
for i in s:
    if i.islower():
        ch+=i
print(ch)





