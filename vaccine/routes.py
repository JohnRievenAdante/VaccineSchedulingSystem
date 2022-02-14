from vaccine import app, db
from flask import Flask, render_template,redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from vaccine.models import availability_details, user_information,hospital,vaccine,avail
from flask_login import current_user,login_user, logout_user, login_required 
from vaccine.forms import RegisterForm,LoginForm, UpdateVaccineForm, AddVaccineForm,AdminLoginForm,UpdateItemForm
from wtforms.validators import ValidationError

@app.route ("/")
def Home():
    return render_template("Home.html", content="Test")

@app.route ("/ScheduleAppointment")
def ScheduleAppointment():
    return render_template("ScheduleAppointment.html", content="Test")

@app.route ("/ViewAppointment")
def ViewAppointment():
    return render_template("ViewAppointment.html", content="Test")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        attempted_user = user_information.query.filter_by(email_address=form.emailadd.data).first()
        if attempted_user:
            
            flash(f'Success! You are logged in as: {attempted_user.email_address}', category='success')
            return redirect(url_for('ViewAppointment'))
    if form.errors != {}: 
        flash('Incorrect Email or Passowrd, Try Again', category='danger')

    return render_template('login.html',form=form)

@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    form = AdminLoginForm()
    
    if form.validate_on_submit():
        
        attempted_user = hospital.query.filter_by(hosp_name=form.hosname.data).first()
        if attempted_user:
            
            flash(f'Success! You are logged in as: {attempted_user.hosp_name}', category='success')
            return redirect(url_for('index'))

    if form.errors != {}: 
        flash('Incorrect Name or Password, Try Again', category='danger')
    return render_template('login_admin.html',form=form)

@app.route('/update')
def index():
    s=[]
    items =  hospital.query.filter_by(hosp_name='asas Rosa Hospital').first()
    #items1 =  vaccine.query.filter_by(vaccine_name='man').first()
    #assoc = availability_details(v=items1, h=items)
    #u=  vaccine(vaccine_name='man')
    #m=  hospital(hosp_name='asas Rosa Hospital',hosp_address='masdasd')

    #items1.following.append(items)
    #db.session.commit()
       
    #vaccine1= items.followers #outputs vaccine affiliated with 'items'
    #hosp1=items1.following #outputs hospital affiliated with 'items1'
    for i in items.availability_details:
        if i.v is None:
            continue
        
        else:
            print(i.h," hos")
            print(i.v," vac")
            s.append(i.v)

    
    return render_template('index.html',s=s)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        
        #email_address = user_information.query.filter_by(email_address=form.email_address.data).first()
        #if email_address:
        #    raise ValidationError('Email Address already exists! Please try a different email address')
        user=user_information(first_name=form.first_name.data,middle_name=form.middle_name.data,last_name=form.last_name.data,
        city=form.city.data,home_address=form.home_address.data,email_address=form.email_address.data,pwd=form.password.data,
        contact_number=form.contact_number.data,birthdate=form.birthdate.data)
        db.session.add(user)
        db.session.commit()
    
        flash(f'Success! You are registered', category='success')
    if form.errors != {}: 
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))

@app.route('/updatevaccine')
def updatevaccine():
    s=[]
    form = UpdateVaccineForm()
    items =  hospital.query.filter_by(hosp_name='asas Rosa Hospital').first()
    items1 =  vaccine.query.filter_by(vaccine_name='AstraZeneca').first()
    for i in items1.availability_details:
        if i.v is None:
            continue
        else:
            s.append(i.a)
    
    return render_template('update.html', form=form,s=s)

@app.route('/addvaccine')
def addvaccine():
    form = AddVaccineForm()
    #if form.validate_on_submit():
     #   attempted_user = availability_details.query.filter_by(email_address=form.emailadd.data).first()
      #  if attempted_user:
            
       #     flash(f'Success! You are logged in as: {attempted_user.email_address}', category='success')
        #    return redirect(url_for('index'))
        #else:
         #   flash('Username and password are not match! Please try again', category='danger')
    return render_template('add.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
