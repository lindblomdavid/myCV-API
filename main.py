from replit import db
import json
from flask import Flask
from flask import request

app = Flask(__name__)

  
@app.route('/', methods =['GET'])
def handle_request():
  relevantdata = str(request.args.get('input'))
  if relevantdata == "education":
    return getEducation()
  elif relevantdata == "experience":
    return getExperience()
  elif relevantdata =="other":
    return getOther()
  else:
    return "You can query the API using by adding:  '/?input=' followed by the queryparameter. Example: '/?input=education' for education. Current options are [education, experience, other]"
  



def getEducation():
  education_keys = db.prefix("ED")
  data_set = {}
  for key in education_keys:
    data_set[key]={'School':db[key][0],'Degree': db[key][1], 'Major': db[key][2], 'City':db[key][3],'fromyear':db[key][4], 'Toyear':db[key][5]}
    json
   
  return json.dumps(data_set)
  


    
def getExperience():
  experience_keys = db.prefix("EX")
  data_set = {}
  for key in experience_keys:
    data_set[key]={'Company':db[key][1],'Position': db[key][2], 'Takeback 1': db[key][3], 'Takeback 2':db[key][4],'Takeback 3':db[key][5], 'Takeback 4':db[key][6], 'City':db[key][7],'Fromyear': db[key][8],'Toyear': db[key][9]}
    
   
  return json.dumps(data_set)
  
def getOther():
  other_keys = db.prefix("OT")
  data_set = {}
  for key in other_keys:
    data_set[key] = {"Description": db[key][1]}

  return json.dumps(data_set)



print(getOther())




















app.run(host='0.0.0.0', port=8080)