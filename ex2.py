#checker odd or even
num=input("Enter any number: ")
#check int or str and print error
if num.isnumeric():
    #divide number to 2, if reminder 0 then even
    number=int(num)
    if (number % 2) == 0:
        print(number, 'is Even')
    else:
        print(number, 'is Odd')
else:
    print("Error!\nPlease, enter only number.")
