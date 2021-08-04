from application import db
from application.models import Results

db.drop_all()
db.create_all()
1 = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
2 = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
3 = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
4 = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
5 = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')

db.session.add(1)
db.session.add(2)
db.session.add(3)
db.session.add(4)
db.session.add(5)


db.session.commit()