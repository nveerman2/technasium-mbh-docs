# Operatoren

Operatoren in programmeren zijn als speciale tekens die de computer vertellen wat te doen met getallen, letters of andere gegevens. Ze helpen ons om dingen te vergelijken, dingen samen te voegen, of dingen te veranderen. Denk aan operatoren als gereedschappen in een gereedschapskist die ons helpen om taken uit te voeren en problemen op te lossen.

## 1. Vergelijkingsoperatoren

- `==` (gelijk aan): Controleert of twee waarden gelijk zijn.  
- `!=` (niet gelijk aan): Controleert of twee waarden niet gelijk zijn.  
- `>` (groter dan): Controleert of de ene waarde groter is dan de andere.  
- `<` (kleiner dan): Controleert of de ene waarde kleiner is dan de andere.  
- `>=` (groter dan of gelijk aan): Controleert of de ene waarde groter is dan of gelijk is aan de andere.  
- `<=` (kleiner dan of gelijk aan): Controleert of de ene waarde kleiner is dan of gelijk is aan de andere.  

```cpp
if (a == b) { /* doe iets */ }
if (a != b) { /* doe iets */ }
if (a > b)  { /* doe iets */ }
if (a < b)  { /* doe iets */ }
if (a >= b) { /* doe iets */ }
if (a <= b) { /* doe iets */ }
```

## 2. Logische operatoren

- `&&` (en): Combineert twee voorwaarden waarvan beide waar moeten zijn.  
- `||` (of): Combineert twee voorwaarden waarvan minstens één waar moet zijn.  
- `!` (niet): Keert de waarde van een voorwaarde om.  

```cpp
if (a > 5 && a < 10) { /* doe iets */ }
if (a == 3 || a == 7) { /* doe iets */ }
if (!(a == b)) { /* doe iets */ }
```

## 3. Toekenningsoperatoren

- `=` (toekennen): Ken een waarde toe aan een variabele.  
- `+=`, `-=`, `*=`, `/=`: Voeg een waarde toe aan, trek een waarde af van, vermenigvuldig met, deel door de huidige waarde van de variabele en wijs het resultaat toe aan de variabele.  

```cpp
int a = 5;
a += 2; // is hetzelfde als a = a + 2;
```

## 4. Increment en decrement operatoren

- `++` (increment): Verhoog de waarde van een variabele met 1.  
- `--` (decrement): Verlaag de waarde van een variabele met 1.  

```cpp
a++; // is hetzelfde als a = a + 1;
a--; // is hetzelfde als a = a - 1;
```

---

In Tinkercad kun je de volgende blokken gebruiken onder **Rekenen**.

![operatoren](../../../img/vaardigheden/arduino/tinkercad_operatoren.png)
