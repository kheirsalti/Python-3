# Logic Puzzles

Find and fix the logic errors. Test your code with the given cases and explain each error in one sentence.

**Hint:** `not` reverses a Boolean value: `not True` gives `False`. Parentheses group conditions: `not (a or b)` reverses the result of the entire group.

Work in [starter/](starter/). Predict the output before each test, run the code, and fix it. Change the variables at the top of each file to test it. Write your explanations in `erklaerungen.md`.

## 1. Shipping benefit

`01-versand.py`: Free shipping applies only to members with a basket total of at least 50 euros.

| basket_total | is_member | Expected output |
| --- | --- | --- |
| 49 | False | Versand bezahlen |
| 49 | True | Versand bezahlen |
| 50 | False | Versand bezahlen |
| 50 | True | Kostenloser Versand |

`Versand bezahlen` means pay for shipping; `Kostenloser Versand` means free shipping.

## 2. Shop open?

`02-laden.py`: `is_closed` describes whether the shop is closed. Print the matching text.

| is_closed | Expected output |
| --- | --- |
| True | Geschlossen |
| False | Geöffnet |

`Geschlossen` means closed; `Geöffnet` means open.

## 3. Alarm

`03-alarm.py`: The alarm should sound only when the system is enabled and the door is open. `door_closed` is `True` when the door is closed.

| door_closed | alarm_enabled | Expected output |
| --- | --- | --- |
| True | True | Kein Alarm |
| True | False | Kein Alarm |
| False | True | Alarm |
| False | False | Kein Alarm |

`Kein Alarm` means no alarm.

## 4. Score rating

`04-punkte.py`: At least 80 points earns Gold, at least 50 earns Silber (silver), and anything below earns Bronze. Print exactly one rating.

| points | Expected output |
| --- | --- |
| 49 | Bronze |
| 50 | Silber |
| 79 | Silber |
| 80 | Gold |

## 5. File synchronisation

`05-synchronisierung.py`: Synchronise only when connected and not paused. In addition, there must be new files or a manual start must be activated.

| is_online | has_new_files | force_sync | is_paused | Expected output |
| --- | --- | --- | --- | --- |
| True | True | False | False | Synchronisieren |
| True | False | True | False | Synchronisieren |
| True | False | False | False | Warten |
| False | False | True | False | Warten |
| True | True | False | True | Warten |
| False | True | True | False | Warten |

`Synchronisieren` means synchronise; `Warten` means wait.

## Done when

- all five programs pass the test cases
- you have written a short explanation for each error
