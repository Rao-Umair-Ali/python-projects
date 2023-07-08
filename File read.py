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

##fp = r"C:\Users\RUA\Desktop\python\d.csv"
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
