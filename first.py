# a=10
# pi=3.14
# name='Parth'
# result=True
# print(type(a))
# print(type(pi))
# print(type(name))
# print(type(result))
# print(id(result))

# Accept three paper marks and calculate total percentage
# m1=50
# m2=80
# m3=70
# total=m1+m2+m3
# percentage=(total/300)*100
# print("Total=",total)
# print("Percentage=",percentage)

#Swapping of two numers using third variable
# val1=15
# val2=20
# temp=val1
# val1=val2
# val2=temp
# print("Val1=",val1)
# print("Val2=",val2)

#Swapping of two variables without using third variable
# a=100
# b=200
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

#WAP to calculate simple interest
# pa=100000
# tm=1
# r=0.08
# si=pa*tm*r
# print(si)

#WAP to calculate area of circle
# pi=3.14
# r=30
# area=pi*r*r
# print(area)

#WAP to calculate circumference of circle
# pi=3.14
# r=30
# circumference=2*pi*r
# print(circumference)

#WAP to enter height of user in feet and covert it into inch and centimeter
# h=20
# inch=h*12
# cm=inch*2.54
# print(inch)
# print(cm)

#WAP to take centigrade temperature and covert it into fahrenheit temperature
# centi=50
# f=1.8*centi+240
# print(f)

#Typecasting - conversion of value from one data type to another data type is known as type casting
# print(2+2) #addition
# print('2'+'2') #concatenation=22
# val=input('Enter value:')
# input function by default accept only string
# val=int(input('Enter value:'))

#int() used to convert into integer
# print(int(3.14))
# #print(int(10+5j))
# print(int(True))
# print(int(False))
# #print(int("4.22"))
# print(int("4"))
# print(int("parth"))
#we cannot convert complex values and floating point string values to int

# float()
# print(float(3))
# print(float(True))
# print(float(False))
# print(float(4.22))
# print(float("4"))
# name cannot be converted to float()

#complex()
# print(complex(3))
# print(complex(3.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))

# bool()
# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool())
# print(bool(False))
# print(bool(True))
# print(bool(-1))

# Memory management
# 1

# identity operator 
# used to compare

# membership operator
# we check if the value is presento or npt

#WAP to accept a number and check +, -, 0
# n=int(input())
# if n>0:
#     print("positive")
# if n<0:
#     print("negative")
# if n==0:
#     print("zero")

#accept 5 and find maximum
# a=input()
# b=input()
# c=input()
# d=input()
# e=input()
# if a>b and a>c and a>d and a>e:
#     print("A")
# if b>a and b>c and b>d and b>e:
#     print("B")
# if c>b and c>a and c>d and c>e:
#     print("C")
# if d>b and d>c and d>a and d>e:
#     print("D")
# if e>b and e>c and e>d and e>a:
#     print("E")

# String Slicing
# string is a group of characters
# name='parthtodankar'
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

# s="python is an object oriented programming language"
# print(s.find("python"))
# print(s.find("java"))
# print(s.find("language"))

# s="parth","umesh","todankar"
# m='%'.join(s)
# print(m)

# s="Python is high level programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# username = input('Enter username:')
# password = input('Enter password:')
# if username == password:
#     print('Login Successful')
# else:
#     print('Bad credentials')

#accept days, sat or sun => weekend, mon - fri => working day, 
# day=input('Enter day:')
# lday=day.lower()
# if lday=='monday' or lday=='tuesday' or lday=='wednesday' or lday=='thursday' or lday=='friday':
#     print("Weekday")
# else:
#     print("Weekend")

# accept 5 exam marks, if fail in any one sub, fail
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# if a<40 or b<40 or c<40 or d<40 or e<40:
#     print('Fail')
# else:
#     print('Pass')

# DAY2
# Convert the input to ACII code and determine it's case
# ch=ord(input('Enter any character'))
# # ord function is used to convert in ASCII code
# if ch>=65 and ch<=91:
#     print("upper case")
# elif cg>=97 and ch<=112:
#    print("lower case")
# elif ch>=48 and ch<=57:
#    print("digit")
# else:
#    print("special symbols")
   
