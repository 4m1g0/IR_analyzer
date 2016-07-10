unsigned long last = 0;
unsigned long now = 0;
int i = 0;
const int N = 1000;

boolean chart[N];
boolean store = 0;

unsigned long counter = 0;

void setup (void)
{
   Serial.begin(9600);
}

void loop (void)
{
  now =  micros();

  if (last + 10 < now) {
    int value = digitalRead(11);
    ++counter *= value; // incrementamos si value = 1 ponemos a 0 si value = 0

    if (value)
      store = 1;

    if (counter > N)
      store = 0;
      
    if (store){
      chart[i++] = value;
      if (i > N-1){
        for (i = 0;i<N;i++)
          Serial.print(chart[i]);
        i=0;
      }
    }
    last = now;
  }
}
