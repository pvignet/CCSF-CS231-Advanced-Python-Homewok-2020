# CS231 Final Exam. Send in a plain text file that describes how and why
# this program produces the output that it does.
'''
Summary:
#this script prints on the same line 3 blocks of 21 characters, each block has blanks and  $ characters.
#the first block & last block have only one $ printed
#the middle block may have one or more $ ,all in grouped together
#the arragment of blanks & $ of each block is given by the function reify()
# by line : ' '*outs+'$'*ins+' '*(frame-outs-ins)
#where frame =21 , outs= number leading blank &  (frame-out-ins) are the trailing blanks
#The calculation of the value outs & ins, for each block are calcuated by 3 functions:
#function politeness() gives the outs & ins(=1) for the 1st block.
#politeness() uses the client API address in the log '/etc/httpd/logs/ssl_error_log'
#to generate the values of outs
#function whimsy() calculates the outs & ins values of the midlle block
#whimsy() uses :
- a)a combination of sampler()& lambda bound to provide a value for variable heft
which  will be the value of ins number of $
-b)a combination of heft & lambda trigo to provide a value for outs the number of leading blanks
#function obligation() calculates the outs & ins(=1) of the last block
#obligation() uses a combination of bytecode opcode &oparg to provide a value for outs number of leading blanks
# sequence :
#the script starts with top() , top() invokes combine(),
#combine () invokes  politeness(), whimsy() &obligations () to assemble the 3 blocks in one line using reify()
#after 189 lines the script stops
'''
#below are mode detail comments for scripts lines
from math import pi, sin as sin #sin returns the sine of value
from time import perf_counter as pc #pc returns float values in seconds of a time between sleep time
from os.path import abspath as path #path returns a normalized absolutized version of the pathname path
from re import split, findall as pickup #pick up returns a list of all matches when used with log.read
#split specify the regular expression pattern in the first parameter and the target character string in the second parameter
from sys import argv #argv list of arguments
from dis import Bytecode as ops #ops has instructions. Each instruction has 2 bytes: opcode & oparg
from subprocess import run, PIPE as p # passed to stoud that point to stream reader instances
# define global variables below:
#define global variables and  assign value: squash=2,fill=9,frame=21
#print is a builtin_function
squash, fill, frame, put = 2, 9, 21, print
#define lambda functions:
#forgive returns an integer if it is one otherwise give 0, it used by obligations()
#trigo  uses fill =9 , sin(n/fill) has max value of 1,  1+sin(n/9) has max value of 2
#trigo returns a value <=10 , it used by whimsy()
#bound returns the min between 10, or max of (squash=2 or n)
#bound returns a value <=10, it is used by whimsy()
forgive = lambda n: int(n) if n else 0
trigo = lambda n: 5*(1+sin(n/fill))
bound = lambda n: min(10,max(squash,n))

def sampler():
    # pc is a perf_counter multiply by fill=9 and at the power of fill=9
    # the result is modulo fill=9 so the return int is >0 & <9
    #sampler() is used by whimsy()
    return int(pc()*fill**fill)%fill

def whimsy(): #to calculate ths outs $ ins of the middle block
 n, heft = sampler()*fill, fill
 # n has the value of sampler()*fill, heft has value of fill=9
 # max of n will be 9*9=81, max of heft is 10
 while True:
  heft = bound(heft+sampler()-fill/squash) #heft is now changed using the lambda bound function & sampler()
  #yield passes a tuple with 2 values they are the outs & ins for reify()
  #the 1st one is for the outs number of leading blanks
  #the fist value is a combination of squask=2, trigo(n) , trigo(n) is lambda function & heft
  #the 2nd value is int( heft) number of $
  yield (int(squash+trigo(n)-heft/squash),int(heft))
  n += 1  # n is incremeented by one for each line

def politeness(): #to calculate the outs of the 1st block
 import re  # use regex library
 log = open('/etc/httpd/logs/ssl_error_log')
 # yield returns a tuple made of 2 values
 # the 1st value is modulo 21  of  the API address of the line of the log changed into  an integer
 # the 1st value of the tuple is the numberof blanks outs
 # the 2nd value is the number of ins =1 , the printed $
 yield from ((int(''.join(split(r'\W',e)[1:]))%frame,1)
  for e in pickup(r'client [\d.]+',log.read())) #pickup provides a  list of all matches  for pattern [client API address]

def obligations(): #to calculate the outs of the 1st block
 while True:
  # yield returns a tuple that of a 2 values
  #the 1st is calculate using the (opcode value-forgive(oparg value))%9
  #which most of time (opcode value-(oparg value))%9
  #if (oparg value)is not an int lambda function makes it = 0
  #the 1st value is the number of preceding blanks
  #the 2nd value is the number of printed $ which is always 1
  for op in ops(open(path(argv[0])).read()):
   yield ((op.opcode-forgive(op.arg))%fill,1)

def reify(job):
 def junk(sample):  #the return a block of 21 characters
   #outs is the number of preceeding blanks
   #ins is the number of $
   #outs & ins are passed by politness() or whimsy() or obligations()
  (outs, ins) = job(sample)
  return ' '*outs+'$'*ins+' '*(frame-outs-ins)
 return junk

def combine():  # put the 3 blocks together in  one line of 21*3 characters
 collect = reify(next)
 group = (politeness(),whimsy(),obligations()) #collect the yields of the 3 functions in one tuple of tuples
 while True:
  yield (collect(measure) for measure in group) # yields the result of the 3 functions while true

def top(): # starting function
 machine = combine() # generator
 for n in range(fill*frame): #for n in (9*21=189) ,189 lines
  put(*next(machine)) #* means without parentheses

if __name__=='__main__':
 top() #invoke top()
else:
 print(run(('/usr/bin/uname','-a'), stdout=p).stdout.decode()) # used in case the wrong path is given


