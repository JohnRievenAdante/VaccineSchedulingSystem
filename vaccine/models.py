from vaccine import db

from flask_login import UserMixin

class user_information(db.Model):
    user_id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(length=45))
    middle_name=db.Column(db.String(length=45))
    last_name=db.Column(db.String(length=45))
    city=db.Column(db.String(length=45))
    home_address=db.Column(db.String(length=45))
    birthdate=db.Column(db.Date)
    contact_number=db.Column(db.String(length=45))
    email_address=db.Column(db.String(length=45))
    pwd=db.Column(db.String(length=45))

    def __repr__(self):
        return "id: {0} | first name: {1} | middle name: {2} | last name: {3} | city: {4} | home address: {5} | email address: {6} | password: {7} | contact number: {8} | birth date: {9}".format(self.user_id,self.first_name,self.middle_name,self.last_name,self.city,self.home_address,self.email_address,self.pwd,self.contact_number,self.birth_date,)

#connector=db.Table('availability_details',),db.Column('vac_id',db.Integer,db.ForeignKey('vaccine.vaccine_id'),
#db.Column('hospital_id',db.Integer,db.ForeignKey('hospital.hosp_id'))

class availability_details(db.Model):
    __tablename__="availability_details"

    id = db.Column(db.Integer, primary_key=True)
    vac_id=db.Column('vac_id',db.Integer,db.ForeignKey('vaccine.vaccine_id'))
    hospital_id=db.Column(db.Integer,db.ForeignKey('hospital.hosp_id'))
    sched=db.Column(db.Integer,db.ForeignKey('avail.schedule_id'))

    v=db.relationship("vaccine", back_populates="availability_details")
    a=db.relationship("avail")
    h=db.relationship("hospital", back_populates="availability_details")

class vaccine(db.Model):
    __tablename__="vaccine"
    vaccine_id=db.Column(db.Integer,primary_key=True)
    vaccine_name=db.Column(db.String(length=255))

    vaccine_hos=db.Column(db.Integer(),db.ForeignKey('hospital.hosp_id'))
    schedules = db.relationship('avail', backref='all_schedules', lazy=True)
    #following = db.relationship('hospital',secondary=connector,backref='followers')
    availability_details = db.relationship("availability_details", back_populates="v")

    def __repr__(self):
        return f'<User: {self.vaccine_name}>'

class hospital(db.Model):
    __tablename__="hospital"
    hosp_id=db.Column(db.Integer,primary_key=True)
    hosp_name=db.Column(db.String(length=45))
    hosp_address=db.Column(db.String(length=255))
    vac = db.relationship('availability_details', backref='vac_names', lazy=True)
    
    def __repr__(self):
        return f'<User: {self.hosp_name}>'
    availability_details = db.relationship("availability_details", back_populates="h")
    #scheds = db.relationship('avail', backref='hosp_vaccine', lazy=True)

class avail(db.Model):
    schedule_id=db.Column(db.Integer,primary_key=True)
    availability_date=db.Column(db.Date)
    availability_time=db.Column(db.String(length=45))
    vac=db.Column(db.Integer,db.ForeignKey('vaccine.vaccine_id'))
    hos = db.Column(db.Integer(), db.ForeignKey('hospital.hosp_id'))