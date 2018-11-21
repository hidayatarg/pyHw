# Question 1

# Girilen Sayilari tutacagiz
Number = []
# Sayilarin Toplami tutacagiz
Total = 0
for i in range(20):
    x = int(input("{0}.SAYI GIRINIZ: ".format(i + 1)))
    Number.insert(i, x)
    Total = Total + int(x)
    i += 1

maxValue = max(Number)
minValue = min(Number)
print("GIRILEN SAYILARIN BUYUGU= {0} ".format(maxValue))
print("GIRILEN SAYILARIN KUCUGU= {0} ".format(minValue))
print("GIRILEN SAYILARI= {0} ".format(Number))
print("GIRILEN SAYILARIN TOPLAM= {0:.2f} ".format(Total))
print("GIRILEN SAYILARIN ORTALMASI= {0:.2f} ".format(Total / len(Number)))


