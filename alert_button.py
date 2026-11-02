from dotenv import load_dotenv
import requests as rq
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
load_dotenv()
print("Alert button monitoring system is now active. Press Ctrl+C to stop.")

jsson = {
    "chat_id": os.getenv("CHAT_ID"),
    "text": "Someone pressed the alert button!"
}

print(os.getenv("BOT_TOKEN"),  os.getenv("CHAT_ID"))

button_pressed = False
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed:
            ans = rq.post("".join(["https://api.telegram.org/bot", os.getenv("BOT_TOKEN"), "/sendMessage"]), json=jsson)
            print(ans)
            button_pressed = True
        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nMonitoring stopped.")
    GPIO.cleanup()
