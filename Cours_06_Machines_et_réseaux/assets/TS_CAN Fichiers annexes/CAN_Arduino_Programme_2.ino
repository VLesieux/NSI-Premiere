float mesure[200] ={}; // On définit un tableau de variables appelée "mesure" pouvant contenir jusque 201 données et laissé vide pour l'instant
int instant[200] = {}; // On définit un tableau de variables appelée "instant" pouvant contenir jusque 201 données et laissé vide pour l'instant
int Te = 10 ; // Définit la valeur de la période d'échantillonnage Te en ms (valeur à prendre entre 10 ms et 200 ms)
float pas = 0.01; // Définit le pas en V (valeur à prendre entre 0,00489 V et 5.00 V)
float tension = 0;   // Définit une variable tension = 0
float arrondi = 0;   // Définit une variable arrondi = 0


void setup() {
  Serial.begin(57600); // Ouvre une liaison avec le moniteur série afin de récupérer les données sur l'écran de l'ordinateur
}


void loop() { 
for (int i=0;i<2000/Te; i++) {  //Boucle d'acquisition de mesures durant 2 s
   tension = analogRead(0)/1023.0000*5.0000; //Met dans tension la valeur lue par le CAN sur l'entrée A0 de la carte, convertie en V
   arrondi=int(tension/pas); // la valeur de "arrondi" est égale à la partie entière de (tension/pas)
   mesure[i] = arrondi*pas; // met dans la mesure n° i la valeur de (arrondi*pas)
   instant[i] = i*Te;   // met dans instant n° i la valeur de l'instant d'échantillonnage
   delay(Te);  //Attend la durée de la période d'échantilllonnage Te
   }
  
for (int i=0;i<2000/Te; i++) {  //Boucle d'envoi des données vers le moniteur série
   Serial.print(instant[i]); //Affiche l'instant n°i de prise de la mesure dans le moniteur série
   Serial.print(";");         //affiche un séparateur entre instant et mesure
   Serial.println(mesure[i]); //affiche la mesure n°i dans le moniteur série
   }
delay(10000); //Attend 10 s avant de refaire une série de mesures
}


  
  
