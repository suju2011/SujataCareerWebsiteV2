

from sqlalchemy import *
from sqlalchemy import create_engine, text
from sqlalchemy. util.langhelpers import dictlike_iteritems

db_connection_string= "mysql+pymysql://9jncxfu9se9pl456yzu3:pscale_pw_HqBfx4MqB4vkAExOgZNnm2snPlj12yQO3sVxF6AWBT0@aws.connect.psdb.cloud/sujatacareers?charset=utf8mb4"
engine = create_engine(db_connection_string,
                    connect_args={"ssl":{"ssl ca": "/etc/ssl/cert.pem"}})

def load_jobs_from_db():

  with engine.connect() as conn:
  
    result = conn.execute(text("select * from jobs"))
   
    jobs=[]   
    for row in result.all():
      jobs.append(row._asdict())
    return jobs