# Nested if else
# if condition1:
#    if condition2:
#       statement
#     else:
#       statement
# else:
#    if condition3:
#       statement
#     else:
#       statement

# Print greatest number
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b:
#    if a>c:
#       print("A")
#    else:
#       print("C")
# else:
#    if b>c:
#       print("B")
#    else:
#       print("C")

# Print smallest number
# a=int(input())
# b=int(input())
# c=int(input())
# if a<b:
#    if a<c:
#       print("A")
#    else:
#       print("C")
# else:
#    if b<c:
#       print("B")
#    else:
#       print("C")

# for loop 
# for i in range(5): #i=0;i<5;i++
#     print(i)

# for i in range(5,11): #i=5;i<11;i++
#     print(i)

# for i in range(1,11,2): #i=1;i<11;i+2
#     print(i)

# 2 table
# for i in range(1,11): #i=10;i>0;i--
#     print(i*2)

# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5)
# print("")
# for i in range(1,11):
#     print(i*11," ",i*12," ",i*13," ",i*14)

# for i in range(1,11):
#     if i%2==0:
#         print('even')
#     else:
#         print('odd')

# even=0
# odd=0
# for i in range(1,101):
#     if i%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print(even)
# print(odd)

# for i in range(1,11):
#     print(i)
#     if i==5:
#         break 

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

# 5 factorial
# factorial=1
# for i in range(1,6):
#     factorial=factorial*i
# print(factorial)

# fibonacci
# a=1
# b=1
# print(a)
# for i in range(1,11):
#     c=a+b
#     print(b)
#     a=b
#     b=c

# Reverse number
# num = 123 #num=123
# a = num%10 #a=3
# num = num//10 #num=12
# b = num%10 #b=2
# num = num//10 #num=1
# c = num #c=1
# rev = a*100+b*10+c #300+20+1=321
# print(rev)

# name = 'parth'
# for i in name:
#     print(i)

# name = 'parth'
# for i in name:
#     print(i)
#     if i=='r':
#         break
    
# counta=0
# name = 'parth'
# for i in name:
#     # print(i)
#     if i=='a':
#         counta=counta+1
# print(counta)

# Reverse string
# name='parth'
# l=len(name)
# for i in range(l-1,-1,-1):
#     print(name[i])

# Another method
# name='parth'
# newstr=''
# l=len(name)
# for i in range(l-1,-1,-1):
#     newstr=newstr+name[i]
# print(newstr)

# Remove Duplicate characters in a string
# string='The quick brown fox jumps over the lazy dog' 
# newStr=''
# for i in string:
#     if i not in newStr:
#         newStr=newStr+i
# print(newStr)

# Count vowels and consonants
# string='The quick brown fox jumps over the lazy dog' 
# vowel=0
# consonant=0
# vowels='aeiou'
# for i in string:
#     if i in vowels:
#         vowel+=1
#     else:
#         consonant+=1
# print("Vowels=",vowel)
# print("Consonants=",consonant)

# .format() function
# name="parth"
# sal=5000000
# age=20
# print("{} sal is {} age is {}".format(name,sal,age))
# print("{0} sal is {1} age is {2}".format(name,sal,age))
# print("{x} sal is {y} age is {z}".format(x=name,y=sal,z=age))
# A=1
# print(f"{A} is a good boy")

# Palindrome number
# string="racecar"
# string=input()
# revstr=''
# for i in range(len(string)-1,-1,-1):
#     revstr=revstr+string[i]
# if string==revstr:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Another method
# string="racecar"
# if string==string[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Anagram listen=silent
# a='listen'
# b='silent'
# a=sorted(a)
# b=sorted(b)
# if a==b:  #sorted(a)==sorted(b)
#     print("Anagram")
# else:
#     print("Fail")

# Pangram
# str='The quick brown fox jumps over the lazy dog'
# str=str.lower()
# flag=0
# for i in str:
#     a=ord(i)
#     # if a>=97 and a<=122:
#     #     b=0
#     # else:
#     #     flag=1
# if flag==0:
#     print("Pangram")
# else:
#     print("Fail")

#Correct method
# string = 'The five boxing wizards jump quickly.'
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# flag=0
# for char in alphabet:
#     if char not in string.lower():
#         flag=1
# if flag==0:
#    print("Pangram")
# else:
#    print("Fail")
              
