# Robot Hinderbana Workshop

[Switch to English](instructions-en.md)

Idag ska vi koda en robot att navigera genom en hinderbana.

Att koda är som att ge din robot en serie instruktioner att följa. Vi kommer att använda tre paneler för att göra detta:

- **Vänster Panel: Kodfilen.** Här skriver du dina instruktioner till roboten.
- **Nedersta Panelen: Chatt med Roboten.** Här skickar du kommandon till roboten.
- **Höger Panel: "Fusklapp".** Här finns all information du behöver.

## Robotens Chatt

Vi använder chatten för att skicka vår kod till roboten. Roboten kommer att läsa dina instruktioner och följa dem.

För att skicka din kod till roboten, skriv detta i chatten:

```plaintext
runonrobot code.py
```

Om roboten fortsätter och du vill att den ska sluta, tryck `CTRL+C` på ditt tangentbord för att stoppa den direkt.

## Instruktioner

Här är alla kommandon du kan ge roboten:

- `power`: Hur starkt roboten ska röra sig (från 0% till 100%).
- `duration`: Hur länge roboten ska utföra handlingen (i sekunder). Kom ihåg att använda `.` för decimaler i koden.

```python
robot.go.forward(power=80, duration=1.4)

robot.go.backward(power=80, duration=1.4)

robot.rotate.left(power=50, duration=0.2)

robot.rotate.right(power=50, duration=0.1)

robot.pause(duration=1)

robot.see.distance() # Roboten talar om hur långt den är från något
```