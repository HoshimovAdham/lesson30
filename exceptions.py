
try:
    lst = [1, 2]
    print(lst[1])
    print(1 + int("2"))
    print(3 / 1)
except IndexError:
    print("list indexingda muammo bor")
except TypeError:
    print("Type lar bilan ishlashda muammo bor")
except ZeroDivisionError:
    print("bolishda muammo bor")
except:
    print('code da muammo bor')
else:
    print('code da muammo yoq')
finally:
    print("try except tugadi")
