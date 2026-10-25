from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    I_am_alive = "Bot is running!"
    return I_am_alive

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
  
