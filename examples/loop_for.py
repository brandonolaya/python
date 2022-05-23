def run(numb):
    for i in range(numb):
        if i % 2 !=0:
            continue
        elif i == 54:
            break
        print(i)
        
if __name__ == "__main__":
    number = int(input("write your number: "))
    run(number)