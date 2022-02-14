from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField,DateField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

cities = ['Alaminos', 'Bay', 'Biñan', 'Cabuyao','Calamba','Calauan','Cavinti','Famy','Kalayaan','Liliw',
    'Los Baños','Luisiana','Lumban','Mabitac','Magdalena','Majayjay','Nagcarlan','Paete','Pagsanjan','Pakil',
    'Pangil','Pila','Rizal','San Pablo','San Pedro','Santa Cruz','Santa Maria','Sta. Rosa','Siniloan','Victoria']
vactime=['1','2','3','4','5','6','7','8','9','10','11','12']
timeofday=['AM','PM']

class RegisterForm(FlaskForm):

    first_name = StringField(label='First Name:',validators=[DataRequired()])
    middle_name = StringField(label='Middle Name:')
    last_name = StringField(label='Last Name:',validators=[DataRequired()])
    city = SelectField(label='City:',choices=cities)
    home_address = StringField(label='Home Address:',validators=[DataRequired()])
    contact_number = StringField(label='Contact Number:',validators=[Length(max=6),DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    birthdate = DateField(label='Birth Date:')
    password1 = PasswordField(label='Password:',validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    emailadd = StringField(label='Email Address:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class AdminLoginForm(FlaskForm):
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