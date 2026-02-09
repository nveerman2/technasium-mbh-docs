# For-loop

Een for-lus is als een herhalingsmachine voor de computer. Je vertelt hem waar hij moet beginnen, waar hij moet stoppen en hoeveel stappen hij elke keer moet zetten. Het is handig voor dingen die je herhaaldelijk moet doen, zoals tellen of herhalen van acties.  

Bijvoorbeeld:

![tinkercad_for](../../../img/vaardigheden/arduino/tinkercad_for.png)


```cpp
for (int i = 0; i < 10; i++) {
    // Doe iets hier
}
```

- `int i = 0` initialiseert een teller met de waarde 0.  
- `i < 10` bepaalt de voorwaarde waaronder de lus blijft doorgaan.  
- `i++` wordt na elke lusuitvoering gebruikt om de teller met 1 te verhogen.  

De code binnen de accolades `{}` wordt herhaald totdat de voorwaarde `i < 10` niet meer waar is. Dus in dit geval zal het "iets doen" 10 keer herhalen, omdat we beginnen bij 0 en doorgaan totdat we 9 hebben bereikt.  
