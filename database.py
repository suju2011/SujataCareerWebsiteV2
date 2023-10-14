# print(sqlalchemy.__version__ )

# from sqlalchemy import *
from sqlalchemy import create_engine, text
# from sqlalchemy import create_engine #removing text from here and add to app.py

# from sqlalchemy.util.langhelpers import dictlike_iteritems

# to create an engine to connect to the database Copy from site:https://docs.sqlalchemy.org/en/20/dialects/mysql.html
# engine = create_engine("mysql+pymysql://splk2f787s61havomk4o:pscale_pw_z794BUqR7aMq8QfiZO3yY7gAYoa70fkTIE6chdNY4cB@aws.connect.psdb.cloud/sujatacareers?charset=utf8mb4")

# Setting the creat engine in a string and called in engine to create it. and also putting another ssl to be created in the engine to run the code and avoide error "ssl"

# not working so had to change the password by creating a new one
# db_connection_string= "mysql+pymysql://splk2f787s61havomk4o:pscale_pw_z794BUqR7aMq8QfiZO3yY7gAYoa70fkTIE6chdNY4cB@aws.connect.psdb.cloud/sujatacareers?charset=utf8mb4"
db_connection_string= "mysql+pymysql://3ncqll7dzlaqoatzy7dz:pscale_pw_mrejLJ5Bfg6r1e2dPZbFFfN4FbU4aWGCpNX44RcMpB1@aws.connect.psdb.cloud/sujatacareers?charset=utf8mb4"
engine = create_engine(db_connection_string,
                    connect_args={"ssl":{"ssl ca": "/etc/ssl/cert.pem"}})

# with engine.connect() as conn:

#   result = conn.execute(text("select * from jobs"))
   
 
#   '''
#   print("1. type (result) : ",type(result))

#   result_all=result.all()
#   print("2. type(result.all()) : ",type(result_all))
#   # print("result.all() : ",result_all)
#   print("3. 1st entry : ",result_all[0])
#   first_result = result_all[0]
#   print("4. Type of 1st entry : ",type(first_result))
#   # how to convert sqlalchemy row into python dictionary : search in stackoverflow
  
#   # first_result_dict = dict(result_all[0])
#   # we are having issue with this dict function as its unable convert dictionary update sequence element #0 to a sequence, so using chart gpt i found it runs well as using .asdict() which makes dict function able to convert the above issue
#   first_result_dict = result_all[0]._asdict()
#   print("5. Type of 1st entry : ",type(  first_result_dict))
#   print("6. 1st entry : ",  first_result_dict)
# '''

# # now we can use this 1dictionary to call all the dictionaries values
#   result_dicts=[]
#   for row in result.all():
#     result_dicts.append(row._asdict())
  # print("7. ", result_dicts)
  
  


# For creating a database to link inthe cloud we need the above 11 lines of code to import into main python file


# Instead of having 2 database file and its details in different file we should call the function from database .py file to import just the function here by importing
def load_jobs_from_db():

  with engine.connect() as conn:
  
    result = conn.execute(text("select * from jobs"))
    # result_dicts=[]
    jobs=[]   # as this is a list of job so replaced the name by job and changed accordingly
    for row in result.all():
      # result_dicts.append(row._asdict())
      jobs.append(row._asdict())
    return jobs