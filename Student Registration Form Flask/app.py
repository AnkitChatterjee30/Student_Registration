from flask import Flask, request, render_template
app = Flask(__name__)

headings=('Name', 'Phone', 'Email-ID','City', 'Board','Stream', 'Marks')
data= [
    ('Ankit','9475937912','ankitchatterjee30@gmail.com','Durgapur','CBSE','Science','89.0'),
]
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/display",methods=['POST','GET'])
def display():
    name = request.form['fname']
    phone= request.form['phone']
    email = request.form['email']
    city = request.form['city']
    board = request.form['board']
    stream = request.form['stream']
    marks = str(float(request.form['percent']))
    lisg=[name, phone, email, city, board, stream, marks]
    data.append(tuple(lisg))
    return render_template("display.html", headings=headings, data= data)
@app.route("/register")
def register():
    science=[]
    commerce=[]
    humanities=[]
    for rows in data:
        if rows[5]=='Science' and rows[6]>='85':
            science.append(rows[0])
        elif rows[5]=='Commerce' and rows[6]>='75':
            commerce.append(rows[0])
        elif rows[5]=='Humanities' and rows[6]>='70':
            humanities.append(rows[0])
    return render_template("register.html", headings=headings, data= data, science=science, commerce=commerce, humanities=humanities)

if __name__=='__main__':
    app.run(debug=True)