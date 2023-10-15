

from sqlalchemy import *
from sqlalchemy import create_engine, text
from sqlalchemy. util.langhelpers import dictlike_iteritems

db_connection_string= "mysql+pymysql://ia7y7c9ekp5mp5zlxh4n:pscale_pw_ASO7wmpcHt1L0DaHw4FmAOGYaDRQ2akqsvd5zTD4N7f@aws.connect.psdb.cloud/sujatacareers?charset=utf8mb4"
engine = create_engine(db_connection_string,
                    connect_args={"ssl":{"ssl ca": "/etc/ssl/cert.pem"}})

def load_jobs_from_db():

  with engine.connect() as conn:
  
    result = conn.execute(text("select * from jobs"))
   
    jobs=[]   
    for row in result.all():
      jobs.append(row._asdict())
    return jobs