from replit import db

#Function to add education, follows structure ED1,ED2
def addEducation(school, degree, major, city, fromyear, toyear):
  id = "ED" + str(len(db.prefix("ED")) + 1)
  db[id] = [school, degree, major, city, fromyear, toyear]
  return print("added a new entry to the database: " + str(db[id])) 

#Function to add Experience, ID follows structure EX1,EX2
def addExperience(company,position,bp1,bp2,bp3,bp4,city,fromyear,toyear =  "N/A"):
  id = "EX" + str(len(db.prefix("EX")) + 1)
  db[id] = [id,company,position,bp1,bp2,bp3,bp4,city,fromyear,toyear]
  return print("added a new entry to the database: " + str(db[id]))


def addOther(*args):
  id = "OT"+ str(len(db.prefix("OT")) + 1)
  db[id] = [id, *args]
  return print("added a new entry to the database: " + str(db[id]))


addOther("Recipient of the Huayu Enrichment Scholarship awarded by the Taiwan's Ministry of Education, financing one year of languages studies in Taiwan 2013.")
addOther("Previous member of the Nova 100 student Talent network in Stockholm.")
addOther("Member of the Swedish Chambers of Commerce team of Young Professionals in Taipei, Taiwan, 2013-2014.")
addOther("Personal interest in programming, able to create simple applications and scripts in programming languages such as Python and Javascript.")

