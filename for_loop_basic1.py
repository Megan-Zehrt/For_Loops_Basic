#Basic - Print all integers from 0 to 150.

def from_0_to_150(count):
    while count!=150:
      print(count)
      count=count+1

from_0_to_150(0)
        
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000

def multi_of_five(times):
    while times != 1000 :
     print(times)
     times=times+5

multi_of_five(0)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

def Coding_Dojo(firstNum, lastNum):
    for i in range(firstNum, lastNum):
        if i % 5 == 0:
            print ("Coding")
        if i % 10 == 0:
            print ("Coding Dojo")
        else: 
            print(i)

Coding_Dojo(1, 100)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

def that_suckers_huge(x):
    final_sum = 0
    for i in range(x + 1):
        final_sum += i
    print(final_sum)

that_suckers_huge(500000)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

def mult_fours(Num, divs):
    for i in range(Num -1):
        if i % divs == 0:
            print(i)

mult_fours(2018, -4)

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flexible_counter(lowNum, highNum, mult):
    for i in range(lowNum, highNum + 1):
        if i % mult == 0:
            print(i)

flexible_counter(5, 100, 3)