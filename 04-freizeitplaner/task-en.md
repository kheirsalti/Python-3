# Activity Planner

Use `if/elif/else` to choose an outing that suits the weather.

## Task

Work in `freizeitplaner.py`. The inputs are prepared; add the decision.

The first matching rule applies:

1. Thunderstorm: `Ausflug absagen` (cancel the outing).
2. Rain or a temperature below 10 °C: `Drinnen bleiben` (stay indoors).
3. At least 28 °C and no shade: `Schattigen Ort suchen` (find a shady place).
4. Otherwise: `Draußen treffen` (meet outdoors).

Print exactly one of these texts. Combine conditions using `and`, `or`, and `not`. You may assume valid whole numbers and `ja` (yes) or `nein` (no). Restart the program for each test.

## Test cases

| Temperature | Thunderstorm | Rain | Shade | Result |
| --- | --- | --- | --- | --- |
| 30 | ja | ja | nein | Ausflug absagen |
| 20 | nein | ja | ja | Drinnen bleiben |
| 9 | nein | nein | ja | Drinnen bleiben |
| 10 | nein | nein | nein | Draußen treffen |
| 27 | nein | nein | nein | Draußen treffen |
| 28 | nein | nein | nein | Schattigen Ort suchen |
| 28 | nein | nein | ja | Draußen treffen |
| 30 | nein | ja | nein | Drinnen bleiben |

## Done when

- every test case produces the expected result
- exactly one plan appears per run
- you can explain why the order of the rules matters
