d1=input("data1: ")
d2=input("data2: ")
l1=d1.split(",")
l2=d2.split(",")
mydict=dict(zip(list1,list2))
print("list1:",l1)
print("list2:",l2)
print("dictionary:",sorted(mydict.items()))