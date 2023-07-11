##----------------------------------counting of employee who sales product Note: this is for sorted file---------------
fp = "C:\\Users\\RUA\\Desktop\\python\\d.csv"
f = open(fp, "r")
md=f.readline()
c=1
c1=1
c2=1
c3=1
md=f.readline()
list1=md.split(",")
pi=list1[6]
while True:
    md=f.readline()
    list1=md.split(",")
    if not md:
        break
    ni=list1[6]
    if pi!=ni:
        new=list1[6]
        while True:
            md=f.readline()
            list1=md.split(",")
            if not md:
                break
            di=list1[6]
            if di!=new:
                new1=list1[6]
                while True:
                    md=f.readline()
                    list1=md.split(",")
                    if not md:
                        break
                    ni=list1[6]
                    if ni!=new1:
                        new1=list1[6]
                        while True:
                            md=f.readline()
                            list1=md.split(",")
                            if not md:
                                break
                            ne=list1[6]
                            if ne==new1:
                                c3+=1
                    else:
                        c2+=1
            else:
                c1+=1
    else:
        c+=1
print(c,c1,c2,c3)
