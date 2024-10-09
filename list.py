list1=[1,2,"python","program",12.7]
print(list1)
print(type(list1))

for i in list1:
    print(i)
    
#concatenate
li1=["vidhi","nidhi","shruti","puja"]
li2=["aditi","niya","priti"]
print(li1+li2)

#slicing
print(li1[0])
print(li1[1])
print(li1[2])
print(li1[3])

print(li1[-1])
print(li1[-2])
print(li1[-3])
print(li1[-4])

#append
l=[]
n=int (input("enter the no of element in list: "))
for i in range(0,n):
    l.append(input("enter no"))
    
for i in l:
    print(i,end=" ")    

list6=[12,14,16,18,20]
la = list6 * 2
print(la)

#insert
num=["mango","banana","chikku","peru","gava"]
num.insert(3,3)
print(num)


nob=[12,13,14,15,16,17]

nob.insert(4,2)
print(nob)

#sum
print("sum of all elements",sum(nob))


# length
n1=[1,2,22,23,12,11,23,34,90,45,67,78,69]
print(len(n1))

#index
print(n1.index(22))
print(n1.index(23))
print(n1.index(90))
print(n1.index(69))

#count
elem = [1,1,1,2,2,3,4,5,1,2,4,5,6,7,7,8,9,2]
print(elem.count(1))
print(elem.count(2))
print(elem.count(3))
print(elem.count(4))
print(elem.count(8))
print(elem.count(9))

#delete
listp=["vaishnavi","nukul","radha","ayushi"]

del listp[0]
print(listp)

del listp[2]
print(listp)

#remove
plist=["vaishnavi","nukul","radha","ayushi","pruhvi","kajal","suhana","nitya"]
plist.remove("suhana")
print(plist)



