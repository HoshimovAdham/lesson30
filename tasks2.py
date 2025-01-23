with open("raqamlar.txt", "r") as file:
    number_list = file.readlines()

operators = set()
n = set()
for line in number_list:
    num = line.split(" ")
    operators.add(" " + num[1].strip())
print("\nMavjud operator kodlari:")
for i in operators:
    print(i)


last_7 = set()
for line in number_list:
    num = line.replace(" ", "")[-8:]
    last_7.add(num)
print("\n7 ta raqamli telefon raqami:")
for i in last_7:
    print(i)