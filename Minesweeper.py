import random

def main():
    pole_result = [0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0,]

    pole = [" ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ",]

    RozmisteniBomb(pole_result)
    VypsaniCisel(pole_result)
    #Board(pole_result)

    hrac_column = 10
    hrac_row = 10
    k = True

    while k:
        if Bomba(pole,k) == False:
            break
        elif ZjisteniBomb(pole,pole_result) == False:
            print("Vyhrál jste")
            break
        CyklusHry(pole, pole_result, hrac_column, hrac_row)

def CyklusHry(pole, pole_result, hrac_column, hrac_row):
    Board(pole)
    x = input("Chcete zvolit pole (p) nebo umístit vlaječku na místo bomby (v) ? ")
    if x == "p":
        hrac_column = int(input("Zadejte column: "))
        hrac_row = int(input('Zadejte row: '))
    elif x.lower() == "v":
        OznaceniBomb(pole)
    else:
        print("Neplatné zadání")
    ZmenaPole(pole, pole_result, hrac_column, hrac_row)
    Board(pole)
    print("\n")
    print("\n")
    print("\n")
    print("\n")

def RozmisteniBomb(pole):
    for i in range(1,random.randint(5,8)):
        j = random.randint(0,63)
        pole[j] = "*"

def VypsaniCisel(pole):
    i = 0
    while i < (len(pole)):
        k = pole[i]
        if k == "*":
            Urceni(pole, i, 0)
            i += 1
        else:
            i += 1

def UrceniCisel(pole,ind,i, array):
    while i < 8:
        try:
            if pole[ind + array[i]] != "*" and (ind + array[i]) >= 0:
                pole[ind + array[i]] += 1
            i += 1
        except:
            i += 1

def Urceni(pole, ind, i):
    array1 = [+1, -1, +7, -7, +8, -8, +9, -9]
    array2 = [-1, +7, +8, -8, -9]
    array3 = [+1, -7, +8, -8, +9]

    array_right = [7, 15, 23, 31, 39, 47, 55, 63,]
    array_left = [0,8,16,24,32,40,48,56]

    if ind in array_right:
        UrceniCisel(pole, ind, i, array2)
    elif ind in array_left:
        UrceniCisel(pole, ind, i, array3)
    else:
        UrceniCisel(pole, ind, i, array1)

def Board(pole):
    horizontal = " ----- ----- ----- ----- ----- ----- ----- -----"
    vertical = "|     |     |     |     |     |     |     |     |"
    s = 0
    while s < 63:
        print(horizontal)
        print(vertical)
        print(f"|  {pole[s]}  |  {pole[s+1]}  |  {pole[s+2]}  |  {pole[s+3]}  |  {pole[s+4]}  |  {pole[s+5]}  |  {pole[s+6]}  |  {pole[s+7]}  |")
        print(vertical)
        s += 8

def Hrac(hrac_column, hrac_row):
    if hrac_column <= 8 and hrac_row <= 8:
        position = ((hrac_column - 1) * 8) + (hrac_row - 1)
        return position
    else:
        pass


def ZmenaPole(pole, pole_result, hrac_column, hrac_row):
    try:
        position = Hrac(hrac_column, hrac_row)
        ukazat_hodnotu = pole_result[position]
        pole[position] = ukazat_hodnotu
        UrceniNuly(position, pole, pole_result, 0, position)
    except:
        pass

def UrceniNuly(position, pole, pole_result, i, pos):
        array = [+1,-1,+8,-8]
        try:
            if pole_result[position + array[i]] == 0 and (position + array[i]) >= 0:
                pole[position + array[i]] = 0
                UrceniNuly(position + array[i], pole, pole_result, i, pos)
            else:
                UrceniNuly(pos, pole, pole_result, i + 1, pos)
        except:
            pass

def OznaceniBomb(pole):
    x = int(input("Zadejte column: "))
    y = int(input("Zadejte row: "))
    if x <= 8 and y <= 8:
        position = Hrac(x,y)
        pole[position] = "B"
    else:
        pass

def ZjisteniBomb(pole, pole_result):
    pocet_bomb = 0
    pocet_bomb_pole = 0

    pocet_prazdnoty = 0

    sum_bomb = " "
    sum_bomb_result = " "

    index_bomb_result = []
    index_bomb = []

    for i in pole_result:
        if i == "*":
            pocet_bomb += 1
            index_bomb_result.append(str(pole_result.index(i)))
    for k in pole:
        if k == "B":
            pocet_bomb_pole += 1
            index_bomb.append(str(pole.index(k)))
        if k != " ":
            pocet_prazdnoty += 1
    for l in index_bomb:
        sum_bomb = sum_bomb + l
    for s in index_bomb_result:
        sum_bomb_result = sum_bomb_result + s

    if pocet_prazdnoty == 64 and pocet_bomb == pocet_bomb_pole and sum_bomb == sum_bomb_result:
        return False
    else:
        return True

def Bomba(pole, k):
    for i in pole:
        if i == "*":
            print("Prohrál jste")
            k = False
            return k




main()


