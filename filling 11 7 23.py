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

##----------------------------------counting of employee who sales product Note: this is for unsorted file---------------
##fp = "C:\\Users\\RUA\\Desktop\\python\\d.csv"
##f = open(fp, "r")
##md=f.readline()
##md=f.readline()
##list1=md.split(",")
##ai=list1[6]
##a=1
##b=0
##c=0
##d=0
##while True:
##    md=f.readline()
##    list1=md.split(",")
##    if not md:
##        break
##    bi=list1[6]
##    if ai!=bi:
##        md=f.readline()
##        list1=md.split(",")
##        if not md:
##            break
##        ci=list1[6]
##        while True:
##            md=f.readline()
##            list1=md.split(",")
##            if not md:
##                break
##            di=list1[6]
##            if ci!=di:
##                md=f.readline()
##                list1=md.split(",")
##                ei=list1[6]
##                if not md:
##                    break
##                while True:
##                    md=f.readline()
##                    list1=md.split(",")
##                    if not md:
##                        break
##                    fi=list1[6]
##                    if ei!=fi:
##                        md=f.readline()
##                        list1=md.split(",")
##                        gi=list1[6]
##                        if not md:
##                            break
##                        while True:
##                            md=f.readline()
##                            list1=md.split(",")
##                            if not md:
##                                break
##                            hi=list1[6]
##                            if gi==hi:
##                                d+=1
##                    else:
##                        c+=1
##                
##            else:
##                b+=1
##            
##    else:
##        a+=1
##print(d,hi)

##fp = "C:\\Users\\RUA\\Desktop\\python\\d.csv"
##f = open(fp, "r")
##f.readline()  # Skip the header row
##
##counts = {}
##current_employee = ""
##product_count = 0
##
##while True:
##    line = f.readline().strip()
##    if not line:
##        break
##
##    data = line.split(",")
##    employee_id = data[6]
##
##    if current_employee != employee_id:
##        if current_employee:
##            counts[current_employee] = product_count
##        current_employee = employee_id
##        product_count = 0
##
##    product_count += 1
##
### Add the last employee's count
##if current_employee:
##    counts[current_employee] = product_count
##
##f.close()
##
##for employee, count in counts.items():
##    print("Employee ID:", employee)
##    print("Product Count:", count)
##    print()
fp = "C:\\Users\\RUA\\Desktop\\python\\d.csv"
f = open(fp, "r")
f.readline()  
counts = {}
line = f.readline()
while line:
    data = line.split(",")
    employee_id = data[6]
    if employee_id in counts:
        counts[employee_id] += 1
    else:
        counts[employee_id] = 1

    line = f.readline()
f.close()
employees = list(counts.keys())
i = 0
while i < len(employees):
    employee = employees[i]
    count = counts[employee]
    print("Employee ID:", employee)
    print("Product Count:", count)
    print()
    i += 1
