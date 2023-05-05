#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
import matplotlib.pyplot as plt

# Pure Recursive Method
def fib_recursive(n):
    if n < 0:
        raise Exception("Invalid Fib Input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Dynamic Programming Method
def fib_dynamic(n):
    if n < 0:
        raise Exception("Invalid Fib Input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

# Measure Execution Time for Pure Recursive Method and Dynamic Programming Method
recursive_times = []
dynamic_times = []
n_values = list(range(10, 51, 10))

for n in n_values:
    # Measure Pure Recursive Method Execution Time
    start_time = time.time()
    fib_recursive(n)
    end_time = time.time()
    recursive_times.append(end_time - start_time)
    
    # Measure Dynamic Programming Method Execution Time
    start_time = time.time()
    fib_dynamic(n)
    end_time = time.time()
    dynamic_times.append(end_time - start_time)
    
# Plot the Results
plt.plot(n_values, recursive_times, label="Recursive Method")
plt.plot(n_values, dynamic_times, label="Dynamic Programming Method")
plt.xlabel("n")
plt.ylabel("Execution Time (s)")
plt.title("Execution Time for Pure Recursive and Dynamic Programming Methods")
plt.legend()
plt.show()

# Determine the maximum value of n that recursive method can calculate
n = 0
try:
    while True:
        fib_recursive(n)
        n += 1
except RecursionError:
    print(f"Maximum value of n for recursive method: {n - 1}")

# Calculate the Fibonacci number using dynamic programming method for n = 10,000
print(fib_dynamic(10000))


# In[ ]:





# In[ ]:




