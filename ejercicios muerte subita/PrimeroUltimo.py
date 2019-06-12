from functools import reduce

def primeroUltimo(lista):
    return lista[0],lista[-1]
    
def main():
l=[[12,54,32,12],[2,8,4,6,3],[12,35,65,98,78]]
print(list(map(lambda x: primeroUltimo(x),l)))

main()