# == "ja" vergleicht die Eingabe mit dem Text "ja".
# Das Ergebnis wird gespeichert: True bei genau "ja", sonst False.

temperature = int(input("Temperatur in °C: "))
has_thunderstorm = input("Gewitter? (ja/nein): ") == "ja"
is_raining = input("Regen? (ja/nein): ") == "ja"
has_shade = input("Schatten vorhanden? (ja/nein): ") == "ja"

# Ergänze hier deine Entscheidung. / Add your decision here.
if has_thunderstorm == "ja":
    print("Ausflug absagen")
elif is_raining == "ja" or temperature < 10:
    print("Drinnen bleiben")
elif temperature >= 28 and has_shade =="ja":
    print("Schattigen Ort suchen")
else :
    print("Draußen treffen")    