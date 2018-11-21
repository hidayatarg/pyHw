# Question 2
import math
# e^1    >> math.exp(y)
x = 0
y = 0
# Toplama Tutacagiz
Total = 0
# X Icin Dongu
while (x < 100):
    # Her x icin dongu tamamlayinca y sifirlariz
    y = 0
    # Y Icin Dongu
    while (y < 100):
        if (x > y):
            Total = (x * math.exp(y))

        elif (x < y):
            Total = (y * math.sin(x))

        else:
            if x != 0:
                Total = (x / (math.log(y + 1)))
        y += 1
    x += 1

print(Total)
