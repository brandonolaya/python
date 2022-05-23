my_tuple = (1,)
#print(type(my_tuple))
my_other_tuple = (2, 3, 4)
#reasignao no la modifico 
my_tuple += my_other_tuple
print(my_tuple)
#desempaqueto los valores de la tupla
x, y, z = my_other_tuple
print(y)

def coordenadas():
    return (34, 56, 78)
x, y, z = coordenadas()
print(y,z)