import math

# e^1    >> math.exp(y)
x = 0
y = 0
Total = 0
while (x < 100):
    y = 0
    while (y < 100):
        if (x > y):
            Total = (x * math.exp(y))

        elif (x < y):
            Total = (y * math.sin(x))

        else:
            if x != 0:
                Total = (x / (math.log(y + 1)))
                print(Total)
            print("cannot divide by zero")
        y += 1
        print("Y= {0} ".format(y))
    x += 1
    print("X= {0} ".format(x))

print(Total)
