
# print(9 ** 3)


n = int(input("Enter the number: "))
sum = 0

for i in range(1, n+1, 1):
    sum = sum + (i ** i)
print(sum)