from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bangaluru, India',
    'Salary':'Rs. 10,00,000'
  
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'Salary':'Rs. 15,00,000'
  
  },
  
  {
    'id':3,
    'title':'FrontEnd Engineer',
    'location':'Remote'
    # 'Salary':'Rs. 12,00,000'
  
  },
  {
    'id':4,
    'title':'BackEnd Engineer',
    'location':'SanFrancisco, USA',
    'Salary':'$ 120,00'
  
  }
  
  
]

@app.route("/")
def hello_sujata():
  return render_template('home.html',jobs=JOBS,company_name='SujataCareers')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
