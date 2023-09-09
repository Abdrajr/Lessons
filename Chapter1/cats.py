#create a function named collatz(number)
# if number is even 
#print // 2
#if odd should print and return 3* number +  1
#then program that lets user type and int and keeps calling colltz() till function returns value 1

def collatz(num):
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    elif num % 2 == 1:
        print(3 * num + 1)
        return( 3 * num + 1)
number = int(input('Enter number : '))
print(number)
while number != 1 :
    number = collatz(number)
    print(number)
    