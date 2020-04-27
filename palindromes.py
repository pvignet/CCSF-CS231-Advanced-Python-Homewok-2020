#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
'''
-Assignement: . Write a program only one statement long (it can span multiple lines) 
that prints the number of palindromes in /users/abrick/resources/english 
-Explanation:if more than one statement was authorized I would do it as below:
pth ='/users/abrick/resources/english'
ct=0
t=0
fl=open(pth,"r") #read the file
lines=fl.readlines() # make it a []
for ln in lines: #loop for each line
    for word in ln.split(): split word in list
        t =t +1  #count number  of words
        if word == (word[::-1]):  #check if it is a palydrome
            ct = ct +1  #count number of palydromes

print("{} palindromes found ".format(ct)) #pring the number of palydromes
but to reduce the number of statements I will
a) suppress the variables such as pthn ,fl,etc.
replacing them with their value
b) use comprehension to flatten the for loops
a+b make  one statement as requested for the home work
as shown below
'''
print("{} palindromes found ".format(len([ ln[::-1].strip('\n')  for  ln in open('/users/abrick/resources/english',"r").readlines()  if ln.strip('\n')  == (ln.strip('\n')[::-1]) ])))
