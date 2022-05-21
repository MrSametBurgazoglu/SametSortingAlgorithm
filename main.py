def samet_sort(karisik_liste):
    son_degisiklik_yeri = len(karisik_liste) - 1
    bitis = False
    while not bitis:
        j = 0
        a = son_degisiklik_yeri
        bitis = True
        while j < son_degisiklik_yeri:
            if karisik_liste[j] < karisik_liste[j + 1]:
                karisik_liste[j], karisik_liste[j + 1] = karisik_liste[j + 1], karisik_liste[j]
                a = j
                bitis = False
            j += 1
        son_degisiklik_yeri = a
    return karisik_liste

karisik_liste = [42, 37, 100, 150, 55, 57, 56, 25, 27, 26]
result = samet_sort(karisik_liste)
print(result)