# Count substrings in a string input:abababab and ab output:4
# string = 'abababababab'
# count = string.count('ab')
# print('No. of occurrences: ', count)

# Count words in a string
# string="this is a sentence"
# count=1
# for i in string:
#     if i ==' ':
#         count+=1
# print(count)

# Reverse words in a string input: Hello World output: World Hello
# string = "hello world" 
# words = string.split() # split into words 
# words.reverse() # reverse the list 
# print(' '.join(words)) # join words back into a string 

# Title case a sentence
# string="hello world"
# string=string.replace(string[0],string[0].upper())
# for i in string:
#     if i==' ':
#         string=string.replace(string[i+1],string[i+1].upper())
# print(string) incomplete

# split
#capitaize

# find the first non repeating letter

# While loop syntax
# i=1 #initialization
# while i<5: #condition
#     print(i)
#     i=i+1 #increment

# i=1 #initialization
# while i<6: #condition
#     print(i)
#     if i==3:
#         pass
#     i=i+1 #increment
# output: 12345

# i=0 
# while i<6: 
#     i=i+1
#     if i==3:
#         continue
#     print(i)
# output: 12456

#sum of natural numbers from 1 to 10
# sum=0
# for i in range(11):
#     sum+=i
# print(sum)

#WAP to calculate factorial of any number
# n=int(input())
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)

#Fibonacci series
# a=1
# b=1
# print(a)
# print(b)
# for i in range(11):
#     c=a+b
#     print(c)
#     a=b
#     b=c

#lcm,hcf,gcd


#leap year
# year=2024
# if(year%4==0):
#     print("Leap year")
# else:
#     print("Year")

#armstrong number
# num=153
# n=num
# a=n%10
# n=n//10
# b=n%10
# n=n//10
# c=n
# arm=c*c*c+b*b*b+a*a*a
# if(num==arm):
#     print("Armstrong number")
# else:
#     print("Fail")

#palindrome number
#prime number
# num=int(input("Enter a number:"))
# flag=True
# if num<=1:
#     print("Invalid choice")
# for i in range(2,num):
#     if num%i==0:
#         print("Not prime")
#         break
#     if num%i!=0:
#         print("Prime")

# There are four types of collection data type in python
# List 
# - Order wise data
# - Heterogeneous data are possible
# - represented by []
# - Duplicate data allowed
# - Growable by nature
# - Mutable

# mylist = ["prashant","Ashish","Komal","ankush","ashish",77,"sandip",60.52,"prashant"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])

# mylist[0]="Akshay"
# print(mylist)

# if "ankush" in mylist:
#     print("Available")
# else:
#     print("Not available")

# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist)

# mylist.insert(0,"sanket")
# print(mylist)

# mylist.remove("sandip")
# print(mylist)

# Clone
# newlist=mylist.copy()
# print(newlist)

# mylist = [['parth','todankar'],[85.86],[440022,"yyy"]]
# print(mylist[0][0])

# list=["parth", "todankar"]
# print(list*3)

# list2=[50,20.25]
# print(list+list2)

# del list2[1]
# print(list2)

# list2.clear()
# print(list2)

# name='parth'
# print(name)
# myname=list(name) #typecasting
# print(myname)

# mylist.reverse()
# print(mylist)

# mylist=[22,22,77,0,9,88]
# mylist.sort()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)

# List should contain homgeneous data

# newlist=mylist
# print(id(newlist))

# list = [4,8,2,9,10,18,9]
# for i in list:
#     print(i)

# Find maximum entity in a list
# list = [4,8,2,9,10,18,9]
# m=0
# for i in list:
#     if m<i:
#         m=i
# print(m)

# Another method
# max=list[0]
# for i in range(len(list)):
#     if max<list[i]:
#         max=list[i]
# print(max)

# Max and min
# max=list[0]
# min=list[0]
# for i in list:
#     if max<i:
#         max=i
#     if min>i:
#         min=i
# print(max)
# print(min)

# Total sum
# sum=0
# for i in list:
#     sum+=i
# print(sum)

