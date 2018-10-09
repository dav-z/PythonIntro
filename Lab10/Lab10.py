## David Zheng
## Lab 10

import datetime as dt
import os

class MyApp():

    def __init__(self, title, author, description, directions):
        self.title = title
        self.author = author
        self.description = description
        self.directions = directions
        self.created = dt.date(2018,4,25)
        
    def start(self):
        print()
        print('%s by %s  %s' % ( self.title, self.author, self. created ) )
        print(self.description)
        print(self.directions)
        print()

######################################
description= "Description: Should you buy Kanye's or Taylor's new album?"
directions= """
Directions:
Answer the questions below.
"""
App = MyApp("The Questionaire", "David", description, directions)

App.start()

valA = 0
valB = 0
valC = 0
fh = open('Questions-tuh94204.txt')
questions = fh.readlines()
n = 0
for i in range(5):
    needAnswer = True
    while needAnswer:
        print(questions[n])
        print(questions[n+1])
        answer = input('> ')
        if answer == 'A' or answer == 'a':
            valA = valA + 1
            needAnswer = False
        if answer == 'B' or answer == 'b':
            valB = valB + 1
            needAnswer = False
        if answer == 'C' or answer == 'c':
            valC = valC + 1
            needAnswer = False
    n = n + 2
fh.close()
print("It looks like you prefer:")
if valA > valB:
    print("Kanye West. Buy his album.")
if valA < valB:
    print("Taylor Swift. Buy her album.")
if valC > valA and valC > valB and valA < 1 and valB < 1:
    print("Neither. Don't buy either album.")
elif valA == valB:
    print("Both. Buy both albums.")
