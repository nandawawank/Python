number = input("Input Number = ") # default type data from function input is String

if number.isnumeric:
    if int(number) % 2 == 0 and int(number) > 0:
        print(number, 'is integers and positif')
    elif int(number) % 2 == 0 and int(number) < 0:
        print(number, 'is integers and negatif')
    else:
        print(number, 'is not integers')
else:
    print("Your input not number")