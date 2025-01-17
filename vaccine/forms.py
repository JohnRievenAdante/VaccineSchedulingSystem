from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField,DateField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from vaccine.models import user_information,hospital

cities = ['Alaminos', 'Bay', 'Biñan', 'Cabuyao','Calamba','Calauan','Cavinti','Famy','Kalayaan','Liliw',
    'Los Baños','Luisiana','Lumban','Mabitac','Magdalena','Majayjay','Nagcarlan','Paete','Pagsanjan','Pakil',
    'Pangil','Pila','Rizal','San Pablo','San Pedro','Santa Cruz','Santa Maria','Sta. Rosa','Siniloan','Victoria']
vactime=['1','2','3','4','5','6','7','8','9','10','11','12']
timeofday=['AM','PM']

class RegisterForm(FlaskForm):

    def validate_email_address(self, email_address_to_check):
        email_address = user_information.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')
    
    first_name = StringField(label='First Name:',validators=[DataRequired()])
    middle_name = StringField(label='Middle Name:')
    last_name = StringField(label='Last Name:',validators=[DataRequired()])
    city = SelectField(label='City:',choices=cities)
    home_address = StringField(label='Home Address:',validators=[DataRequired()])
    contact_number = StringField(label='Contact Number:',validators=[Length(max=6),DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    birthdate = DateField(label='Birth Date:',validators=[DataRequired()])
    password = PasswordField(label='Password:',validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    def validate_password(self, pass_to_check):
        password = user_information.query.filter_by(pwd=pass_to_check.data).first()
        
        if password == None:
            print("bro")
            raise ValidationError('Incorrect Password')

    emailadd = StringField(label='Email Address:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class AdminLoginForm(FlaskForm):
    def validate_hosid(self, pass_to_check):
        hosid = hospital.query.filter_by(hosp_id=pass_to_check.data).first()
        if hosid is None:
            raise ValidationError('Incorrect Password')
    hosname = StringField(label='Hospital Name:', validators=[DataRequired()])
    hosid = PasswordField(label='Hospital ID:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class UpdateItemForm(FlaskForm):
    submit = SubmitField(label='Update')
    delete = SubmitField(label='Delete')
    
class UpdateVaccineForm(FlaskForm):
    vaccinedate = DateField(label='Vaccine Date:')
    vaccinename=StringField(label='Vaccine Name:', validators=[DataRequired()])
    hospitalname=StringField(label='Hospital Name:', validators=[DataRequired()])
    time1=SelectField(label='Time:',choices=vactime)
    time2=SelectField(choices=vactime)
    ampm1=SelectField(label='Time:',choices=timeofday)
    ampm2=SelectField(choices=timeofday)
    submit = SubmitField(label='Update')
    addtime = SubmitField(label='Add New Schedule')

class AddVaccineForm(FlaskForm):
    vaccinedate = DateField(label='Vaccine Date:')
    vaccinename=StringField(label='Vaccine Name:', validators=[DataRequired()])
    submit = SubmitField(label='Add')