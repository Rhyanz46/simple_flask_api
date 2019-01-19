from app import db, User

data = User(username='haha', foto='hehe')
db.session.add(data)
db.session.commit()

data = User(username='dede', foto='dede')
db.session.add(data)
db.session.commit()



