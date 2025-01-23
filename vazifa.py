# Uyga vazifa shartida yozgan kodlarimizni tushuntirish ham aytilgan ekan
"""
Quyidagi kodda foydalanuvchilar ro'yxati saqlangan fayldagi malumotlarni tahlil qilib,
mavjud foydalanuvchilar haqidagi ba'zi savollarga javob bo'lishi mumkin bo'lgan malumotlarni
qayta ishlab o'zgaruvchilarga saqlab ketildi.

"""

# Bizga 'json' fayllari bilan ishlash uchun quyidagi kutubxona kerak bo'ladi
import json 

# Uyga vazifa shartida yozgan kodimizda turli xolatlar(xar-hil turdagi xatoliklar)ni hisobga olish ham aytilgan ekan

# try orqali people.json faylini o'qishga urunib ko'ramiz
try:
    # people.json faylini 'file' deb olish
    with open('people.json', 'r') as file:
        # fayldagi malumotni o'zgaruvchiga qiymat sifatida berish
        people_list = json.load(file)

# Agar biz o'qimoqchi bo'lgan faylimiz topilmasa xabar berish uchun
except FileNotFoundError:
    print("\nFaylni topishda xatolik!!!\n")

# Agar biz o'qimoqchi bo'lgan fayl muammosiz o'qilsa habar berish
else:
    print("\nFayl o'qildi!!!\n")

    # Erkaklar sonini aniqlashga urinish
    try:
        males = list(filter(lambda man: man['gender'].lower() == 'male', people_list))
    except TypeError:
        print("\nRo'yxatdagi ma'lumotlarni aniqlashda xatolik!!!\n")
    except ValueError:
        print("\nRo'yxatdagi qiymatlar yoki shartlarda xatolik!!!\n")
    else:
        print("\nRo'yxatdagi erkaklar soni muammolarsiz aniqlandi!!!")
        print(f'\n1-Vazifa.\nFayldagi Erkaklar soni: {len(males)}ta')


    # Ayollar soni aniqlashga urinish
    try:
        females = list(filter(lambda woman: woman['gender'].lower() == 'female', people_list))
    except TypeError:
        print("\nRo'yxatdagi ma'lumotlarni aniqlashda xatolik!!!\n")
    except KeyError:
        print("Ro'yxatda 'gender' kalitini topishda xatolik\n")
    else:
        print("\nRo'yxatdagi ayollar soni muammolarsiz aniqlandi!!!")
        print(f'\n2-Vazifa.\nFayldagi Ayollar soni: {len(females)}ta')

        #Hindistonlik foydalanuvchilarni topishga urinish
    try:
        indian_user = list(filter(lambda indians: indians["country"] == "India", people_list))

    # Qanday xatolik ekanini chiqarish
    except Exception as e:
        print(f'xatolik yuz berdi: {e}')
    else:
        print("\nRo'yxatdan Hindistonlik foydalanuvchilar topildi!!!")
        print(f"\n3-Vazifa.\nFayldagi Hindistonlik foydalanuvchilar:")
        for i in indian_user:
            print(i)

        # 20yoshdan kichik foydalanuvchilar ro'yxati chiqarishga urinish
    try:
        age_20 = list(filter(lambda youngs: youngs['age'] <= 20, people_list))
    except Exception as e:
        print(f'Xatolik: {e}')
    else:
        print("\n20 yoshdan kichiklar muvaffaqiyatli topildi!!!")
        print(f"\n4-Vazifa.\nFayldagi 20 yoshdan kichiklar ro'yxati:")
        for i in age_20:
          print(i)

    # Muhandis kasbiga ega foydalanuvchilarni topishga urinish
    try:
        enginer_user = list(filter(lambda enginer: enginer['job'].lower() == "engineer", people_list))
    except Exception as e:
        print(f"Xatolik: {e}")
    else:
        print("\nRo'yxatdan muhandislar muvaffaqiyatli topildi")
        print(f"\n5-Vazifa.\nFayldagi Muhandis kasbiga ega foydalanuvchilar:")
        for i in enginer_user:
            print(i)
# Eng oxirida finally dan foydalanib faylni yopib ketish
finally:
    file.close()