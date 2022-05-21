def samet_sort(karisik_liste):
    son_degisiklik_yeri = len(karisik_liste) - 1
    ilk_degisiklik_yeri = 0
    bitis = False
    a = 0
    while not bitis:
        bitis = True
        j = ilk_degisiklik_yeri
        while j < son_degisiklik_yeri:
            if karisik_liste[j] < karisik_liste[j+1]:
                karisik_liste[j], karisik_liste[j + 1] = karisik_liste[j + 1], karisik_liste[j]
                bitis = False
                ilk_degisiklik_yeri = max(j-1, 0)
                break
            j += 1
        while j < son_degisiklik_yeri:
            if karisik_liste[j] < karisik_liste[j + 1]:
                karisik_liste[j], karisik_liste[j + 1] = karisik_liste[j + 1], karisik_liste[j]
                a = j
            j += 1
        son_degisiklik_yeri = a
    return karisik_liste

karisik_liste = [-10, 42, 37, 100, 150, 55, 57, 56, 25, 27, 26, 26]
result = samet_sort(karisik_liste)
print(result)
