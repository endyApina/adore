print("Exercise 1")

def isPalindrome(n: int) -> bool:
 
    # Find reverse of n
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
 
    # If n and rev are same,
    # then n is palindrome
    return (n == rev)
 
# prints palindrome between min and max
def getPal(minn: int, maxx: int) -> None:
    counter = 0
    for i in range(minn, maxx + 1):
        if isPalindrome(i):
            counter = counter + 1
            if counter == 10:
                print(i, end = " \n")
                counter = 0
            else: 
                print(i, end = " ")

getPal(1, 3000)

print("\nExercise 2")

def primeCheck(n):
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n==1 or n==0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Not prime if divisable by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(n**(1/2))+1, 2):
            if n%i == 0:
                return False
        return True

def checkPrime(min: int, maxx: int) -> None:
    counter = 0
    for i in range(min, maxx + 1):
        if primeCheck(i): 
            counter = counter + 1
            if counter == 10: 
                print(i, end = " \n")
                counter = 0
            else: 
                print(i, end = " ")

checkPrime(100, 1000)

print("\nExercise 3")

def common_divisors(x, y):
   cd = 1   
   if x % y == 0:
       print(y)
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           cd = k
           print(cd)
           break 
   return cd

firstVal = input("Please enter the first integer: ")
secondVal = input("Please enter the second integer: ")

