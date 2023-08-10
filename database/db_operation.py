from numbers import Number

import psycopg2

from model.BeginnerBo import BeginnerBo
from model.Sentences import Sentences

hostname = "localhost"
u = "postgres"
db = "TransalationApp"
pwd = "Abhi123@."
port_id = 5432

conn = None
cur = None

def get_BegineerLevelInfo():
    conn = psycopg2.connect(dbname=db, user=u, host=hostname, password=pwd, port=port_id)

    lst = []

    cur = conn.cursor()

    statement = "select * from level_0"

    cur.execute(statement)

    records = cur.fetchall()

    if (len(records) > 0):
        for row in records:
            obj = BeginnerBo();
            obj.id = int(row[0])
            obj.english_sentence = str(row[1])
            strsentences = str(row[2])
            obj.translated_sentence = Sentences.from_dict(strsentences)
            lst.append(obj)

    if(cur is not None):
        cur.close()
    return lst
