def first_lyric(lista_first_lyrics):
    first_lyrics=[]

    for word in lista_first_lyrics:
        try:
            assert type(word) == str, f'{word} is not str'
            assert len(word)>0, f'is vacio'
            first_lyrics.append(word[0])
        except AssertionError as e:
            print(e)
    
    return first_lyrics
    
lista = ['brandon', 20, " ", 'Camila', '45']
words = list(first_lyric(lista))
print(words)

a = True
b = False
print (a and b) 