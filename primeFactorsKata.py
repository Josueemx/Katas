def primeFactors(number):
    lista = []
    x = number
    while True:
        for y in range(2, x+1):
            while x%y == 0:
                x //= y
                lista.append(y)
        else:
            return(lista)
