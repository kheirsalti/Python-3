# Logikrätsel

Finde und korrigiere die Logikfehler. Teste deinen Code mit den angegebenen Fällen und erkläre jeden Fehler in einem Satz.

**Hinweis:** `not` kehrt einen Wahrheitswert um: `not True` ergibt `False`. Klammern fassen Bedingungen zusammen: Bei `not (a or b)` wird das Ergebnis der gesamten Klammer umgekehrt.

Arbeite in [starter/](starter/). Sage vor jedem Test die Ausgabe voraus, führe den Code aus und korrigiere ihn. Ändere zum Testen die Variablen oben in der Datei. Schreibe deine Erklärungen in `erklaerungen.md`.

## 1. Versandvorteil

`01-versand.py`: Kostenloser Versand gilt nur für Mitglieder mit einem Einkaufswert ab 50 Euro.

| basket_total | is_member | Erwartete Ausgabe |
| --- | --- | --- |
| 49 | False | Versand bezahlen |
| 49 | True | Versand bezahlen |
| 50 | False | Versand bezahlen |
| 50 | True | Kostenloser Versand |

## 2. Laden geöffnet?

`02-laden.py`: `is_closed` beschreibt, ob der Laden geschlossen ist. Gib den passenden Text aus.

| is_closed | Erwartete Ausgabe |
| --- | --- |
| True | Geschlossen |
| False | Geöffnet |

## 3. Alarm

`03-alarm.py`: Der Alarm soll nur auslösen, wenn die Anlage eingeschaltet und die Tür offen ist. `door_closed` ist bei geschlossener Tür `True`.

| door_closed | alarm_enabled | Erwartete Ausgabe |
| --- | --- | --- |
| True | True | Kein Alarm |
| True | False | Kein Alarm |
| False | True | Alarm |
| False | False | Kein Alarm |

## 4. Punktebewertung

`04-punkte.py`: Ab 80 Punkten gibt es Gold, ab 50 Silber, darunter Bronze. Es soll genau eine Bewertung erscheinen.

| points | Erwartete Ausgabe |
| --- | --- |
| 49 | Bronze |
| 50 | Silber |
| 79 | Silber |
| 80 | Gold |

## 5. Dateisynchronisierung

`05-synchronisierung.py`: Synchronisiere nur bei bestehender Verbindung und ausgeschalteter Pause. Zusätzlich muss es neue Dateien geben oder der manuelle Start aktiviert sein.

| is_online | has_new_files | force_sync | is_paused | Erwartete Ausgabe |
| --- | --- | --- | --- | --- |
| True | True | False | False | Synchronisieren |
| True | False | True | False | Synchronisieren |
| True | False | False | False | Warten |
| False | False | True | False | Warten |
| True | True | False | True | Warten |
| False | True | True | False | Warten |

## Fertig, wenn

- alle fünf Programme die Testfälle erfüllen
- du zu jedem Fehler eine kurze Erklärung notiert hast
