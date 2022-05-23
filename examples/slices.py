name = input("What is your first name?: ")
#cut spaces in init and finish
name = name.strip()
#replace spaces in all chain text this is better
name = name.replace(' ','')
print(name)

#cut position 0 sizen 4 return xxxx
print(name[0:4])
#return position two in two
print(name[0:6:2])
#invert the text
print(name[::-1])