# Count even odd
# even=0
# odd=0
# for i in list:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even)
# print(odd)

# Append if not in list
# newlist=[]
# for i in list:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)

#Find the second largest element
# list=[7,3,9,2,8]
# list.sort()
# print(list[-2])

# Remove duplicates from unsorted array

# Intersection of two arrays
# input: [1,2,2,1] and [2,2]
# output: [2]
# list1=[1,2,2,1]
# list2=[2,2]
# ans=[]
# for i in list1:
#     if i in list2:
#         if i not in ans:
#             ans.append(i)
# print(ans)

#Array rotation (2)
# list=[1,2,3,4,5]
# ans=[]
# l=len(list)
# p=0
# for i in range(l):
#     p=i-2
#     l+=1
#     ans.append(list[p])
# print(ans)

# Another approach
# list=[1,2,3,4,5]
# ans=[]
# for i in range(len(list)):
#     ans.append(list[i-2])
# print(ans)

# Find the majority element
# list=[3,3,4,2,4,4,2,564,4,2]
# maxcount=0
# n=0
# for i in list:
#     if list.count(i)>maxcount:
#         maxcount=list.count(i)
#         n=i
# print(n)

# val=[1,2,3,4,5]
# print(val.index(2))

# Input: 578378923 Output: 3
# Return the count of repeating digits

# n=[]
# for i in range(9):
#     n.append=input()

# n=[5,7,8,3,7,8,9,2,3]
# new=[]
# for i in n:
#     if n.count(i)>=2 and i not in new:
#         new.append(i)
# print(len(new))

# 1 2 3   1 1 1
# 1 2 3   2 2 2
# 1 2 3   3 3 3
# for i in range(1,4): #Row
#     for j in range(1,4): #Column
#         print(i, end=' ') # i=rows, j=columns
#     print()

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# n=5
# for i in range(1,n+1):
#     print("* "*n)

# A A A A A 
# B B B B B 
# C C C C C 
# D D D D D 
# E E E E E 
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=' ')
#     print()

# 5 5 5 5 5 
# 4 4 4 4 4 
# 3 3 3 3 3 
# 2 2 2 2 2 
# 1 1 1 1 1 
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i, end=' ')
#     print()

# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=' ')
#     print()

# A A A A A 
# B B B B B 
# C C C C C 
# D D D D D 
# E E E E E
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=' ')
#     print()

# E E E E E 
# D D D D D 
# C C C C C 
# B B B B B 
# A A A A A 
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(65+n-i),end=' ')
#     print()

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# n=5
# for i in range(1,n+1):
#     print(' '*(n-1),end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])
# Output: 13579

# input 5, output 12345
# n = input()
# list=[]
# for i in range(1,int(n)+1):
#     list.append(str(i))
# print(''.join(list)) 

# 1 5
# 2 4
# 4 2
# 5 1
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i,' ',j) 

# Exam practice

# Array Rotation
# Given an array and a no k, rotate the array to the right by k elements
# Input:[1,2,3,4,5], 2
# Output:[4,5,1,2,3]

# list=[1,2,3,4,5]
# k=2
# ans=[]
# p=0
# for i in range(len(list)):
#     p=i-k
#     ans.append(list[p])
# print(ans)

# Zeroes to end
# Write a progran to move all zeros in the array to the end while
# maintaining the order of non-zero elements.
# Input:[0,1,0,3,12]
# Output:[1,3,12,0,0]

# nums = [0,1,0,3,12]
# ans=[]
# zeroCount=nums.count(0)
# for i in nums:
#     if i!=0:
#         ans.append(i)
# ans=ans+[0]*zeroCount
# print(ans)

# Prime Sum
# Write a function that calculates the sum of all prime numbers for input
# n upto 100.
# Input:10
# Output:17

# import math
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
# def sum_primes_upto_100(n):
#     # Ensure the upper limit is capped at 100
#     n = min(n, 100)
#     prime_sum = 0
#     for i in range(2, n + 1):
#         if is_prime(i):
#             prime_sum += i
#     return prime_sum
# # Test the function
# n = int(input("Enter a number: "))
# print("Sum of primes up to", n, "is:", sum_primes_upto_100(n))

