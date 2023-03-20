from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template("form.html", methods = ['GET']) 

@app.route('/login')
def login():
  user, password = request.args.get('nm'), request.args.get('snm')
  if  user == 'admin' and password == 'xxx123#':
    return render_template("login.html", user = user) 
  else:
    return render_template("errore.html") 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

# if request.method == 'POST':
#     user = request.form['nm']
#      return redirect(url_for('success',name = user))
#   else:
#      user = request.args.get('nm')
#      return redirect(url_for('success',name = user))