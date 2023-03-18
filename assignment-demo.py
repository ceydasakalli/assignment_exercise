x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# kullanıcıdan aldığınız 2 sayının çarpımını ile x,y,z toplamının farkı nedir?
a = int(input('number 1:'))
b = int(input('number 2:'))

result = (a*b) - (x+y+z)
print(result)

# y nin x e kalansız bölümünü hesaplayınız
result = y // x

# (x,y,z) toplamının mod 3 ü nedir

total = x+y+z
result = total%3

# y'nin x. kuvvetini hesaplayınız.
result = y**x

# x, *y, z = numbers işlemine göre z'nin küpü kaçtır
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
result ** 3
print(y)

# x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
result = y[0] + y[1] + y[2]
print(result) 
