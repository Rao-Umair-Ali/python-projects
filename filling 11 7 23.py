##----------------------------------counting of employee who sales product Note: this is for sorted file---------------
##fp = "C:\\Users\\RUA\\Desktop\\python\\d.csv"
##f = open(fp, "r")
##md=f.readline()
##c=1
##c1=1
##c2=1
##c3=1
##md=f.readline()
##list1=md.split(",")
##pi=list1[6]
##while True:
##    md=f.readline()
##    list1=md.split(",")
##    if not md:
##        break
##    ni=list1[6]
##    if pi!=ni:
##        new=list1[6]
##        while True:
##            md=f.readline()
##            list1=md.split(",")
##            if not md:
##                break
##            di=list1[6]
##            if di!=new:
##                new1=list1[6]
##                while True:
##                    md=f.readline()
##                    list1=md.split(",")
##                    if not md:
##                        break
##                    ni=list1[6]
##                    if ni!=new1:
##                        new1=list1[6]
##                        while True:
##                            md=f.readline()
##                            list1=md.split(",")
##                            if not md:
##                                break
##                            ne=list1[6]
##                            if ne==new1:
##                                c3+=1
##                    else:
##                        c2+=1
##            else:
##                c1+=1
##    else:
##        c+=1
##print(c,c1,c2,c3)



##----------------------------------counting of product---------------

##
##fp = "C:\\Users\\RUA\\Desktop\\python\\d.csv"
##f = open(fp, "r")
##f.readline()  
##counts = {}
##line = f.readline()
##while line:
##    data = line.split(",")
##    employee_id = data[6]
##    if employee_id in counts:
##        counts[employee_id] += 1
##    else:
##        counts[employee_id] = 1
##
##    line = f.readline()
##f.close()
##employees = list(counts.keys())
##i = 0
##while i < len(employees):
##    employee = employees[i]
##    count = counts[employee]
##    print("Employee ID:", employee)
##    print("Product Count:", count)
##    print()
##    i += 1
##
##
##
##
####----------------------------------counting of employee who sales product Note: this is for sorted file---------------
##
##fp = "C:\\Users\\RUA\\Desktop\\python\\d.csv"
##f = open(fp, "r")
##f.readline()
##counts = {}
##line = f.readline()
##while line:
##    data = line.split(",")
##    employee_id = data[6]
##    price =int(data[4])
##    qty =int(data[3])
##    new=qty*price
##    if employee_id in counts:
##        counts[employee_id] += new
##    else:
##        counts[employee_id] = new
##    
##    line = f.readline()
##    
##f.close()
##employees = list(counts.keys())
##i = 0
##while i < len(employees):
##    employee = employees[i]
##    count = counts[employee]
##    print("Employee ID:", employee)
##    print("Revenue generated :", count)
##    print()
##    i += 1
##
##


##----------------------------------counting of employee who sales product Note: this is for sorted file---------------

fp = "C:\\Users\\RUA\\Desktop\\python\\d.csv"
f = open(fp, "r")
f.readline()
counts = {}
line = f.readline()
while line:
    data = line.split(",")
    employee_id = data[6]
    price =int(data[4])
    qty =int(data[3])
    new=qty*price
    if employee_id in counts:
        counts[employee_id] += new
    else:
        counts[employee_id] = new
    
    line = f.readline()
    
f.close()
employees = list(counts.keys())
i = 0
a=[]
while i < len(employees):
    employee = employees[i]
    count = counts[employee]
    a.append([count,employee])
    i += 1
a.sort()
b=a[-1]
print("best employee:",b)
























