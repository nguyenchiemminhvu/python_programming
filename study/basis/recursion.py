def recur_sample(n):
    if n > 0:
        recur_sample(n - 1)
        print(n)

recur_sample(5)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def fibonacy(n):
    if n == 1 or n == 2:
        return 1
    return fibonacy(n - 1) + fibonacy(n - 2)

print(fibonacy(10))

def reverse_string(s, l, r):
    if l >= r:
        return s
    s[l], s[r] = s[r], s[l]
    return reverse_string(s, l + 1, r - 1)

s = list("abcdefg")
print(''.join(reverse_string(s, 0, len(s) - 1)))