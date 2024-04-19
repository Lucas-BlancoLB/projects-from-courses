from flask import Flask, render_template
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_babel import _

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
pass_list = {"admin@email.com": '12345678'}

class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), validators.Email(message=_("Please enter a valid email")),
                                                   validators.length(min=3, message=_('Little short for an email address?'))])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


app = Flask(__name__)
app.secret_key = 'super-secret-code'
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    form.validate_on_submit()

    if form.data['email'] in pass_list and form.data['password'] == pass_list[form.data['email']] and form.validate():
        return render_template('success.html')
    elif form.validate_on_submit():
        return render_template('denied.html')

    return render_template('login.html', form=form)





# ,methods=['POST','GET']
if __name__ == '__main__':
    app.run(debug=True)
