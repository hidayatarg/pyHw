# Question 3

# Progarmlarin Ismimleri tutacagiz
Programs = []
# Birinci Programin Ratingler icin
ProgramOneRatings = []
# Ikinci Programin Ratingler icin
ProgramTwoRatings = []
# Ucuncu Programin Ratingler icin
ProgramThreeRatings = []

TotalOfProgramOne = 0
TotalOfProgramTwo = 0
TotalOfProgramThree = 0
for i in range(3):
    x = input("{0}.PROGRAMI GIRINIZ: ".format(i + 1))
    Programs.insert(i, x)
    i += 1

j = 0
while j < 7:
    y = int(input("1.PROGRAMIN {0}.GUN RATING GIRINIZ: ".format(j + 1)))
    ProgramOneRatings.insert(j, y)
    TotalOfProgramOne = y + TotalOfProgramOne
    j += 1

j = 0
while j < 7:
    y = int(input("2.PROGRAMIN {0}.GUN RATING GIRINIZ: ".format(j + 1)))
    ProgramTwoRatings.insert(j, y)
    TotalOfProgramTwo = y + TotalOfProgramTwo
    j += 1

j = 0
while j < 7:
    y = int(input("3.PROGRAMIN {0}.GUN RATING GIRINIZ: : ".format(j + 1)))
    ProgramThreeRatings.insert(j, y)
    TotalOfProgramThree = y + TotalOfProgramThree
    j += 1

# print("GIRILEN PROGRAMLARIN ADLAR:{0} ".format(Programs))

avgOfThirdProgram = TotalOfProgramThree / len(ProgramThreeRatings)
avgOfSecondProgram = TotalOfProgramTwo / len(ProgramTwoRatings)
avgOfFirstProgram = TotalOfProgramOne / len(ProgramOneRatings)

# Eger birinci programin rating ortalamasi baskalardan buyukse
if (avgOfFirstProgram > avgOfSecondProgram and avgOfFirstProgram > avgOfThirdProgram):
    print("{0} Program".format(Programs[0]))
# Eger ikinci programin rating ortalamasi baskalardan buyukse
elif (avgOfSecondProgram > avgOfFirstProgram and avgOfSecondProgram > avgOfThirdProgram):
    print("{0} Program".format(Programs[1]))
# Son ihtimal ucuncu program olur
else:
    print("{0} Program".format(Programs[2]))
