leeftijd = input("Geef je leeftijd: ")
paspoort = input("Nederlands paspoort: (ja/nee) ")
if int(leeftijd) >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Helaas, je mag niet stemmen.")