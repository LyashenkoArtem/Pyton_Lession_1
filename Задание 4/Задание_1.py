#(выработка в часах * ставка в час) + премия

def plata():
    chas = int(input('Введите количество отработанных часов: '))
    stav = int(input('Введите ставку работника: '))
    prem = int(input('Введите размер премии: '))

    plata = chas * stav + prem
    return plata

a = plata()
print(a)