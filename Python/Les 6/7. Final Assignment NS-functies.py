def standaardprijs(afstandKM):
    if afstandKM >= 50:
        return 15 + (afstandKM * 0.60)
    elif afstandKM <= 0:
        return 0
    else:
        return afstandKM * 0.8

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaard = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == True:
            return standaard * 0.65
        else:
            return standaard * 0.70
    else:
        if weekendrit == True:
            return standaard * 0.6
        else:
            return standaard

leeftijd = int(input("Leeftijd: "))
weekend = ""
while weekend != "y" and weekend != "n":
    weekend = input("Reist u in het weekend: (y/n): ")
    if weekend == "y":
        weekendrit = True
    elif weekend == "n":
        weekendrit = False
    else:
        print("Verkeerde waarde! (voer y of n in)")
afstandKM = int(input("Hoeveel KM reist u?: "))


print ("U betaalt ", round(ritprijs(leeftijd, weekendrit, afstandKM), 2), "Euro voor u reis.")