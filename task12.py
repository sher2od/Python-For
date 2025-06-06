t_yig = 0
j_yig = 0


n = int(input("nechigacha : "))

for i in range(n + 1):
    if i % 2 == 0:
        j_yig += i
    else:
        t_yig += i

print(j_yig,t_yig)

