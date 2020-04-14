from app import db
class Users(db.Model):
    __tablename__ = 'users'
    idusers = db.Column('idusers', db.Integer, primary_key=True)
    email = db.Column('email', db.Unicode)
    password = db.Column('password', db.Unicode)
    call = db.Column('call', db.Integer)
    sms = db.Column('sms', db.Integer)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Reminders(db.Model):
    frequency = db.Column('frequency', db.Unicode)

    __tablename__ = 'reminders'
    idreminders = db.Column('idreminders', db.Integer, primary_key=True)
    idusers = db.Column('idusers', db.Integer)
    name = db.Column('name', db.Unicode)
    reminder = db.Column('reminder', db.Unicode)
    email = db.Column('email', db.Integer)
    text = db.Column('text', db.Integer)
    call = db.Column('call', db.Integer)
    datetime = db.Column('datetime', db.DateTime)
    completed = db.Column('completed', db.DateTime)