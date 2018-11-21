print("3 Tv Programs")

# Problem Summary
# input: user => 3 tv program names, 7 days ratings
# Every Program rating average
# Output => High Rating app print to screen


Programs = []
ProgramOneRatings = []
ProgramTwoRatings = []
ProgramThreeRatings = []

TotalOfProgramOne = 0
TotalOfProgramTwo = 0
TotalOfProgramThree = 0
for i in range(3):
    x = input("enter {0}.Program: ".format(i + 1))
    Programs.insert(i, x)
    i += 1

j = 0

while j < 7:
    y = int(input("enter {0}. Program one : ".format(j + 1)))
    ProgramOneRatings.insert(j, y)
    TotalOfProgramOne = y + TotalOfProgramOne
    j += 1
j = 0
while j < 7:
    y = int(input("enter {0}. Program two : ".format(j + 1)))
    ProgramTwoRatings.insert(j, y)
    TotalOfProgramTwo = y + TotalOfProgramTwo
    j += 1

j = 0
while j < 7:
    y = int(input("enter {0}. Program three : ".format(j + 1)))
    ProgramThreeRatings.insert(j, y)
    TotalOfProgramThree = y + TotalOfProgramThree
    j += 1

print("GIRILEN PROGRAMLARIN ADLAR:{0} ".format(Programs))

avgOfThirdProgram = TotalOfProgramThree / len(ProgramThreeRatings)
avgOfSecondProgram = TotalOfProgramTwo / len(ProgramTwoRatings)
avgOfFirstProgram = TotalOfProgramOne / len(ProgramOneRatings)

if (avgOfFirstProgram > avgOfSecondProgram and avgOfFirstProgram > avgOfThirdProgram):
    print("A is bigger")
elif (avgOfSecondProgram > avgOfFirstProgram and avgOfSecondProgram > avgOfThirdProgram):
    print("B is bigger")
else:
    print("C is bigger")
