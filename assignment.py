x = 5
y = 10
z = 20

x, y, z = 5, 10, 20

x,y = y, x    #x ile y nin değerlerini değiştirmiş olduk.

# x = x + 5     x+=5   
# x = x - 5     x-=5    
# x = x * 5     x*=5
# x = x % 5     x%=5
# x = x // 5    x//=5
# y = y**5      y**5

values = 1, 2, 3

print(values)
print(type(values))

x, y, z = values
# örneğin x, y, z ; 3 ayrı değer olduğu için valuesda 3 tane değer tanımlanmış olmalı yoksa hata alırız. ama örneğin
# values = 1, 2, 3, 4, 5 ama x, y, z olarak 3 değer var ise örneğin z nin üstüne bir yıldız koyarak x = 1 , y = 2, ama z = 3,4,5 değerini alır.

# values = x,y, z[0] örneğin z için 3 değerini verir.

print(x, y, z)