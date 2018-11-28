# Question 4


#Generate 4 digit random number

import random

#a = random.randint(1000, 9999)
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
d = random.randint(0, 9)
#print(a, b, c, d)

randomList = [a, b, c, d]
print(randomList)
print(randomList[0])

Number = []

for i in range(4):
    x = int(input("enter no.{0}: ".format(i + 1)))
    Number.insert(i, x)
    i += 1

print(Number)
j = 0
z = 0
digitLocation = 0
while j<10:
    for i in range(3):
        if Number[i] == randomList[z]:
            if digitLocation == z:
                print("+")
            else:
                print('-')

        elif Number[i] == randomList[z+1]:
            if digitLocation == z+1:
                print("+")
            else:
                print('-')

        elif Number[i] == randomList[z+2]:
            if digitLocation == z+2:
                print("+")
            else:
                print('-')

        elif Number[i] == randomList[z+3]:
            if digitLocation == z+3:
                print("+")
            else:
                print('-')

        else:
            print("0")
        i += 1
        digitLocation += 1
        y = 0
        for i in range(3):
            if(Number[i]==randomList[i]):
                if(y==4):
                    print("You win the game")
                y += 1
                
    j += 1
    print("You have " + j + " chances to play")


#Allow user to guess the number


#If the user guess match the target number and the location

# For each correct print a +  if match but different location -

# if not match and (not  location and value it is blank)


# 10 chances if guess right winning message or print the tries
