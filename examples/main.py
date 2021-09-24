import time

from test_py_go import greet, hello, factorial

hello()
greet(b"Gijs")


def pyfactorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


print("=" * 10)
print("Python benchmark")
start = time.time()
pyfactorial(100_000)
end = time.time()
print(end - start, "seconds")
print("=" * 10)

print("Go benchmark")
start = time.time()
factorial(100_000)
end = time.time()
print(end - start, "seconds")
print("=" * 10)
