davlatlar = ["Kanada", "Rossiya", "Ukraina", "Qozoqiston", "Turkiya", "Italiya", "Meksika"]
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
sonlar = list(range(120,1201,2))
print(sonlar)
summa = sum(sonlar)
print(summa)
maks = max(sonlar)
mini = min(sonlar)
ayirma = maks - mini
print(ayirma)
print(len(sonlar))
print(sonlar[:20])
print(sonlar[250:270])
print(sonlar[520:])
taomlar = ["Osh", "Muzqaymoq", "Tort", "Shashlik", "Non"]
nonushta = []
nonushta = taomlar[:]
print(taomlar)
print(nonushta)
nonushta.remove("Osh")
nonushta.remove("Shashlik")
nonushta.append("Murabbo")
nonushta.append("Kofe")
print(nonushta)
print(taomlar)