# Missing Number
# You are given an array of numbers that represent an arithmetic
# sequence with one missing number. Your task is to find that missing
# number. The size of the input and output arrays must be kept same.
# Input:[1,3,7,9]
# Output:5

# def find_missing_number(arr):
#     n = len(arr)
#     # Calculate the expected common difference using the first two terms
#     d = (arr[-1] - arr[0]) // n  # Common difference based on the total range
#     # Check where the difference between consecutive elements is not equal to d
#     for i in range(1, n):
#         if arr[i] - arr[i - 1] != d:
#             return arr[i - 1] + d  # The missing number is the next term in the sequence
#     # If no missing number was found, return None (though this shouldn't happen)
#     return None
# # Test the function
# arr = [3, 5, 7, 11, 13]  # Example array with one missing number
# print("The missing number is:", find_missing_number(arr))

# Reverse String
# def reverse_string(s):
#     return s[::-1]
# s = input()
# print(reverse_string(s))

# using list
# def reverse_string(s):
#     char_list = list(s)
#     char_list.reverse()
#     return ''.join(char_list)
# s = input()
# print(reverse_string(s))

# Max Product of Three
# def max_product_of_three(nums):
#     nums.sort()
#     return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
# nums = eval(input().replace(" ", ""))
# print(max_product_of_three(nums))

# Anagram Checker
# a='listen'
# b='silent'
# a=sorted(a)
# b=sorted(b)
# if a==b:  #sorted(a)==sorted(b)
#     print("Anagram")
# else:
#     print("Fail")

# Sum of digits
# def sumd(num):
#     sum=0
#     for digit in num:
#         sum+=int(digit)
#     return sum
# n=input()
# print(sumd(n))

# Smallest Integer
# list=[3,5,8,2]
# s=list[0]
# for i in list:
#     if s>i:
#         s=i
# print(s)

# Digit from Array
# Given an array of single-digit integers, your task is to form a singe number
# by combining these digits. For example:
# • If the input array is [1,2,3] , the output should be 123
# • If the input array is [4,0,5], the output should be 405

# Note: The output should not have any leading zeros unless the number is 0.
# Implement a function that takes an array of integers and returns the
# combined number as an integer.

# def combine_digits(arr):
#     return int(''.join(map(str, arr)))
# user_input = input()
# arr = eval(user_input)
# result = combine_digits(arr)
# print(result)

# Max Subarray Sum
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = float('-inf')
#         currentSum = 0
#         for num in nums:
#             currentSum += num
#             if currentSum > maxSum:
#                 maxSum = currentSum
#             if currentSum < 0:
#                 currentSum = 0
#         return maxSum

# Climbing Stairs
# def climbStairs(n):
#     if n == 1:
#         return 1
#     # Base cases
#     prev2, prev1 = 1, 1  # ways(0) = 1, ways(1) = 1
#     # Start calculating from step 2 to n
#     for i in range(2, n + 1):
#         current = prev1 + prev2
#         prev2 = prev1
#         prev1 = current
#     return prev1
# # Test the function
# n = int(input("Enter the number of steps: "))
# print("Number of ways to reach the top:", climbStairs(n))

# Word Count
# def wordCount(text,word):
#     text=text.lower()
#     word=word.lower()
#     list=text.split()
#     return list.count(word)
# text=input()
# word=input()
# print(wordCount(text,word))

# import re
# def count_word_occurrences(text, word):
#     # Convert both the text and word to lowercase for case-insensitive comparison
#     text_lower = text.lower()
#     word_lower = word.lower()
#     # Remove non-alphabetic characters from each word in the text
#     cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text_lower)
#     # Split the cleaned text into a list of words
#     words = cleaned_text.split()
#     # Count the occurrences of the word in the list
#     return words.count(word_lower)
# # Take input from the user
# input_str = input('Enter the string and word to count (e.g., "This is a test", "test"): ')
# # Split the input into the string and word to count
# text, word = input_str.split('","')
# text = text[1:]  # Remove the starting double quote from the text
# word = word[:-1]  # Remove the ending double quote from the word
# # Get the number of occurrences of the word in the string
# result = count_word_occurrences(text, word)
# # Print the result
# print(f"The word '{word}' appears {result} times in the string.")

