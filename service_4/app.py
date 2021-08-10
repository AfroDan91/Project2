from flask import Flask, jsonify, request
import random

app = Flask(__name__)


@app.route('/post/who_won', methods=['POST'])
def who_won():
    
    p = request.json[0]
    e = request.json[1]


    if p[1] + p[2] >= e[1] + e[2]:
        winner = "Win"
    elif e[1] + e[2] > p[1] + p[2]:
        winner = "Loss"
    else:
        winner = "Draw"

    return jsonify(winner)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')