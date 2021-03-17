# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 08:45:41 2021

@author: ABHISHEK
"""


import random
list1=[1,2,3,4,5,6]
p=0;
while 1:
    computer=random.randint(0, 7)
    player=int(input("Enter the score "))
    if player==computer:
        print("Out");
        break
    elif(player!=computer):
        p=p+player;
print("final score=",p)
        
    