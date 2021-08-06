from flask import Flask, Response, request, jsonify, render_template
import requests
from . import app, db
from .models import Results


@app.route('/')
def main():
    # step 1: sends get requests to service 2 and 3 for player and enemy stats
    stats = [requests.get('http://service-3:5000/get/pstats').json(), requests.get('http://service-2:5000/get/estats').json()]
    

    # step 2: sends the results of the requests to 2 and 3 to service 4 for a winner
    result = requests.post('http://service-4:5000/post/who_won', json=stats).json()


    # step 3: pulls 5 previous results from the database.
    history = Results.query.order_by(Results.id.desc()).limit(5).all()  # pulls 5 previous results from the database.


    # step 4: gets the stats from services 2 and 3 and the result from service 4 and commits it to the database.
    new_res = Results(pname=stats[0][0], patt=stats[0][1], pdef=stats[0][2], ename=stats[1][0], eatt=stats[1][1], edef=stats[1][2], outcome=result)
    db.session.add(new_res)
    db.session.commit()

    # step5: passes the player stats, enemy stats, match results and 5 match history to the html template for rendering.
    return render_template("main.html", estats=stats[1], pstats=stats[0], result=result, history=history)