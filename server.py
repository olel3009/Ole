from flask import Flask, request, render_template

app = Flask(__name__)

# Variable zum Speichern des letzten Helligkeitswerts
lichtwert = "Noch keine Daten empfangen"

@app.route('/data', methods=['POST'])
def receive_data():
    global lichtwert
    lichtwert = request.form.get('lichtwert')
    print(f"Empfangene Helligkeit: {lichtwert}")
    return "OK", 200

@app.route('/get_light', methods=['GET'])
def get_light():
    return render_template('light.html', lichtwert=lichtwert)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
