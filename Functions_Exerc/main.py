# we get 2 integers values (m and n) != 0, find the MDC
def more_small(x, y):
    if x > y:
        return y
    return x


def max_div(x, y, small):
    cont = 1
    while cont <= small:
        if (x % cont == 0) and (y % cont == 0):
            mdc = cont
        cont = cont + 1
    return mdc


x = int(input("Insert a number"))
y = int(input("Insert a number"))
small = more_small(x, y)
mdc = max_div(x, y, small)
print(f"O mdc({x},{y})={mdc} ")


# giving a n value, determinate the sum of all "divisors", if the num is 0 return 0
def sum_divs(n):
    if n == 0:
        return 0
    summa = 0
    x = 1
    while x <= n:
        if n % x == 0:
            summa = summa + x
        x = x + 1
    return summa


n = int(input("insert a integer num: "))
answer = sum_divs(n)
print(f"The summa of divisors of {n} is {answer}")


# find if a number is prime
def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            print("Not is prime", n, "is divisor")
            return False
    print("Is prime")
    return True


num = int(input("input a number: "))
is_prime(num)

# build a function that find if a input number is "triangular"
def is_triangular(num):
    m = 1
    sum = 0
    while sum < num:
        sum = sum + m
        m = num + 1
    if sum == num:
        return True
    return False

# for n in range(1, 1000):
#     is_triangular(num)


num = int(input("insert a number: "))
answer = is_triangular(num)
print(f"{num} is triangular {answer}")


# calculate the recursive factorial of a given number
def fact(num):
    if num == 1 or num == 0:
        return 1
    return num * fact(num-1)


num = int(input("input a number: "))
answer = fact(num)
print(f"Factorial of {num} is {answer}")


# function to calculate the recursive value of x**y
def pot(base, exp):
    if exp == 0:
        return 1
    return base * pot(base, exp-1)


base = int(input("Insert a number x: "))
exp = int(input("Insert a number y: "))
answer = pot(base, exp)
print(f"{answer}")

frase = "Hello world"
print(frase[3:7].count('o'))
print(frase[3:].count('o'))
print(frase[3:len(frase)].count('o'))