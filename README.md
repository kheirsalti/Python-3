# Tagesaufgaben – Entscheidungen treffen

Bearbeitet die Aufgaben in dieser Reihenfolge: von Boolean-Werten über eigene Entscheidungen bis zur Fehlersuche.

1. **Zugangscheck:** Wiederholt Vergleiche und verknüpft Boolean-Werte. [Deutsch](01-zugangscheck/task-de.md) · [English](01-zugangscheck/task-en.md)
2. **Dateinamen-Check:** Prüft einen Dateinamen und gebt mit `if/else` eine passende Meldung aus. [Deutsch](02-dateinamen-check/task-de.md) · [English](02-dateinamen-check/task-en.md)
3. **Zahlenraten:** Reagiert mit `if/elif/else` auf einen einzelnen Tipp. Als Bonus lasst ihr die Geheimzahl zufällig wählen. [Deutsch](03-zahlenraten/task-de.md) · [English](03-zahlenraten/task-en.md)
4. **Freizeitplaner:** Verknüpft Bedingungen und entscheidet zwischen mehreren Möglichkeiten. [Deutsch](04-freizeitplaner/task-de.md) · [English](04-freizeitplaner/task-en.md)
5. **Logikrätsel:** Findet und korrigiert Fehler in fünf kleinen Programmen. [Deutsch](05-logikraetsel/task-de.md) · [English](05-logikraetsel/task-en.md)

Erstellt eure Python-Dateien im jeweiligen Aufgabenordner. Öffnet zum Testen ein WSL-Terminal in diesem Ordner und startet das Programm mit `python3 <dateiname>.py`. Ersetzt `<dateiname>` durch den Namen eurer Datei.

## Arbeitsablauf

Öffnet das WSL-Terminal und ersetzt `<URL-des-Repositories>` durch die URL eures GitHub-Repositories:

```bash
git clone <URL-des-Repositories> ILP-22
cd ILP-22
git switch solution
code .
```

Der Branch `solution` ist bereits vorbereitet. Löst dort eure Aufgaben in VS Code und testet eure Programme im WSL-Terminal.

Speichert am Ende eure Dateien und pusht die Ergebnisse aus dem Repository-Ordner auf den Branch `solution`:

```bash
git add .
git commit -m "Tagesaufgabe"
git push -u origin solution
```
