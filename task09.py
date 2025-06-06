eng_kichik = int(input("1-sonni kiriting: "))

for i in range(6):
    son = int(input(f"{i+2}-sonni kiriting: "))
    
    
    if son < eng_kichik:
        eng_kichik = son


print("Eng kichik son:", eng_kichik)

