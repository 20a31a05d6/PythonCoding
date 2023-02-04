a=int(input("enter:"))
arr=[]
for i in range(a):
    action=input().split()
    if action[0]=="add":
        arr.append(int(a[1]))
    elif a[0]=="insert":
        ele=int(a[1])
        ind=int(a[2])
        arr.insert(ind,ele)
    elif a[0]=="remove":
        ele=int(a[1])
        if ele in arr:
            arr.remove(ele)
    elif a[0]=="pop":
        if len(arr)>0:
            arr.pop()
    elif a[0]=="print":
        if len(arr)!=0:
            print(*arr)