# Find Letter
# def check_letter_in_word(word, letter):
#     # Convert both the word and the letter to lowercase for case-insensitive comparison
#     word_lower = word.lower()
#     letter_lower = letter.lower()
#     # Check if the letter exists in the word
#     return letter_lower in word_lower
# # Take input from the user
# word = input()
# letter = input()
# # Get the result
# result = check_letter_in_word(word, letter)
# # Print the result
# print(result)

# Day 5
# immutable: no change in same memory
# mutable: can be changed

# Tuple is read only version of list
# t=()
# t=tuple()
# t=(1,2,3,4,5)
# t=1,2,3,4,5
# t=eval(input('Enter:')) #Enter as list, tuple, set{}

# t=eval(input())
# print(t)
# sum=0
# len=0
# for x in t:
#     sum=sum+x
#     len=len+1
# print("sum =",sum)
# print("avg =",sum/len)

# s=set()
# print(s)
# print(type(s))
# s={1,2,3,4,5}
# print(s)
# print(type(s))

# Dictionary
# Group of objects as key pairs
# d={}
# d=dict()
# d={101:"Parth",102:"Raj"}
# d=eval(input())
# print(d[101])

# Write a program to enter name and percentage marks in a dictionary and display information on the screen.
# rec={}
# n=int(input("Number of students:"))
# for i in range(1,n+1):
#     name=input("Name")
#     marks=input("Marks")
#     rec[name]=marks
# print(rec)
# for i in rec:
#     print(i,'\t',rec[i])

# Deleting and Clearing
# del d[200]
# d.clear()

# Create a dictionary
# dict()
# len()
# clear()
# get()

# d={100:"Parth", 200:"Partht"}
# print(d[100])
# print(d.get(100))
# print(d.get(100,"Guest")) # Guest is default value

# get(): To get the value associated with the key
    
# print(d.keys())
# print(d.values())
# print(d.items())

# Write a program to take dictionary from the keyboard and print the sum of values
# d=eval(input())
# sum=0
# for i in d.values():
#     sum+=i
# print(sum)

# Remove key value pairs from a dictionary
# del d[200]
# d = {'a': 1, 'b': 2, 'c': 3}
# del d['b']
# print(d)

# Ckeck if a key exists in a dictionary
# get()
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# value = my_dict.get('d')
# if value is not None:
#     print("Key Exists")
# else:
#     print("Not Exists")

# Reverse a dictionary
# d = {'a': 1, 'b': 2, 'c': 3}
# reverse_dict = {v: k for k, v in d.items()}
# print(reverse_dict)
#
# for k,v in d.items():
#     res[v]=kv

# Remove all occurences of an element in a list
# l=[1,2,3,4,2,6,2,8]
# nl=[]
# for i in l:
#     if i not in nl:
#         nl.append(i)
# print(nl)

# l=[1,1,1,2,2,2,3,3,3]
# ans=[]
# element=2
# for i in l:
#     if i not in element:
#         ans.append(i)
# print(ans)

# TCS launchpad
# https://infytq.onwingspan.com/web/ Infosys
# https://www.codility.com/ Wipro
# https://wheebox.com/ https://assessment.aon.com/en-us/prepare-your-assessment https://mettl.com/programming-skills-test/?ads_cmpid=17590013514&ads_adid=&ads_targetid=&ads_loc_intrst=&ads_loc_physcl=9199162&ads_network=x&ads_gclid=CjwKCAiAm-67BhBlEiwAEVftNhqJUWSF7FI46KBR613tcDu-PgZQpEs83nX9iwXhBfPFKWdUlxiF_RoCz-gQAvD_BwE&ads_creative=&ads_kw_term=&ads_adposition=&utm_source=adwords&utm_medium=ppc&utm_campaign=17590013514&gclid=CjwKCAiAm-67BhBlEiwAEVftNhqJUWSF7FI46KBR613tcDu-PgZQpEs83nX9iwXhBfPFKWdUlxiF_RoCz-gQAvD_BwE&gad_source=1 Accenture
# Leetcode
# Hackerank
# Codechef
# TCS NQT
# Courses: https://cognitiveclass.ai/courses

