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
# The Time Complexity is O(2^n) because of 2 recursion calls for every term
# The Space Complexity is O(n)

#recursive fibonacci(memoized)
def fibonacci_memoized(n) -> int:
    global memo_fibonacci
    if memo_fibonacci[n] != -1: 
        return memo_fibonacci[n]
    elif n <= 1: 
        memo_fibonacci[n] = n
        return n
    else:
        memo_fibonacci[n] = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
        return memo_fibonacci[n]
# The Time Complexity is O(n) because each term is only calculated once and memoized for future use
# The Space Complexity is O(n)

