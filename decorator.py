import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"{func.__name__} took {time_taken:.6f} seconds to execute.")
        print('')
        return result
    return wrapper

@execution_time
def count_down_1(num1):
    print(f'Counting down from {num1} to 0 :')
    for i in range(num1,-1,-1):
        i -=1

@execution_time
def count_down_2(num2):
    print(f'Counting down from {num2} to 0 :')
    for i in range(num2,-1,-1):
        i -=1


if __name__ =="__main__":
    print('Enter 2 large numbers seperated by space : ')
    num1, num2  = [int(x) for x in input().split()]
    count_down_1(num1)
    count_down_2(num2)