#x,y,z=map(int,input().split())
#z=list(map(int,input().split()))

# Functions
# Pre Defined
# User Defined

# def add(a,b):
#     sum=a+b
#     return sum
# a=int(input())
# b=int(input())
# print(add(a,b))

# Python can return multiple values in function
# In Java, C++, we can use pointer to return multiple values in function

# def fun(a,b):
#     sum=a+b
#     dif=a-b
#     mul=a*b
#     return sum,dif,mul
# a=int(input())
# b=int(input())
# print(fun(a,b))

# sum,dif,mul=fun(a,b)
# print(sum)
# print(dif)
# print(mul)

# Arguments

# 1. Positional Argument
# def add(x,y):
#     sum=x+y
#     print(x)
#     print(y)
#     print(sum)
# add(1,2)

# 2. Keyword Argument
# add(x=1,y=2)

# 3. Default Argument
# def add(x,y=2):
#     sum=x+y
#     print(x)
#     print(y)
#     print(sum)
# add(1)

# 4. Variable Length Argument
# def sum(*n):
#     total=0
#     for i in n:
#         total+=i
#     return total
# print(sum(1,2,3,4,5))
# import sys
# def add(a,b):
#     c=a+b
#     return c
# def sub(a,b):
#     c=a-b
#     return c
# def mul(a,b):
#     c=a*b
#     return c
# def div(a,b):
#     c=a/b
#     return c

# while True:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     choice=int(input())
#     a=int(input())
#     b=int(input())
#     if choice==1:
#         print(add(a,b))
#     elif choice==2:
#         print(sub(a,b))
#     elif choice==3:
#         print(mul(a,b))
#     elif choice==4:
#         print(div(a,b))
#     elif choice==5:
#         sys.exit(0)
#     else:
#         print("Invalid Choice")

# Palindrome String
# Input: "A man, a plan, a canal: Panama"

# import string
# input = "A man, a plan, a canal: Panama"
# input = input.lower()
# # Remove spaces and punctuation using str.translate()
# translator = str.maketrans('', '', string.punctuation + ' ')
# input = input.translate(translator)
# # Check if the string is a palindrome
# revString = input[::-1]
# print(input == revString)

# t=int(input())
# for i in range(t):
#     a,b,c=map(int,input().split())
#     list=[a,b,c]
#     list.sort()
#     print(list[1])

# arr=list(map(int,input().strip('[]').split(',')))
# arr=eval(input())
# print(arr)

########



#########

# 11th January
# data="Learning python is very easy from Ashish Sir"
# f=open("myfile.txt", 'w')
# f.write(data)

# with open("myfile.txt",'r+') as f:
#     fileData=f.read()
#     print(fileData)
#     print("Current Cursor Position is ",f.tell())
#     f.seek(15)
#     print("Current Cursor Position is ",f.tell())
#     f.write("-Java-")

# # WAP to print number of lines, words, characters present in file
# import os,sys
# fname=input("Enter file name:")
# if os.path.isfile(fname):
#     print("File exists:",fname)
#     f=open(fname,'r')
# else:
#     print("File is not exist: ",fname)
#     sys.exit(0)

# lcount=wcount=ccount=0
# for line in f:
#     lcount=lcount+1
#     ccount=ccount+len(line)
#     words=line.split()
#     wcount=wcount+len(words)

# print("Total lines: ",lcount)
# print("Total words: ",wcount)
# print("Total Characters: ",ccount)

# Read and write new image
# f1=open("alia.jpg","rb")
# f2=open("newalia.jpg","wb")
# bytes=f1.read()
# f2.write(bytes)
# print(bytes)
# print("New image is available")

# Writing data to .csv file

# import csv
# with open("emp.csv", "w", newline='') as f:
#     w=csv.write(f)
#     w.writerow(["ENO","ENAME","ESALARY","EADDR"])
#     n=int(input("Enter number of employees: "))
#     for i in range(n):
#         eno=input("Enter employee no: ")
#         ename=input("Enter employees name: ")
#         esal=input("Enter employees salary: ")
#         eaddr=input("Enter employee address: ")
#         w.writerow([eno,ename,esal,eaddr])

