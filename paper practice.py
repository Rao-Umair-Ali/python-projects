##================================1=========================
##name=input("What is your name ")
##print("Your name is :",name)

##================================2=========================
##Number1=int(input("give me a number : "))
##Number2=int(input("give me another number : "))
##print(Number1+Number2)

##================================3=========================
##Number_of_days=int(input("Give me number of days :"))
##hours=Number_of_days*24
##minutes=hours*60
##seconds=minutes*60
##print("Total hours:",hours,"\n"+"Total minutes:",minutes,"\n"+"Total seconds:",seconds)

##================================4=========================
##Number1=int(input("give me a number : "))
##Number2=int(input("give me another number : "))
##Number3=int(input("give me another number : "))
##print((Number1+Number2)*Number3)

##================================5=========================
##Number1=int(input("give me a number : "))
##if Number1>=10 and Number1<=20:
##    print("Thank you :)")
##else:
##    print("Incorrect Answer :(")

##================================6=========================
##age=int(input("give me your age :"))
##if age==18:
##    print("You can vote")
##elif age==17:
##    print("You can learn to drive ")
##elif age==16:
##    print("You can buy a lottery")
##elif age<16:
##    print("You can go trick or treating ")
##elif age>18:
##    print("Give me age under 19")
##else:
##    print("give me age in numeric")

##================================7=========================
##num=int(input("give me your number:"))
##if num==1:
##    print("Thank you ")
##elif num==2:
##    print("Well done ")
##elif num==3:
##    print("Correct")
##else:
##    print("give me Number from 1 to 3 ")

##================================8=========================
##num=int(input("give me number for table :"))
##i=1
##while i<11:
##    print(num,"x",i,"=",num*i)
##    i+=1

##================================8=========================

##================================8=========================
##num=int(input("give me number:"))
##i=50
##while i!=num:
##    ans=i-1
##    print(ans)
##    i-=1

##================================9=========================
##fp="C:\\Users\\RUA\\Desktop\\python\\d.csv"
##f=open(fp,"r")
##f.readline()
##dic={}
##i=0
##line=f.readline()
##while line:
##    char=line.split(",")
##    emp=char[6]
##    if emp in dic:
##        dic[emp]+=1
##    else:
##        dic[emp]=1
##    line=f.readline()
##f.close()
##i=0
##employee=list(dic.keys())
##employee.sort()
##while i<len(employee):
##    empl=employee[i]
##    c=dic[empl]
##    print(empl,c)
##    i+=1
##    
##================================10=========================
##fp="C:\\Users\\RUA\\Desktop\\python\\d.csv"
##f=open(fp,"r")
##f.readline()
##dic={}
##line=f.readline()
##while line:
##    data=line.split(",")
##    emp=data[6]
##    unit_price=int(data[4])
##    amount=int(data[5])
##    revenue=amount*unit_price
##    if emp in dic:
##        dic[emp]+=revenue
##    else:
##        dic[emp]=revenue
##    line=f.readline()
##f.close()
##empId=list(dic.keys())
##empId.sort()
##i=0
##while i<len(empId):
##    empl=empId[i]
##    count=dic[empl]
##    print(empl,count)
##    i+=1
##    
##================================11=========================
##y=[]
##while True:
##    d=input("give me a number for making list")
##    if d=="":
##        break
##    else:
##        num=int(d)
##        y.append(num)
##print("your given list ",y)
##i=0
##n=len(y)
##while i<n:
##    smallNumber=i
##    j=i+1
##    while j<n:
##        if y[j]<y[smallNumber]:
##            smallNumber=j
##        j+=1
##    y[i],y[smallNumber]=y[smallNumber],y[i]
##    i+=1
##print("Sorted list ",y)
##    
##================================12========================
    
    


##
##def merge(list1):
##    if len(list1) > 1:
##        mid = len(list1) // 2
##        left = list1[:mid]
##        right = list1[mid:]
##
##        merge(left)
##        merge(right)
##
##        i = j = k = 0
##
##        while i < len(left) and j < len(right):
##            if left[i] < right[j]:
##                list1[k] = left[i]
##                i += 1
##            else:
##                list1[k] = right[j]
##                j += 1
##            k += 1
##
##        while i < len(left):
##            list1[k] = left[i]
##            i += 1
##            k += 1
##
##        while j < len(right):
##            list1[k] = right[j]
##            j += 1
##            k += 1
##
##list1 = [8, 5, 4, 6, 2, 1, 7, 9]
##merge(list1)
##print(list1)
##++++++++++++++++++++++++++++++++++================================
##R=[1,2,3,4,1]
##i=0
##while i<len(R):
##    R[i]=0
##    i+=1
##print(R)
##R = [1, 2, 3, 4, 1]
##for i in R:
##    print(R)
##    R[i] = 0
##    
##    
##================================13========================
##a=[[2,4,4],
##   [1,5,1],
##   [3,5,3]]
##
##b=[[2,0],
##   [0,5],
##   [3,0]]
##
##c=[[0,0],
##   [0,0],
##   [0,0]]
##for i in range(0,len(a)):
##    for j in range (0,len(b[0])):
##        for k in range(0,len(c)):
##            c[i][j]+=a[i][k]+b[k][j]
##for d in c:
##    print(d)
##        
##================================14========================
##matrix1=[]
##i=0
##while i<3:
##    a=[]
##    j=0
##    while j<3:
##        k=int(input())
##        a.append(k)
##        j+=1
##    i+=1
##    matrix1.append(a)
##c=0
##while c<len(matrix1):
##    d=matrix1[c]
##    print(d)
##    c+=1
##matrix2=[]
##i=0
##while i<3:
##    a=[]
##    j=0
##    while j<3:
##        k=int(input())
##        a.append(k)
##        j+=1
##    i+=1
##    matrix2.append(a)
##c=0
##while c<len(matrix2):
##    e=matrix2[c]
##    print(e)
##    c+=1
##
##l=[[0,0,0],[0,0,0],[0,0,0]]
##for f in range(0,len(matrix1)):
##    for g in range(0,len(matrix2[0])):
##        for h in range(len(l)):  # Note that this should be the length of the second dimension of matrix2
##            l[f][g] += matrix1[f][h] * matrix2[h][g]
##print(l)
    
##a=[[1,2,3],
##   [4,5,6],
##   [7,8,9]]
##
##i=len(a)-1
##while i>-1:
##    print(a[i])
    


