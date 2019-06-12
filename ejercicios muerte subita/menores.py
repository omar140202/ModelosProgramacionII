def Menor(L):
    return min(L)

def listaSuper(L):
    return [x for x in L if superpares(x)==True]

def superpares(num):
    if num==0:
        return True
    else:
        if(num%2==0):
            return True and superpares(int(num/10))
        else:
            return False

def main():
	l=[[26,51,35,48],[12,48,68,46,25],[13,46,15,84,23]]
	print(list(map(lambda x: Menor(x),list(map(lambda x:listaSuper(x),l)))))

main()