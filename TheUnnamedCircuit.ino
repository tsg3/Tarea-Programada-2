//  _ ___ _______     ___ ___ ___  ___ _   _ ___ _____ ___ 
// / |_  )__ /   \   / __|_ _| _ \/ __| | | |_ _|_   _/ __| 
// | |/ / |_ \ |) | | (__ | ||   / (__| |_| || |  | | \__ \ 
// |_/___|___/___/   \___|___|_|_\\___|\___/|___| |_| |___/ 
// 
// The Unnamed Circuit
// 
// Made by Esteban Campos Granados
// License: CC-BY-SA 3.0
// Downloaded from: https://circuits.io/circuits/5114656-the-unnamed-circuit

int boton2 = 2;
int boton3 = 3;
int boton4 = 4;
int boton5 = 5;
int boton6 = 6;
void setup() {
  Serial.begin(9600);
  pinMode(boton2, INPUT);
  pinMode(boton3, INPUT);
  pinMode(boton4, INPUT);
  pinMode(boton5, INPUT);
  pinMode(boton6, INPUT);
}

void loop() {
  int buttonState2 = digitalRead(boton2); 
  int buttonState3 = digitalRead(boton3);
  int buttonState4 = digitalRead(boton4);
  int buttonState5 = digitalRead(boton5);
  int buttonState6 = digitalRead(boton6);
  if (buttonState2 == 1){ Serial.println(1); }
  if (buttonState3 == 1){ Serial.println(2); }
  if (buttonState4 == 1){ Serial.println(3); }
  if (buttonState5 == 1){ Serial.println(4); }
  if (buttonState6 == 1){ Serial.println(5); }
  delay(100);        
}
