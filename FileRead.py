##------------------------------for adding specific index number-------------

##fp="C:\\Users\\RUA\\Desktop\\python\\data.csv"
##f=open(fp,"r")
##n=3
##i=0
##add=0
##line=f.readline()
##list1=line.split(",")
##p=list1[2]
##print(p)
##while i<n:
##    line=f.readline()
##    if not line:  
##        break
##    list1=line.split(",")
##    p=list1[2]
##    i+=1
##    n=int(p)
##    add+=n
##print(add)


##------------------------------for writing any data in given file (append)-------------


##fp="C:\\Users\\RUA\\Desktop\\python\\d.csv"
##f=open(fp,"a",encoding='utf-8')
##n=int(input("How many data you want to add in list"))
##i=0
##while i<n:
##    book=input("book name")
##    Author=input("Author name")
##    year=input("year released")
##    f.write(book+","+Author+","+year+","+"\n")
##    i+=1
##f.close()

##------------------------------for searching -------------

##fp = "C:\Users\RUA\Desktop\python\d.csv"
##f = open(fp, "r", encoding='utf-8')
##authorname = input("Enter the author's name: ")
##n = 4
##i = 0
##line = f.readline()
##list1 = line.split(",")
##while i < n:
##    line = f.readline()
##    
##    if not line:
##        break
##    list1 = line.split(",")
##    if list1[1] == authorname:
##        print(list1[0])
##        i += 1
##if i == 0:
##    print("No books found by", authorname)
##f.close()

##------------------------------for searching between -------------
##uusing csv ask user the user to enter a starting year and end year
##displlay all book released between those two year .
##fp = "C:\\Users\\RUA\\Desktop\\python\\d.csv"
##f = open(fp, "r", encoding='utf-8')
##sy=int(input("starting year"))
##ey=int(input("ending year"))
##line = f.readline()
##list1 = line.split(",")
##i=0
##n=4
##while i<n:
##    line = f.readline()
##    if not line:
##        break
##    list1 = line.split(",")
##    year=list1[2]
##    y=int(year)
##    if y>=sy and y<=ey:
##        print(list1[0],y)
##    i+=1
##
