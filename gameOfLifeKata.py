def vecinos(x, b):
    global universo
    global columnas
    global lineas
    b = universo
    count = 0
    if x == 0:
        if universo[x+1]== "*":
            count += 1
        if universo[x+1+columnas] == "*":
            count += 1
        if universo[x+columnas] == "*":
            count += 1
        return(count)
    if x == columnas-1:
        if universo[x-1] == "*":
            count += 1
        if universo[x-1+columnas] == "*":
            count += 1
        if universo[x+columnas] == "*":
            count += 1
        return(count)
    if x == (lineas-1)*columnas:
        if universo[x-columnas] == "*":
            count += 1
        if universo[x+1-columnas] == "*":
            count += 1
        if universo[x+1]== "*":
            count += 1
        return(count)
    if x == (lineas*columnas)-1:
        if universo[x-columnas] == "*":
            count += 1
        if universo[x-1-columnas] == "*":
            count += 1
        if universo[x-1] == "*":
            count += 1
        return(count)
    if x > (lineas-1)*columnas and x < (lineas*columnas)-1 :
        if universo[x-1] == "*":
            count += 1
        if universo[x+1]== "*":
            count += 1
        if universo[x-1-columnas] == "*":
            count += 1
        if universo[x-columnas] == "*":
            count += 1
        if universo[x+1-columnas] == "*":
            count += 1
        return(count)
    if (x+1) % columnas == 0:
        if universo[x+columnas] == "*":
            count += 1
        if universo[x-1+columnas] == "*":
            count += 1
        if universo[x-1] == "*":
            count += 1
        if universo[x-columnas] == "*":
            count += 1
        if universo[x-1-columnas] == "*":
            count += 1
        return(count)
    if x % columnas == 0:
        if universo[x+1+columnas] == "*":
            count += 1
        if universo[x+columnas] == "*":
            count += 1
        if universo[x+1] == "*":
            count += 1
        if universo[x+1-columnas] == "*":
            count += 1
        if universo[x-columnas] == "*":
            count += 1
        return(count)
    if x > 0 and x < columnas-1:
        if universo[x+1+columnas] == "*":
            count += 1
        if universo[x+columnas] == "*":
            count += 1
        if universo[x-1+columnas] == "*":
            count += 1
        if universo[x+1] == "*":
            count += 1
        if universo[x-1] == "*":
            count += 1
        return(count)
    if universo[x+1+columnas] == "*":
        count += 1
    if universo[x+columnas] == "*":
        count += 1
    if universo[x-1+columnas] == "*":
        count += 1
    if universo[x+1] == "*":
        count += 1
    if universo[x-1] == "*":
        count += 1
    if universo[x+1-columnas] == "*":
        count += 1
    if universo[x-columnas] == "*":
        count += 1
    if universo[x-1-columnas] == "*":
        count += 1
    return(count)

def NextOfspring(u):
    global universo
    global universo2
    global columnas
    global lineas
    global cortar
    cortar = "\n"
    lineas = int(u[0])
    columnas = int(u[1])
    universo = u[2:]
    xx = ""
    universo2 = ""
    for i in range(len(universo)):
        if universo[i] == cortar:
            ()
        else:
            xx += universo[i]
    for a in range(len(universo)):
        if universo[a] == "*":
            if vecinos(a, universo) < 2:
                universo2 += "."
            elif vecinos(a, universo) > 3:
                universo2 += "."
            elif vecinos(a, universo) == 3 and vecinos(a, universo) == 2:
                universo2 += "*"
            else:
                universo2 += "*"
        elif universo[a] == "." and vecinos(a, universo) == 3:
            universo2 += "*"
        else:
            universo2 += "."
    c = str(lineas)+str(columnas) + universo2
    return(c)

def GetUniverse(u):
    global columnas
    global lineas
    global cortar
    cortar = "\n"
    lineas = int(u[0])
    columnas = int(u[1])
    uni = u[2:]
    xx = ""
    for i in range(lineas):
        if i == lineas-1:
            xx += uni[i*columnas:(i*columnas)+columnas]
        else:
            xx += uni[i*columnas:(i*columnas)+columnas] + cortar
    return(xx + "\n")       

if __name__ == '__main__':
    print("Captura un universo (Linea por linea segun el formato y vacio para terminar)")
    u = ""
    line = input()
    while(line != ""):
        u += line
        line = input()
    option = input("Teclee n para ver la siguiente generacion y s para deter la simulacion")
    while(option == "n"):
        u = NextOfspring(u)
        print(GetUniverse(u))
        option = input()
    
