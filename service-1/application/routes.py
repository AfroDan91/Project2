from flask import Flask, Response, request, jsonify
from . import app, db
from .models import Results


@app.route('/')
def main():
    # estats = requests.get('http://service-2:5000/get/estats').json()
    # pstats = requests.get('http://service-3:5000/get/pstats').json()

    # sends get requests to service 2 and 3 for player and enemy stats
    stats = [pstats = requests.get('http://service-3:5000/get/pstats').json(), requests.get('http://service-2:5000/get/estats').json()]
    
    # sends the results of the requests to 2 and 3 to service 4 for a winner
    result = requests.post('http://service-4:5000/post/who_won', json=stats).json()

    # pulls 5 previous results from the database.
    history = Results.query.order_by(Results.id.desc()).limit(5).all()  # pulls 5 previous results from the database.

    # gets the stats from services 2 and 3 and the result from service 4 and commits it to the database.
    new_res = Results(pname=pstats[0], patt=pstats[1], pdef=pstats[2], ename=estats[0], eatt=estats[1], edef=estats[2], outcome=result)
    db.session.add(new_res)
    db.sesson.commit()

    # renders the html page to display all information.
    return render_template("main.html", estats=estats, pstats=pstats, result=result, history=history)