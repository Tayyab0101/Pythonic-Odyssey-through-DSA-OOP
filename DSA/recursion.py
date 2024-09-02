# Using for loop
def FibboSeq(x):
    if x <= 0:
        return []
    elif x == 1:
        return [0]
    elif x == 2:
        return [0, 1]
    
    seq = [0, 1]
    for i in range (2, x):
        next_value = seq[-1] + seq[-2]
        seq.append(next_value)
        
    return(seq)

print(FibboSeq(5))

# using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        new_value = fibonacci(n-1) + fibonacci(n-2)
        return new_value

def FibboSeq(x):
    fib_seq = []
    for i in range(x):
        fib_seq.append(fibonacci(i))
    return fib_seq

# Example usage:
print(FibboSeq(10))
    