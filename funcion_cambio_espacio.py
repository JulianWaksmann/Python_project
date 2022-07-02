def espacioToGuion (palabraseparadaensilabas):
    nueva_separada= ""
    for caracter in palabraseparadaensilabas:
        if caracter != " ":
            nueva_separada = nueva_separada + caracter
        else:
            nueva_separada = nueva_separada + "-"
    return nueva_separada