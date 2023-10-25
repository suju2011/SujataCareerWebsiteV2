from flask import Flask, render_template, jsonify
from database import load_jobs_from_db,load_job_from_db #this load_job_from_db is another app

# by importing the load_job functin from database file and removing the sqlalchemy from here and the engine also

# from sqlalchemy import text
app = Flask(__name__)

# JOBS=[
#   {
#     'id':1,
#     'title':'Data Analyst',
#     'location':'Bangaluru, India',
#     'Salary':'Rs. 10,00,000'
  
#   },
#   {
#     'id':2,
#     'title':'Data Scientist',
#     'location':'Delhi, India',
#     'Salary':'Rs. 15,00,000'
  
#   },
  
#   {
#     'id':3,
#     'title':'FrontEnd Engineer',
#     'location':'Remote'
#     # 'Salary':'Rs. 12,00,000'
  
#   },
#   {
#     'id':4,
#     'title':'BackEnd Engineer',
#     'location':'SanFrancisco, USA',
#     'Salary':'$ 120,00'
  
#   }
  
  
# ]
# Instead of having 2 database file and its details in different file we should call the function from database .py file to import just the function here by importing
# def load_jobs_from_db():

#   with engine.connect() as conn:

#     result = conn.execute(text("select * from jobs"))
#     # result_dicts=[]
#     jobs=[]   # as this is a list of job so replaced the name by job and changed accordingly
#     for row in result.all():
#       # result_dicts.append(row._asdict())
#       jobs.append(row._asdict())
#     return jobs

@app.route("/")
def hello_sujata():
  jobs=load_jobs_from_db()
  return render_template('home.html',jobs=jobs,company_name='SujataCareers')
  # return render_template('home.html',jobs=JOBS,company_name='SujataCareers')

@app.route("/api/jobs")
def list_jobs():
  jobs=load_jobs_from_db()
  return jsonify(jobs)
  
# @app.route("/job/<id>")
# def show_job(id):
#   job=load_jobs_from_db(id)
#   return jsonify(job)


@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_from_db(id)  # Use the correct function to load a specific job
    if job is None:
        return "Job not found", 404
    else:
        return jsonify(job)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
