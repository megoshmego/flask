from flask import Flask, request, render_template, redirect
from random import choice, randint, sample
from flask_debugtoolbar import DebugToolbarExtension


COMPLIMENTS = ["COOL", "CLEVER", "TENACIOUS", "PYTHONIC", "AWESOME"]


app = Flask(__name__)
app.config['SECRET_KEY'] = "mego"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return "Helloo there!"
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/form')
def show_form():
    return render_template("form.html")
 
@app.route('/greet')
def get_greeting():   #make sure to put this in the route you want to send this to, see form.html ln 11
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliments=nice_thing)
    
@app.route('/jinja')
def say_jinja():
    return render_template("jinja.html")



@app.route('/form2')
def show_form_2():
    return render_template("form2.html") 



@app.route('/greet2') #looping example
def get_greeting_2():
    username = request.args["username"]
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3) if wants else []
    return render_template("greet2.html", username=username, wants_compliments=wants, compliments=nice_things)

@app.route('/lucky') #render_template ex., with random number
def lucky_number():
    num = randint(1, 10)
    return render_template('lucky.html', lucky_num=num, msg="You are so lucky!")

@app.route('/spell/<word>')  #for loop
def spell_word(word):
    caps_word = word.upper()
    return render_template("spellword.html", word=caps_word)

@app.route('/old-home-page') #redirect 
def redirect_to_home():
    """
    redirects to home
    """
    return redirect("/")

@app.route("/childtemplate")
def my_page():
    """Show my page, example of template inheritance"""
    return render_template("childtemplate.html")