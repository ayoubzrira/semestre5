#! /usr/bin/env python3

def main():
    a = [((1,2),(3,5))]
    iterateur = iter(a)
#    depart = next(iterateur)
#    prec = depart
#    n = [ p for p,s in iterateur if p!=s]
    for p,s in iterateur:
        if p!=s:
            print(p!=s)






main()
