def affiche():
    a = int(input("entrez le nb de ligne"))
    for i in range(1,a+1):
        res += str(i)
        print(res,'\n')



def affiche2():
    a = int(input("entrez le nb de ligne"))
    for i in range(1,a):
        res = []*i
        x =0
        while x <= i:
            res.append(x)
            x += 1
def affiche3():
    a = int(input("entrez le nb de ligne"))
    res = ""
    for i in range(1,a+1):
        print(res[::-1],i,res,sep=" ")
        res = str(i) + res
affiche3()
