def run(repet):
    i=0
    while i < repet:
        numero = 2 ** i
        i += 1
        if numero < 1000000:
            print(numero)


if __name__ == "__main__":
    repetitions = int(input("How many powers are?: "))
    run(repetitions)