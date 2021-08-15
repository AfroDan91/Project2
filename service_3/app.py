from flask import Flask, jsonify, request
import random

app = Flask(__name__)

names = ["IRON MAN", "GOOD GUY MCGOO", "JESUS"]

@app.route('/get/pstats')
def player_gen():

    player_name = random.choice(names)
    attack = random.randint(1, 10)
    defence = random.randint(1, 10)
    pstats = [player_name, attack, defence]

    return jsonify(pstats)


if __name__ == '__main__':
    app.run(host='0.0.0.0')