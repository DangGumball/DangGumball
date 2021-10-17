n = int(input('Enter a number n: '))
def giaiThua(n):
    if n==0:
        return 1
    return n * giaiThua(n - 1)
print(giaiThua(n))