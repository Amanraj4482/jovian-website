from flask import Flask
#the smaller one is called the module and the Flask is called the class
app=Flask(__name__)
#this app is the obj of the Flask cls
# when a certain url is req what should be returned
# jovian.ai/[path/route]
# we add which path we wanted to match
@app.route("/")#/ is the empty route which is home page of the jovian-carrier.ai
def hello_World():
  return "hello_World"


if __name__=="__main__""
  app.run(host="0.0.0.0",debug=True)