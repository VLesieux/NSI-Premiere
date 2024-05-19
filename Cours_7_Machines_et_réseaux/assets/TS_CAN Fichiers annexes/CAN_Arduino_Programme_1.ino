float  mesure = 0; // On définit une variable appelée "mesure" à laquelle on attribue la valeur 0

void setup() {
  Serial.begin(115200); // Ouvre une liaison avec le moniteur série afin de visualiser le résultat
                      // sur l'écran de l'ordinateur
}

void loop() {
  mesure = analogRead(0); //Met dans "mesure" la valeur lue par le CAN sur l'entrée A0 de la carte
  Serial.println(mesure); //Affiche la valeur lue par le CAN dans le moniteur série
  }


  
  
