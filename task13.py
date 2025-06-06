son = int(input("1-sonni kiriting: "))
eng_kichik = son
eng_katta = son


for i in range(6):
    son = int(input(f"{i+2}-sonni kiriting: "))

    if son < eng_kichik:
        eng_kichik = son


    if son > eng_katta:
        eng_katta = son



print("Eng kichik son:", eng_kichik)
print("Eng katta son:", eng_katta)

