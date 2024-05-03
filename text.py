
ədədlər = []
for i in range(5):
    ədəd = int(input("Bir ədəd daxil edin: "))
    ədədlər.append(ədəd)
ədədlər.sort()
print("Sıralanmış ədədlər:", ədədlər)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

n = 13
cəhd_sayi = 0

while True:
    giris = input("Ədəd daxil edin: ")
    cəhd_sayi += 1
    
    if int(giris) == n:
        print(f"Təbriklər! {cəhd_sayi} cəhdə {n} ədədini tapdınız.")
        break
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

for i in range(2, 101):
    sade = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            sade = False
            break
    if sade:
        print(i, end=" ")
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
word=input("Bir soz  daxil edin: ")
list=list(word)
list.sort()
print(list)
