from functools import reduce



def Triangular(num):
 
	return ((num*(num+1))/2)


def main():
	
	l=[(1,3),(3,2),(4,2),(15,5),(28,7)]
	
	l2=list(reduce((lambda x,y: x+y),list(filter(lambda x: x[0]==Triangular(x[1]),l))))
	
	print(reduce(lambda x,y: x+y,list(filter(lambda x: l2.index(x)%2==0,l2))))



main()