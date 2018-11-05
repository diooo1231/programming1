def kwadraten_som(grondgetallen):
    somkwadraat=0
    for i in grondgetallen:
        if i > 0:
            somkwadraat += (i ** 2)
    return somkwadraat

print (kwadraten_som([4, 5, 3, -81]))