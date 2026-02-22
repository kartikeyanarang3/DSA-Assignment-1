#recursive factorial
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)

#recursive fibonacci(naive)
def fibonacci_naive(n):
  if n<=1: 
    return n
  else:
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)


