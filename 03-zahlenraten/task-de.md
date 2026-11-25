# Zahlenraten

## Dein Ziel

Programmiere ein kleines Ratespiel: Eine Person gibt einen Tipp ab und dein Programm antwortet mit `Zu klein!`, `Zu groß!` oder `Richtig geraten!`.

## Deine Datei

Erstelle `zahlenraten.py` in diesem Aufgabenordner.

## Arbeitsauftrag

1. Lege eine feste Geheimzahl zwischen 1 und 20 in einer Variable ab. Sie bleibt während des Spiels gleich.
2. Zeige eine kurze Begrüßung mit dem Zahlenbereich an. Verrate die Geheimzahl dabei nicht.
3. Frage mit `input()` nach einem Tipp und wandle die Eingabe in einen Integer um.
4. Vergleiche den Tipp mit der Geheimzahl. Nutze `if`, `elif` und `else`, um genau eine der drei Rückmeldungen auszugeben.

Nach dieser Rückmeldung ist das Spiel beendet. Du darfst voraussetzen, dass eine ganze Zahl zwischen 1 und 20 eingegeben wird.

## Hilfe

- Mit `<`, `>` und `==` kannst du Zahlen vergleichen.
- Überlege vor dem Programmieren: Welche drei Fälle gibt es und wann trifft welcher Fall zu?
- Achte auf die Einrückung der Ausgaben innerhalb der Zweige.

## Teste dein Spiel

Starte das Programm für jeden Test neu. Wenn du zum Testen die Geheimzahl `13` festlegst, müssen diese Ergebnisse entstehen:

| Tipp | Rückmeldung |
| --- | --- |
| `8` | `Zu klein!` |
| `17` | `Zu groß!` |
| `13` | `Richtig geraten!` |

## Fertig, wenn

- der Tipp als Zahl mit der Geheimzahl verglichen wird
- jeder der drei Fälle die passende Rückmeldung auslöst
- pro Spiel genau ein Tipp abgefragt und genau eine Rückmeldung dazu ausgegeben wird
- du alle drei Fälle getestet hast

## Bonus: Zufällige Geheimzahl

Lass die Geheimzahl bei jedem Programmstart zufällig zwischen 1 und 20 wählen.

Zur Erinnerung – so habt ihr in ILP-21 eine Eventnummer erzeugt:

```python
import random

event_number = random.randint(1000, 9999)
```

`randint()` erzeugt eine ganze Zufallszahl einschließlich beider Grenzen. Passe das Beispiel für deine Geheimzahl an.
