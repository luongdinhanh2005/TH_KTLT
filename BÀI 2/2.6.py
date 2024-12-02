print("luong dinh anh")
print("mssv235752021610008")
n = int (input("Enter a Number--->"));
j=[]
for i in range (2000,3021):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print (','.join(j))
