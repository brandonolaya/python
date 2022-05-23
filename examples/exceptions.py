from posixpath import split


def split_element_of_list(lista, split):
    try: 
        return [i/ split for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
split = 0

print(split_element_of_list(lista, split))