def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return(str("fizzbuzz"))
    elif num % 5 == 0:
        return(str("buzz"))
    elif num % 3 == 0:
        return(str("fizz"))
    else:
        return(str(num))
