## Besturen van leds

### c-code voor Arduino

~~~c
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <string.h>

#define MAX_COMMAND_SIZE  100

#define BAUD_RATE 9600
#define BAUD_RATE_DIVISOR (F_CPU / 16 / BAUD_RATE - 1)

#define LOOP_TOT_BIT_SET(sfr, bit) do { } while (bit_is_clear(sfr, bit))

void serial_initialise()
{
    UCSR0A = 0 << TXC0 | 0 << U2X0 | 0 << MPCM0;
    UCSR0B =  1 << RXCIE0 | 0 << TXCIE0
            | 0 << UDRIE0
            | 1 << RXEN0 | 1 << TXEN0
            | 0 << UCSZ02
            | 0 << TXB80;
    UCSR0C =  0 << UMSEL01 | 0 << UMSEL00
            | 0 << UPM01 | 0 << UPM00
            | 0 << USBS0
            | 1 << UCSZ01 | 1 << UCSZ00
            | 0 << UCPOL0;
    UBRR0 = BAUD_RATE_DIVISOR;
}

void serial_send_byte(unsigned char data)
{
        LOOP_TOT_BIT_SET(UCSR0A, UDRE0);
        UDR0 = data;
}


void serial_send_string(char *s)
{
    while (*s) {
        serial_send_byte(*s);
        s++;
    }
}

void serial_send_number(int i)
{
    char s[25];
    itoa(i, s, 10);
    serial_send_string(s);
}

uint8_t serial_receive_byte(void) {
  loop_until_bit_is_set(UCSR0A, RXC0);       /* Wait for incoming data */
  return UDR0;                                /* return register value */
}


int read_command(char* line)
{
    int i = 0;
    while(1) {
      line[i] = serial_receive_byte();
      if (line[i] == ')' || i >= MAX_COMMAND_SIZE) break;
      i++;
    }
    line[i] = 0;
    return i-1;
}

char leds[] = {5,5};

int up(char* line)
{
    switch(line[3]) {
        case '0' : if(leds[0]<10) leds[0]++;return 0;
        case '1' : if(leds[1]<10) leds[1]++;return 1;
    }
    return -1;
}

int down(char* line)
{
    switch(line[5]) {
        case '0' : if(leds[0]>0) leds[0]--;return 0;
        case '1' : if(leds[1]>0) leds[1]--;return 1;
    }
    return -1;
}

int get(char* line)
{
    switch(line[4]) {
        case '0' : return 0;
        case '1' : return 1;
    }
    return -1;
}

void adapt_pwm(char number) {
    switch(number) {
        case 0 : OCR1A = 0xFFFF / 10 * leds[number];break;
        case 1 : OCR1B = 0xFFFF / 10 * leds[number];break;
    }
}

void execute_command(char* line)
{
    int led = -1;
    if(strncmp(line,"up",2) == 0) {
        led = up(line);
    } else if(strncmp(line,"down",4) == 0) {
        led = down(line);
    } else if(strncmp(line,"get",3) == 0) {
        led = get(line);
    } else {
        led = get(line);
    }

    if(led >= 0) {
        serial_send_number(led);
        serial_send_byte(';');
        serial_send_number(leds[led]);
        serial_send_byte('\n');
    }
}

int main(void) {
    DDRB |= (1 << DDB1) | (1 << DDB2); // PB1 and PB2 als output

    ICR1 = 0xFFFF; //TOP-waarde op 16-bit

    //Je hebt 2 uitgangen die je kan laten uitgaan bij ...
    OCR1A = 0xFFFF; // 25% duty cycle PB1
    OCR1B = 0xBFFF; // 75% duty cycle @ 16bit
    //TOP = 0xFFFF


    TCCR1A |= (1 << COM1A1) | (1 << COM1B1); // none-inverting mode

    // FAST PWM mode (16-bit) met ICR1 as TOP    1110
    TCCR1A |= (1 << WGM11);
    TCCR1B |= (1 << WGM12) | (1 << WGM13);

    // Voorlopig geen prescaler nodig (volle snelheid)
    TCCR1B |= (1 << CS10);

    serial_initialise();



    while (1) {
        char line[MAX_COMMAND_SIZE];
        read_command(line);
        execute_command(line);
        adapt_pwm(0);
        adapt_pwm(1);
    }
    return 0;
}
~~~

### Python-code

~~~python
from tkinter import *
from tkinter import scrolledtext
from time import sleep
import serial
from serial.tools.list_ports import *

class SerialConnection:
    def __init__(self,connection_string,baud):
        self.ser = serial.Serial(port=connection_string,
            baudrate=baud,
            bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1,
                        xonxoff=0,
                        rtscts=0)
        sleep(2)


    def write_command(self,command):
        self.ser.write(command.encode())
        val = self.ser.readline().decode()
        return val.split(';')[1]

class Led:
    def __init__(self,master,serial,led_number):
        self.led_number = led_number
        row_number = self.led_number        
        Button(master,text='-',command=self.decrement_led).grid(row=row_number,column=0)
        self.scale = Scale(master, from_=1, to=10,orient=HORIZONTAL)
        self.scale.grid(row=row_number,column=1)
        Button(master,text='+',command=self.increment_led).grid(row=row_number,column=2)
        self.command("get({})".format(self.led_number))

    def command(self,com):
        val = serial.write_command(com)
        self.scale.set(val)

    def increment_led(self):
        self.command("up({})".format(self.led_number))

    def decrement_led(self):
        self.command("down({})".format(self.led_number))

master = Tk()
master.geometry('350x350')
for port in comports():
    print(port.device)
    print(port.manufacturer)
    print(port.pid)
    print(port.vid)

serial = SerialConnection('COM3',9600)
led = Led(master,serial,0)
led = Led(master,serial,1)

# txt = scrolledtext.ScrolledText(master,width=70,height=20)
# txt.grid(column=0,row=3,columnspan="3")


mainloop()
~~~
