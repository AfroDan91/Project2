from flask import Flask, jsonify, request
import random

app = Flask(__name__)

names = ["Jack the ripper","Angry Dave", "Crazy Pat"]

@app.route('/get/estats')
def enemy_gen():
    names = ["Jack the ripper","Angry Dave", "Crazy Pat"]
    enemy_name = random.choice(names)
    attack = random.randint(1, 10)
    defence = random.randint(1, 10)
    estats = [enemy_name, attack, defence]

    return jsonify(estats)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
