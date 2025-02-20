import random

def generate_random_list(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit):
    return [num for num in range(2, limit + 1) if is_prime(num)]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    size = 50
    array = generate_random_list(size, 1, 100)
    
    print("Original List:", array)
    print("Bubble Sort:", bubble_sort(array[:]))
    print("Selection Sort:", selection_sort(array[:]))
    
    print("Max Element:", max(array))
    print("Min Element:", min(array))
    
    print("Fibonacci Sequence (10 terms):", fibonacci(10))
    print("Prime Numbers up to 50:", get_primes(50))
    
    print("Factorial of 5:", factorial(5))
    print("GCD of 12 and 18:", gcd(12, 18))
    print("LCM of 12 and 18:", lcm(12, 18))

if __name__ == "__main__":
    main()
