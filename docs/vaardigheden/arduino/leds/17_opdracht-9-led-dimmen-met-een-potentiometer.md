# Opdracht 9: LED dimmen met een potentiometer

In deze opdracht leer je hoe je de helderheid van een LED kunt regelen met behulp van een potentiometer.  
Door de draaiknop van de potentiometer te veranderen, pas je de weerstand aan, wat resulteert in een verandering van de helderheid van de LED.  

---

## Tinkercad Opdracht

**9.1** Bouw de schakeling na zoals getoond in de afbeelding.  
**9.2** Programmeer de Arduino om de waarde van de potentiometer uit te lezen en de helderheid van de LED dienovereenkomstig aan te passen.  

![9_dimmen_circuit](../../../img/vaardigheden/arduino/9_dimmen_circuit.png)

![9_dimmen_code](../../../img/vaardigheden/arduino/9_dimmen_code.png)

---

## Code

```cpp
int sensorValue = 0; // Variabele om de waarde van de sensor op te slaan

void setup()
{
  pinMode(A0, INPUT); // Stel pin A0 in als een invoerpin voor de sensor
  pinMode(9, OUTPUT); // Stel pin 9 in als een uitvoerpin voor de LED
  Serial.begin(9600); // Start de communicatie met de Serial Monitor op een baudrate van 9600
}

void loop()
{
  // Lees de waarde van de sensor, vertaal deze naar een waarde tussen 0 en 255 voor de LED en sla op in sensorValue
  sensorValue = map(analogRead(A0), 0, 1023, 0, 255);
  
  // Stuur de sensorValue naar de Serial Monitor met daarna een nieuwe regel
  Serial.println(sensorValue);
  
  // Pas de helderheid van de LED aan op basis van de waarde van de sensorValue
  analogWrite(9, sensorValue);
  
  // Wacht een korte periode voordat de volgende meting wordt uitgevoerd
  delay(10); 
}
```

---

## Fysieke Opdracht

**9.3** Bouw dezelfde schakeling met een fysieke Arduino, een breadboard, een LED en een potentiometer.  
Sluit de potentiometer aan op een analoge pin van de Arduino en de LED op een PWM-pin.  
Programmeer de Arduino met dezelfde code die je hebt gebruikt in Tinkercad en observeer hoe de helderheid van de LED verandert terwijl je aan de potentiometer draait.  
