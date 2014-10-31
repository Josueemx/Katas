def GetRankedGame(hands):
    """
        Esta funcion recibe las manos y se encarga de determinar 
        que juego tiene cada mano, darles puntajes y determinar cual gana
        (regresa una cadena con el formato indicado) 
    """
    handsarr = hands.split("\n")
    finishedstring = ''
    itcount = -1
    handvalues = {}
    cardvalues = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    for hand in handsarr:
        itcount += 1
        if hand == '':
            break
        elif len(hand) < 20:
            finishedstring += hand + '*&' 
        else:
            finishedstring += hand
            faces = hand[0:20:3]
            suits = hand[1:20:3]
            hnf = True
            fs = ''
            ss = ''
            facestring = 'AKQJT987654321'
            for x in 'AKQJT987654321':
                for y in faces:
                    if x == y:
                        fs += y
            for x in 'scdh':
                for y in suits:
                    if y == x:
                        ss += y
            #Royal Flush
            if hnf and 'AKQJT' in fs and (ss.count('s') > 4 or ss.count('c') > 4 or ss.count('d') > 4 or ss.count('h') > 4):
                finishedstring += " Royal Flush"
                hnf = False
                handvalues[itcount] = 1000
            #Straight Flush
            if hnf:
                for i in range(0,9):
                    if facestring[i:i+5] in fs and (ss.count('s') > 4 or ss.count('c') > 4 or ss.count('d') > 4 or ss.count('h') > 4):
                        hnf = False
                        finishedstring += " Straight Flush"
                        handvalues[itcount] = 450*2
                        break
            #Poker
            if hnf:
                for i in range (0,14):
                    if facestring[i] * 4 in fs:
                        finishedstring += ' Poker'
                        hnf = False
                        handvalues[itcount] = 400*2
                        break
            #Full House
            fhpos = False
            exclude = 0
            if hnf:
                for i in range(0,14):
                    if facestring[i] * 3 in fs:
                        exclude = i
                        fhpos = True
                        break
                if fhpos:
                    for i in range(0,14):
                        if i == exclude:
                            pass
                        elif facestring[i] * 2 in fs:
                            finishedstring += ' Full House'
                            hnf = False
                            handvalues[itcount] = 350*2
                            break
            #Flush
            if hnf and (ss.count('s') > 4 or ss.count('c') > 4 or ss.count('d') > 4 or ss.count('h') > 4):
                finishedstring += ' Flush'
                hnf = False
                handvalues[itcount] = 300*2
            #Straight
            if hnf:
                for i in range(0,9):
                    if facestring[i:i+5] in fs:
                        hnf = False
                        finishedstring += " Straight"
                        handvalues[itcount] = 250*2
                        break
            #Three of a kind
            if hnf:
                for i in range(0,14):
                    if facestring[i] * 3 in fs:
                        finishedstring += " Three of a Kind"
                        handvalues[itcount] = 200*2
                        hnf = False
                        break
            #Two pair, pair and no card...
            paircount = 0
            if hnf:
                for i in range(0,14):
                    if facestring[i] * 2 in fs:
                        paircount += 1
                if paircount > 1:
                    finishedstring += " Two Pair"
                    handvalues[itcount] = 150*2
                elif paircount > 0:
                    finishedstring += " One Pair"
                    handvalues[itcount] = 100*2
                elif paircount == 0:
                    finishedstring += " High card"
                    handvalues[itcount] = 50*2
            finishedstring += '*&'
            #add value to the hand according to the high cards
            for card in fs:
                handvalues[itcount] += cardvalues[card]
    #End giant for
    #Begin winner calculation.
    winner = ''
    ts = 1000
    while ts > 0:
        for key in handvalues:
            if handvalues[key] == ts:
                winner = key
                break
        ts -= 1
        if winner != '':
            break
    winstring = finishedstring.split('&')
    finalstring = ''
    for x in range(0,len(winstring)):
        if x == winner:
            finalstring += winstring[x].replace('*', ' (winner)\n')
        else:
            finalstring += winstring[x].replace('*', '\n')
                

    return finalstring
    
if __name__ == '__main__':
    print("Captura una mano por linea y una linea en blanco para terminar:")
    hands = ""
    line = input()
    while(line != ""):
        hands += line + "\n"
        line = input()
    print(GetRankedGame(hands))
