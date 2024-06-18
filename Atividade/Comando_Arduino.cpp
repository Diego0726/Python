void setup() {
  Serial.begin(9600);

  //Quando for Executar o respectivo programa não esquecer de ajustar os PINOS
  pinMode(,OUTPUT); // PINO LAMPADA
  pinMode(,OUTPUT); // PINO VENTILADOR
  pinMode(,OUTPUT); // PINO FECHADURA
  
}
void loop() {

    //Validação de um comando em formato de String
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    

    // LAMPADA
    if (command == "Texto_lampada_ligar") {
      digitalWrite(, HIGH);
    } 
    else if (command == "Texto_lampada_desligar") {
      digitalWrite(, LOW);
    }
   
   
    //Ventilador
    if (command == "Texto_ventilador_ligar") {
      digitalWrite(, HIGH);
    } 
    else if (command == "Texto_ventilador_desligar") {
      digitalWrite(, LOW);


    //Fechadura
    if (command == "Texto_fechadura_abrir") {
      digitalWrite(, HIGH);
    } 
    else if (command == "Texto_fechadura_fechar") {
      digitalWrite(, LOW);
    }

    }
  }
}

