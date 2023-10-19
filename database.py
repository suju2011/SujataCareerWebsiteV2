

from sqlalchemy import *
from sqlalchemy import create_engine, text
from sqlalchemy. util.langhelpers import dictlike_iteritems

db_connection_string= "mysql+pymysql://rg2xekqkiuofmsizmv9r:pscale_pw_QW4kxAky9CQvERWIVYh3Uzfi99XVTajkQEyia6lI3bT@aws.connect.psdb.cloud/careers?charset=utf8mb4"
engine = create_engine(db_connection_string,
                    connect_args={"ssl":{"ssl ca": "/etc/ssl/cert.pem"}})

def load_jobs_from_db():

  with engine.connect() as conn:
  
    result = conn.execute(text("select * from jobs"))
   
    jobs=[]   
    for row in result.all():
      jobs.append(row._asdict())
    return jobs