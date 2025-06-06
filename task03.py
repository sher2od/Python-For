n = int(input("nechidan boshlab >> "))

if n <= 15:
    for i in range(n, 16):
        print(i)
else:
    for i in range(n, 14, -1):
        print(i)
