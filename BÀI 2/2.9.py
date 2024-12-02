print("luong dinh anh")
print("mssv235752021610008")
str=input("Enter a sting:")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] +=1
    else:
        dict[n] = 1
print (dict) 
