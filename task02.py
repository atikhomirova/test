# Task 02
# Function to calculate Fibonacci numbers

if __name__ = __main__:

    def fib(n):
       if n == 0:
           return 0
       elif n == 1:
           return 1
       else:
           return fib(n - 1) + fib(n - 2)
    
    n = 5
    
    for i in range(n):
        print(fib(i))

