def superpares(num):
    if num==0:
        return True
    else:
        if(num%2==0):
            return True and superpares(int(num/10))
        else:
            return False
def main():
	l=[248,523,625,864,222]
	print(list(filter(lambda x: superpares(x)==True,l)))

main()