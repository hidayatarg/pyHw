# Question 1
print("Kullanıcı tarafıdan girilen 20 sayini ortalamasi, en buyu, en kucugu bulan vek ekran yazdiran programi")

Number = []
Total = 0
for i in range(20):
    x = int(input("enter no.{0}: ".format(i + 1)))
    Number.insert(i, x)
    Total = Total + int(x)
    i += 1

maxValue = max(Number)
minValue = max(Number)
print("GIRILEN SAYILAR MAX:{0} ".format(maxValue))
print("GIRILEN SAYILAR MIN:{0} ".format(minValue))
print("GIRILEN SAYILAR:{0} ".format(Number))
print("SAYILARIN TOPLAM:{0:.2f} ".format(Total))
print("GİRDİĞİNİZ SAYILARIN ORTALMASI:{0:.2f} ".format(Total / len(Number)))


