import array as ar

a=ar.array('i',[1,2,3])
for i in range(0,3):
    print (a[i],end=" ")
print()

b=ar.array('i',[10,14,28,31,38,54,58])
for i in range(0,7):
    print (b[i],end=" ")
print()


import array as arr
a = arr.array('i', [1, 2, 3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
a.insert(1, 4)
print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()
b.append(4.4)
print("Array after insertion : ", end=" ")
for i in (b):
    print(i, end=" ")
print()

