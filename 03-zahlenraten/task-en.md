# Guess the Number

## Your goal

Build a small guessing game: a person enters a guess and your program responds with `Zu klein!` (too low), `Zu groß!` (too high), or `Richtig geraten!` (correct).

## Your file

Create `zahlenraten.py` in this exercise directory.

## Task

1. Store a fixed secret number between 1 and 20 in a variable. It stays the same throughout the game.
2. Display a short welcome message with the number range. Do not reveal the secret number in this message.
3. Ask for a guess using `input()` and convert the input to an integer.
4. Compare the guess with the secret number. Use `if`, `elif`, and `else` to print exactly one of the three responses.

The game ends after this response. You may assume that the input is a whole number between 1 and 20.

## Help

- You can compare numbers using `<`, `>`, and `==`.
- Before coding, consider the three possible cases and when each one applies.
- Pay attention to the indentation of the output inside each branch.

## Test your game

Restart the program for each test. If you set the secret number to `13` for testing, these should be the results:

| Guess | Response |
| --- | --- |
| `8` | `Zu klein!` |
| `17` | `Zu groß!` |
| `13` | `Richtig geraten!` |

## Done when

- the guess is compared with the secret number as a number
- each of the three cases produces the appropriate response
- each game asks for exactly one guess and prints exactly one response to it
- you have tested all three cases

## Bonus: Random secret number

Let the program randomly choose the secret number between 1 and 20 each time it starts.

As a reminder – this is how you generated an event number in ILP-21:

```python
import random

event_number = random.randint(1000, 9999)
```

`randint()` generates a random whole number including both limits. Adapt the example for your secret number.
