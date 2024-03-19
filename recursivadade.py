#recursividade
def fatorial(n):
    if n == 1:
        print('if --'+str(n))
        fatr = n
    else:
        print('else -- '+str(n))
        fatr = n*fatorial(n-1)
    print('return--'+str(n))
    return fatr
x = fatorial(5)
print(x)

def soma(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista[0]+soma(lista[1:])
print(soma([1,2,3,4]))

def resto(n):
    if n in [0,1]:
        rst = n
    else:
        rst = resto(n-2)
    return rst
print(resto(10))
