

import os

from sqlalchemy import *
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']
# SETTING THE DATABASE DETAILS SECRATE TO US ONLY
# db_connection_string= "mysql+pymysql://vb0x6hpuomu9q7d275xq:pscale_pw_imckS4hZZHfbxmn8kcUVdObckpgKHIe1i3Tr39ElUo@aws.connect.psdb.cloud/careers?charset=utf8mb4"
engine = create_engine(db_connection_string,
                    connect_args={"ssl":{"ssl ca": "/etc/ssl/cert.pem"}})

def load_jobs_from_db():

  with engine.connect() as conn:
  
    result = conn.execute(text("select * from jobs"))
   
    jobs=[]   
    for row in result.all():
      jobs.append(row._asdict())
    return jobs