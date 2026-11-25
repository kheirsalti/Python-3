# Freizeitplaner

Entscheide mit `if/elif/else`, welcher Ausflugsplan zum Wetter passt.

## Arbeitsauftrag

Arbeite in `freizeitplaner.py`. Die Eingaben sind vorbereitet; ergänze die Entscheidung.

Die erste passende Regel zählt:

1. Bei Gewitter: `Ausflug absagen`.
2. Bei Regen oder einer Temperatur unter 10 °C: `Drinnen bleiben`.
3. Ab 28 °C und ohne Schatten: `Schattigen Ort suchen`.
4. Sonst: `Draußen treffen`.

Gib genau einen dieser Texte aus. Verbinde die Bedingungen mit `and`, `or` und `not`. Du darfst gültige ganze Zahlen sowie `ja` oder `nein` voraussetzen. Starte das Programm für jeden Test neu.

## Testfälle

| Temperatur | Gewitter | Regen | Schatten | Ergebnis |
| --- | --- | --- | --- | --- |
| 30 | ja | ja | nein | Ausflug absagen |
| 20 | nein | ja | ja | Drinnen bleiben |
| 9 | nein | nein | ja | Drinnen bleiben |
| 10 | nein | nein | nein | Draußen treffen |
| 27 | nein | nein | nein | Draußen treffen |
| 28 | nein | nein | nein | Schattigen Ort suchen |
| 28 | nein | nein | ja | Draußen treffen |
| 30 | nein | ja | nein | Drinnen bleiben |

## Fertig, wenn

- jeder Testfall das passende Ergebnis liefert
- pro Ausführung genau ein Plan erscheint
- du erklären kannst, warum die Reihenfolge der Regeln wichtig ist