# print("Data inserted successfully!")

# # Reading data from .csv file
# import csv
# f=open("emp.csv", "r")
# r=csv.reader(f)
# data=list(r)
# print(data)
# for line in data:
#     for word in line:
#         print(word,"\t")

# Array Rotation
# arr=[1,2,3,4,5]
# ans=[]
# k=2
# p=0
# for i in range(len(arr)):
#     p=i-k
#     ans.append(arr[p])
# print(ans)

#
# arr=[1,2,3,4,5]
# k=2
# for k in range(k):
#     temp=arr[-1]
#     for i in range(len(arr)-1,-1,-1):
#         arr[i]=arr[i-1]
#     arr[0]=temp
# print(arr)

# import os,sys
# print(dir(os))
# print(dir(sys))
# print(os.getcwd()) #Current working directory
# print(os.listdir()) #Print all the folders and files in the folder

## Merge two sorted lists
# def mergeAndSort(a,b):
#     ans=[]
#     i=0
#     j=0
#     while i<len(a) and j<len(b):
#         if a[i]<b[j]:
#             ans.append(a[i])
#             i+=1
#         else:
#             ans.append(b[j])
#             j+=1
#     while i < len(a):
#         ans.append(a[i])
#         i += 1
#     while j < len(b):
#         ans.append(b[j])
#         j += 1
#     return ans
# list1=[1,3,5]
# list2=[2,4,6]
# print(mergeAndSort(list1,list2))

# Pattern Find
# import re
# count=0
# pattern=re.compile("ab")
# matcher=pattern.finditer("ababababab")
# for match in matcher:
#     count+=1
#     print(match.start(), '...', match.end(), '...', match.group())
# print("Total no of group occurences: ",count)

# Character Matcher
# import re
# # x="[abc]"
# # x="^abc"
# # x="[a-z]"
# # x="[0-9]"
# # x="[a-zA-Z0-9]"
# x="\\s"
# x="\s"
# x="\d"
# x="\D"
# x="\w"
# x="\W"
# x-="."
# matcher=re.finditer(x,"a7bD2@k2D8z")
# print(matcher)
# for match in matcher:
#     print(match.start(), '...', match.group())

# Oracle ocgp scgp for Java

# match() function
# import re
# str=input("Enter any string: ")
# m=re.match(str,abc@xyz_pqr)

# split()
# import re
# list=re.split(",","a,b,c,d,e,f")
# print(list)
# for x in list:
#     print(x)

# Mobile number validation
# import re
# number=input("Enter mobile number")
# match=re.fullmatch("[7-9]\\d{9}",number)
# if match!=None:
#     print(number,"is valid mobile number")
# else:
#     print(number," is not valid mobile number")

# Check if the number is armstrong or not
# no=int(input())
# sum=0
# nsave=no
# while n>0:
#     rem=no%10
#     sum=sum+(rem**3)
#     no=no//10
# while no>0:
#     no=no//10
#     count=count+1
# no=nsave
# while no>0:
#     rem=no%10

# if sum==nsave:
#     print(nsave, " is armstrong")
# else:
#     print(nsave, " is not armstrong")

# Check armstrong 1-1000
# for i in range(1,10001):
#     no=i
#     sum=0
#     nsave=no
#     count=0
#     while no>0:
#         no=no//10
#         count=count+1
#     no=nsave

# Print fibonacci series
n=int(input())
f0=0
f1=1
print(f0,"\t",f1,end="")
for i in range(3,n+1):
    f2=f0+f1
    print("\t", f2, end="")
    f0=f1
    f1=f2

# Find the sum of following series
# sum=1+x/1+x^2/2+x^3/3+..+x^n/n

# sum=1+x/1! + x^2/2! + x^3/3! + .. +x^n/n!

# n=int(input())
# x=int(input())
# sum=1
# for i in range(1,n+1):
#     no=i
#     fact=1
#     while no>0:
#         sum=sum+(x**i)/i
# print("sum= ",sum)

# Find missing no. in an array
# Input=[1,2,3,4,5,7,8,9]
# Output=6
arr=[]
for i in range(len(arr)):
    







