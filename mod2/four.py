# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:03:17 2020

@author: Dell
"""


myList=[0,6,2,7,8,9]
print(myList)
#print(myList[1])
"""output:6"""

#print(myList[0])
"""output is:0"""

#print(myList[7])
"""list index out of range.
because the list have only 6 elements.the code is says to display 7th element"""

#print(myList[4.0])
"""list indices must be integers or slices, not float.
the reason of these error is our list is in integers.and we enter a float value"""

#print(myList[-3])
"""output is 7"""

#print(myList[-1])
"""output is -3"""

#print(myList[2:6])
"""output is [2,7,8,9]"""

#print(myList[4:5])
"""output is [8]"""

#print(myList[6:1000])
"""output is []"""


#print(myList[2:4][1])
"""output is [35]"""

#print(myList[0:3:2])
"""output is [0,2]
 skip 2 values .but 0 is the first value.it should be print"""
 
 
#print(myList[1::3])
"""output is [6,8]"""


#print(myList[::])
"""output is [0,6,2,7,8,9]""" 

#print(myList[2::2])
"""output is [2,8]"""

#print(myList[::3])
"""output is [o,7]"""

#print(myList[1::2])
"""output is [6,7,9]"""

#print(myList[::4])

#print(myList[::2])

#print(myList[:]) 

#print(myList[::-1][3:5])

#print(myList[::-1])


#print(myList[::-1])

#print(myList[1:5][2:3][1])
"""output is:list index out of range.
      """
      
#print(myList[::1])
     
#print(myList[::1])