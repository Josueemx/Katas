# coding: utf8
template = " 1 │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n 7 │ 8 │ 9 "

def GetTablero():
    global template
    return str(template)

def JuegoContinua():
    global tie
    return not tie

def IntentarTirada(casilla):
    global tie
    global template
    global turno
    global caserror
    global count
    if not caserror:
        if turno == "O":
            turno = "X"
        else:
            turno = "O"
    casilla = int(casilla)
    if casilla > 9 or casilla < 1:
        caserror = True
        return "La tirada debe de estar entre 1 y 9"
    if casilla == 1:
        if template[1] == 'X' or template[1] == 'O':
            caserror = True
            return "La casilla ya esta ocupada"
        else:
            caserror = False
            count += 1
            temp = ''
            for x in range(0,len(template)):
                if template[x] == '1':
                    temp += turno
                else:
                    temp += template[x]
            template = temp
            if template[1] + template[5] + template[9] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[25] + template[29] + template[33] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[49] + template[53] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[25] + template[49] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[5] + template[29] + template[53] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[33] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if count > 8:
                tie = True
                return "Juego empatado. :("
    if casilla == 2:
        if template[5] == 'X' or template[5] == 'O':
            caserror = True
            return "La casilla ya esta ocupada"
        else:
            caserror = False
            count += 1
            temp = ''
            for x in range(0,len(template)):
                if template[x] == '2':
                    temp += turno
                else:
                    temp += template[x]
            template = temp
            if template[1] + template[5] + template[9] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[25] + template[29] + template[33] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[49] + template[53] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[25] + template[49] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[5] + template[29] + template[53] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[33] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if count > 8:
                tie = True
                return "Juego empatado. :("
    if casilla == 3:
        if template[9] == 'X' or template[9] == 'O':
            caserror = True
            return "La casilla ya esta ocupada"
        else:
            caserror = False
            count += 1
            temp = ''
            for x in range(0,len(template)):
                if template[x] == '3':
                    temp += turno
                else:
                    temp += template[x]
            template = temp
            if template[1] + template[5] + template[9] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[25] + template[29] + template[33] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[49] + template[53] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[25] + template[49] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[5] + template[29] + template[53] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[33] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[29] + template[49] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if count > 8:
                tie = True
                return "Juego empatado. :("
    if casilla == 4:
        if template[25] == 'X' or template[25] == 'O':
            caserror = True
            return "La casilla ya esta ocupada"
        else:
            caserror = False
            count += 1
            temp = ''
            for x in range(0,len(template)):
                if template[x] == '4':
                    temp += turno
                else:
                    temp += template[x]
            template = temp
            if template[1] + template[5] + template[9] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[25] + template[29] + template[33] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[49] + template[53] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[25] + template[49] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[5] + template[29] + template[53] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[33] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if count > 8:
                tie = True
                return "Juego empatado. :("
    if casilla == 5:
        if template[29] == 'X' or template[29] == 'O':
            caserror = True
            return "La casilla ya esta ocupada"
        else:
            caserror = False
            count += 1
            temp = ''
            for x in range(0,len(template)):
                if template[x] == '5':
                    temp += turno
                else:
                    temp += template[x]
            template = temp
            if template[1] + template[5] + template[9] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[25] + template[29] + template[33] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[49] + template[53] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[25] + template[49] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[5] + template[29] + template[53] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[33] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if count > 8:
                tie = True
                return "Juego empatado. :("
    if casilla == 6:
        if template[33] == 'X' or template[33] == 'O':
            caserror = True
            return "La casilla ya esta ocupada"
        else:
            caserror = False
            count += 1
            temp = ''
            for x in range(0,len(template)):
                if template[x] == '6':
                    temp += turno
                else:
                    temp += template[x]
            template = temp
            if template[1] + template[5] + template[9] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[25] + template[29] + template[33] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[49] + template[53] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[25] + template[49] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[5] + template[29] + template[53] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[33] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if count > 8:
                tie = True
                return "Juego empatado. :("
    if casilla == 7:
        if template[49] == 'X' or template[49] == 'O':
            caserror = True
            return "La casilla ya esta ocupada"
        else:
            caserror = False
            count += 1
            temp = ''
            for x in range(0,len(template)):
                if template[x] == '7':
                    temp += turno
                else:
                    temp += template[x]
            template = temp
            if template[1] + template[5] + template[9] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[25] + template[29] + template[33] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[49] + template[53] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[25] + template[49] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[5] + template[29] + template[53] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[33] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if count > 8:
                tie = True
                return "Juego empatado. :("
    if casilla == 8:
        if template[53] == 'X' or template[53] == 'O':
            caserror = True
            return "La casilla ya esta ocupada"
        else:
            caserror = False
            count += 1
            temp = ''
            for x in range(0,len(template)):
                if template[x] == '8':
                    temp += turno
                else:
                    temp += template[x]
            template = temp
            if template[1] + template[5] + template[9] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[25] + template[29] + template[33] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[49] + template[53] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[25] + template[49] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[5] + template[29] + template[53] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[33] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if count > 8:
                tie = True
                return "Juego empatado. :("
    if casilla == 9:
        if template[57] == 'X' or template[57] == 'O':
            caserror = True
            return "La casilla ya esta ocupada"
        else:
            caserror = False
            count += 1
            temp = ''
            for x in range(0,len(template)):
                if template[x] == '9':
                    temp += turno
                else:
                    temp += template[x]
            template = temp
            if template[1] + template[5] + template[9] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[25] + template[29] + template[33] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[49] + template[53] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[25] + template[49] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[5] + template[29] + template[53] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[33] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[1] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if template[9] + template[29] + template[57] == turno * 3:
                tie = True
                return "Felicidades " + turno + " as ganado. weeee"
            if count > 8:
                tie = True
                return "Juego empatado. :("
    return ""
    """
        Esta funcion recibe el intento del jugador por ocupar una casilla
        y regresa una cadena segun los siguientes criterios:
        Si esta fuera de rango: "La tirada debe de estar entre 1 y 9"
        Si la casilla esta ocupada: "La casilla ya esta ocupada"
        Si x a ganado: "Felicidades X as ganado. weeee"
        Si o a ganado: "Felicidades O as ganado. weeee"
        Si el juego a quedado empatado: "Juego empatado. :("
        Ninguna de las anteriores: "" (cadena vacia)
    """

def IniciaJuego():
    global turno
    global caserror
    global count
    global tie
    global template
    count = 0
    caserror = False
    turno = 'O'
    template = " 1 │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n 7 │ 8 │ 9 "
    tie = False

if __name__ == '__main__':
    IniciaJuego() 
    while(JuegoContinua()): 
        print(GetTablero())
        msg = ""
        casilla = int(input("Escoge una casilla: "))
        msg = IntentarTirada(casilla)
        if msg != "":
            print(msg)
