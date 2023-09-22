def fibonacci_gen(n):
    a, b, count = 0 ,1, 0
    while count < n:
        yield a
        a, b = b, a+b
        count += 1

if __name__ == '__main__':
    n = int(input('Enter the number of values you wish to generate in Fibonacci sequence : '))
    fibonacci_sequence = list(fibonacci_gen(n))
    print(f"Fibonacci sequence up to the {n}th number:")
    print(fibonacci_sequence)
