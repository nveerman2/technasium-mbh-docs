# Opdracht 4: Stappenmotor (28BYJ-48 met ULN2003 Driver)

In deze opdracht gaan we werken met de **28BYJ-48 stappenmotor** in combinatie met de **ULN2003 driver**.  

Een stappenmotor is een soort elektromotor die draait in stappen in plaats van continu. Dit maakt ze uitermate geschikt voor toepassingen waarbij precisie en controle over de rotatie vereist zijn, zoals in 3D-printers, CNC-machines en positioneringssystemen.

![stepper_types](../../../img/vaardigheden/arduino/stepper_types.jpg)

*Verschillende typen stappenmotoren*

> **Opmerking:** Deze opdracht kan niet in Tinkercad worden uitgevoerd. Zorg ervoor dat je de bedrading nauwkeurig uitvoert en dat je veiligheidsmaatregelen neemt bij het werken met elektrische componenten.  

---

## Fysieke Opdracht

**2.1** Voeg een Arduino Uno, een 28BYJ-48 stappenmotor en een ULN2003 driver toe aan het circuit.  
**2.2** Programmeer de Arduino om de stappenmotor in verschillende richtingen te laten draaien en met verschillende snelheden met de onderstaande code.  

![stepper_schema](../../../img/vaardigheden/arduino/stepper_schema.png)

> De stappenmotor kan rechtstreeks vanaf de Arduino worden gevoed maar dit wordt **niet aanbevolen** omdat de motor elektrische ruis op zijn voedingslijnen kan genereren wat de Arduino kan beschadigen.  

```cpp
// Voegt de ingebouwde Arduino Stepper-bibliotheek toe
#include <Stepper.h>

// Definieert het aantal stappen per omwenteling
const int stappenPerOmwenteling = 2038;

// Maakt een instantie van de stepper-klasse
// Pinnen ingevoerd in volgorde IN1-IN3-IN2-IN4 voor de juiste stapvolgorde
Stepper mijnStappenmotor = Stepper(stappenPerOmwenteling, 8, 10, 9, 11);

void setup() {
    // Niets te doen (Stepper-bibliotheek stelt pinnen in als uitgangen)
}

void loop() {
    // Draai met de klok mee langzaam op 5 RPM (omwentelingen per minuut)
    mijnStappenmotor.setSpeed(5);
    mijnStappenmotor.step(stappenPerOmwenteling);
    delay(1000);
    
    // Draai tegen de klok in snel op 10 RPM
    mijnStappenmotor.setSpeed(10);
    mijnStappenmotor.step(-stappenPerOmwenteling);
    delay(1000);
}
```

---

## Verwerkingsopdracht

**2.3** Voeg twee knoppen toe in de code die de stappenmotor elk in een andere richting en snelheid laten draaien.  

---

## Verder met de stappenmotor?

Wanneer je twee stappermotoren tegelijkertijd wilt laten draaien of de stappenmotor wilt laten versnellen of vertragen heb je een andere bibliotheek nodig.  

Zie voor dit en meer informatie over hoe een stappenmotor en de driver werkt op:  
🔗 [LastMinuteEngineers - 28BYJ-48 Stepper Motor Arduino Tutorial](https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/)  
