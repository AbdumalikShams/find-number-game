"""Son topish o'yini"""

import random as r

def find_number(x=10):
    son = r.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>> "))
        if taxmin > son:
            print(f"Xato.Men o'ylagan son {taxmin} dan kichikroq.")
        elif taxmin < son:
            print(f"Xato. Men o'ylagan son {taxmin} dan kattaroq.")
        else:
            break
    print(f"Tabriklayman.{taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar

def find_number_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = r.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz. Tog'ri (t), "
                    f"Men o'ylagan son bundan kattaroq (+),kichikroq (-) ".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = find_number(x)
        taxminlar_pc = find_number_pc(x)
        
        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_user} ta taxmin bilan yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_pc} ta taxmin bilan yutdingiz!")
        else:
            print("Durrang!")
        
        yana = int(input("Yana davom ettirasizmi? ha(1) yo'q(0): "))
        
play()