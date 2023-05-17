from fractions import Fraction


x1 = int(input("x1 değerini giriniz: "))
y1 = int(input("y1 değerini giriniz: "))

x2 = int(input("x2 değerini giriniz: "))
y2 = int(input("y2 değerini giriniz: "))

denklem1 = Fraction((y1),(y2-y1))
denklem2 = Fraction((x1),(x2-x1))

denklem3 = denklem1-denklem2

print(f"Denklem3: {denklem3}")
print(f"denklem = (y/{y2-y1})-(x/{x2-x1})= {denklem3} ")

