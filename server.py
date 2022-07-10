from flask import Flask,render_template,request,redirect,session  # Import Flask to allow us to create our app
import random
# from datetime import datetime
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key='veryverysneaky'


@app.route('/')
def index():
    if 'money' in session:
        pass
    else:
        session['money'] =0
    print(session['money'])
    if 'activities' in session:
        pass
    else:
        session['acitivies'] ="Hello"
    return render_template("index.html", num_gold=session['money'])


@app.post('/process_money')
def gold():
    if request.form['button'] == 'farm':
        rand_int=random.randint(10,20)
    if request.form['button'] == 'cave':
        rand_int=random.randint(5,10)
    if request.form['button'] == 'house':
        rand_int=random.randint(2,5)
    if request.form['button'] == 'casino':
        rand_int=random.randint(-50,50)
    session['money'] +=rand_int
    return redirect("/")
#Earned {{message | safe}}from the "place"...message = "<ul><li>rand_int</li></ul>"

@app.route('/restart')
def restart_game():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


# from datetime import datetime

# # Getting the current date and time
# dt = datetime.now()

# # getting the timestamp
# ts = datetime.timestamp(dt)

# print("Date and time is:", dt)
# print("Timestamp is:", ts)