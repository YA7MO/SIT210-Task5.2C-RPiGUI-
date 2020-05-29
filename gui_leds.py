from tkinter import *
from gpiozero import LED

green_led = LED(3)
blue_led = LED(2)
red_led = LED(4)

def green():
    blue_led.off()
    red_led.off()
    green_led.on()
    print("green")
    
def blue():
    print("blue")
    blue_led.on()
    red_led.off()
    green_led.off()
        
def red():
    print("red")
    red_led.on()
    blue_led.off()
    green_led.off()
    
    
win = Tk()
win.title("GUI LEDS")

greenbtn = Radiobutton(win, text = "Green" ,value = "greenLed",bg = "green" ,command = green, height = 1, width = 10)
greenbtn.pack()
bluebtn = Radiobutton(win, text = "Blue", value = "blueLed", bg = "blue" ,command = blue, height = 1, width = 10)
bluebtn.pack()
redbtn = Radiobutton(win, text = "Red" ,value = "redLed", bg = "red" ,command = red, height = 1, width = 10)
redbtn.pack()
win.mainloop()

