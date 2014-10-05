def toRoman(num):
    import math
    Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    Millar=["", "M", "MM", "MMM"]
    x = num
    if(x>=1000):
        u= x % 10
        d=int(((x%1000)%100)//10)
        c=int((x%1000)//100)
        m=int(math.floor(x/1000))
        return(str(Millar[m]+Centena[c]+Decena[d]+Unidad[u]))
    elif(x>=100):
        u= x % 10
        d=int((x%100)//10)
        c=int(math.floor(x/100))
        return(str(Centena[c]+Decena[d]+Unidad[u]))
    elif(x>=10):
        u= x % 10
        d=int(math.floor(x/10))
        return(str(Decena[d]+Unidad[u])) 
    else:
        return(str(Unidad[x]))
