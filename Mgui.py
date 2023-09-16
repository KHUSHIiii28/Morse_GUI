import RPi.GPIO as GPIO
import time
import tkinter as tk

#Morse code dictionary
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

ledPin = 14 #Output pin is set at GPIO14 (Pin 8 as board pin)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

def dot():
    GPIO.output(ledPin, 1)
    time.sleep(0.2)
    GPIO.output(ledPin, 0)
    time.sleep(0.2)

def dash():
    GPIO.output(ledPin, 1)
    time.sleep(0.5)
    GPIO.output(ledPin, 0)
    time.sleep(0.2)

def morse_code_blink(input_text):
    for letter in input_text:
        for symbol in CODE.get(letter.upper(), ''):
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
            else:
                time.sleep(0.5)
        time.sleep(0.5)

def send_button_clicked():
    user_input = input_entry.get()
    morse_code_blink(user_input)

#GUI Window 
root = tk.Tk()
root.title("Morse Code LED Blinker")

#Label creation 
label = tk.Label(root, text="Enter text to send in Morse Code:")
label.pack()

#Creating entry widget 
input_entry = tk.Entry(root)
input_entry.pack()

#Creating send button
send_button = tk.Button(root, text="Send Morse Code", command=send_button_clicked)
send_button.pack()

#Running the GUI main loop
root.mainloop()

