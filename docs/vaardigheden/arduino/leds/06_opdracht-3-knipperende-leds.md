# Opdracht 3: Knipperende LEDs

In deze opdracht leer je hoe je LEDs kunt laten knipperen met behulp van Arduino-code.  

---

## Tinkercad Opdracht

**3.1** Bouw de schakeling na zoals getoond in de afbeelding.  
**3.2** Probeer de code te begrijpen en te voorspellen wat er zal gebeuren voordat je hem uploadt naar je Arduino.  

![3_meerleds](../../../img/vaardigheden/arduino/3_meerleds.png)

---

## Code

```cpp
int ledPin1 = 13;
int ledPin2 = 12;

void setup() {
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
}

void loop() {
  digitalWrite(ledPin1, HIGH);
  digitalWrite(ledPin2, LOW);
  delay(1000);
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, HIGH);
  delay(1000);
}
```

---

## Verwerkingsopdracht

**3.3** Breid de schakeling en code uit met nog een LED, waarbij je de LEDs om en om laat knipperen.  
