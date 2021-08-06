  
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from application import app, db
from application.models import Results

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db")
        return app

    def setUp(self):
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

    
    def tearDown(self):
        db.drop_all()


class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            m.get('http://service-2:5000/get/estats', json=['steve', 1, 1])
            m.get('http://service-3:5000/get/pstats', json=['bob', 5, 5])
            m.post('http://service-4:5000/post/who_won', json="Win")

            response = self.client.get(url_for('main'))

        self.assert200(response)
        self.assertIn('Win', response.data.decode())

# # Import the necessary modules
# from flask import url_for
# from flask_testing import TestCase
# from requests_mock import mock

# # import the app's classes and objects
# from application import app, db
# from application.models import Results



# class TestBase(TestCase):
#     def create_app(self):
#         app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db")
#         return app

#     def setUp(self):
#         db.create_all()
#         a = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
#         b = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
#         c = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
#         d = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')
#         e = Results(pname = 'good guy', patt = 4, pdef = 5, ename = 'bad guy', eatt = 1, edef = 1, outcome = 'Win')

#         db.session.add(a)
#         db.session.add(b)
#         db.session.add(c)
#         db.session.add(d)
#         db.session.add(e)

#         db.session.commit()

    
#     def tearDown(self):
#         db.drop_all()


# class TestRead(TestBase):
#     def test_main_layout(self):
#         response = self.client.get(url_for("main"))
#         assert "You" in response.data.decode()


# class TestCreate(TestBase):
#     def test_add_emp(self):
        
#         with self.client:
#             response = self.client.post(
#                 url_for("add_emp"),
#                 data={"emp_fname": "bob", "emp_lname": "bob", "emp_email": "bob", "works_in" :'departments'},
#                 #data=dict(emp_fname = "bob", emp_lname = "bob",  emp_email = "bob", dep_name =(1, 'Sales')),
#                 follow_redirects=True

#             )
#             #self.assertEqual(response.status_code, 200)
#             assert "bob" in response.data.decode()
#         #self.assertIn(b'bob', response.data)


          
# class testRead_dep(TestBase):
#     def test_departments(self):
#         response = self.client.get(url_for("dep"))
#         assert "Sales" in response.data.decode()


# class TestUpdate(TestBase):
#     def test_update_emp(self):
#         response = self.client.post(
#             url_for("update_role", id=1),
#             data=dict(departments=Departments(dep_name= 'Sales')),
#             follow_redirects=True
#             )
#         assert "Sales" in response.data.decode()


# class TestDel(TestBase):
#     def test_delete(self):
#         response = self.client.post(
#             url_for("del_emp", id=1),
#             follow_redirects=True
#             )
#         assert "Daniel" not in response.data.decode()
#         self.assertEqual(response.status_code, 200)









