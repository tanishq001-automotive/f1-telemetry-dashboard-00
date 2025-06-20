from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

lap = 1
lap_data = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    global lap, lap_data

    if lap > 10:
        return jsonify(message="🏁 Race Finished", speed=0, temp=0, lap=lap - 1, pit="Yes")

    speed = random.randint(120, 340)
    temp = random.randint(80, 130)

    pit_stop = "Yes" if temp > 110 else "No"

    lap_data.append({
        "lap": lap,
        "speed": speed,
        "temp": temp,
        "pit": pit_stop
    })

    response = {
        "lap": lap,
        "speed": speed,
        "temp": temp,
        "pit": pit_stop
    }

    lap += 1
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
