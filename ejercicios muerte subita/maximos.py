def Maximo(L):
    return max(L)

def main():
	l=[[1,2,3],[12,45,32],[112,25,23]]
	print(list(map(lambda x: Maximo(x), l)))

main()