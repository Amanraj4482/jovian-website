from flask import Flask,render_template,jsonify
#the smaller one is called the module and the Flask is called the class
# this app is the obj of the Flask cls
app=Flask(__name__)
# when a certain url is req what should be returned
# jovian.ai/[path/route]
# we add which path we wanted to match
JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengluru , India',
    'salary':'Rs. 1,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi , India',
    'salary':'Rs. 15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    # 'salary':'Rs. 12,00,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'SanFrancisco ,USA',
    'salary':'$ 120,000'
  }
]
@app.route('/')#/ is the empty route which is home page of the jovian-carrier.ai
def create_app():
  # return "HELLO"
  return render_template('home.html',
               jobs=JOBS,
               company_name='Jovian')
@app.route("/api/jobs")#returns the structured data in form of the json which can be progrically analysed
def list_jobs():
  return jsonify(JOBS)
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)