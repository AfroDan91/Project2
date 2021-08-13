from flask import Flask, jsonify, request
import random

app = Flask(__name__)

names = ["Steve the King", "Evan Almighty", "Thor"]
response3 = requests.get("https://api.parser.name/?api_key=25d97a94cfff505ad3b2a732cf9b2496&endpoint=generate").json()

@app.route('/get/pstats')
def player_gen():

    player_name = response3['data'][0]['name']['firstname']['name']
    attack = random.randint(1, 10)
    defence = random.randint(1, 10)
    pstats = [player_name, attack, defence]

    return jsonify(pstats)


if __name__ == '__main__':
    app.run(host='0.0.0.0')