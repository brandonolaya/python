# 2. esta funcion resive dos parametros un argumento y una funcion 
def func1(un_arg, una_func):
    """
    nose que hago aqui
    mentiras soy la documentacion de esta funcion
    """
    # 4. cuando la invoca le llega ese algumento y procede
    def func2(otro_arg):
        #5. ese argumento lo procede a operar y retorna un valor para la operacion 3
        return otro_arg * 2
    # 3. valor depende la funcion dos asi que la invoca y le manda un argumento
    # 6. trajo el valor que le mando la funcion 2
    valor = func2(un_arg)
    #7. como ya termino de operrar lo de arriva este retorna un valor para una funcion
    # como ya ya lo habiamos pasado como parametro desde cualquier funcion
    return una_func(valor)
    """
    nose que hago aqui
    """

un_arg=1
# 8. se le pasa el valor que opero la primera funcion 
def cualquier_func(cualquier_arg):
    # 9. opera con lo que le madaron y opera , con esto regresa y termina de operar
    return cualquier_arg + 5
# 1. en lo global llamo a la funcion 1, le paso un argumento y una funcion
#  
func1(un_arg, cualquier_func)
#llamo la documentacion de la funcion
help(func1)