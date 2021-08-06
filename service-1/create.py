from application import db
from application.models import Results

db.drop_all()
db.create_all()

a = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
b = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
c = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
d = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
e = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')

db.session.add(a)
db.session.add(b)
db.session.add(c)
db.session.add(d)
db.session.add(e)


db.session.commit()