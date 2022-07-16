import os
import sys
import psycopg2
from configparser import ConfigParser
from stage_db_clean import config

def read_sql():
    fd = open('stage_clean.sql', 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    return sqlCommands

def exec_db(sqL):
    for command in sqL[:-1]:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'{command}')
        conn.commit()
        print("DB Cleanup Done")
    
   
if __name__ == "__main__":
    #input2='preprod_stage'
    input2 = os.environ['ENV']
    print(input2)
    if (input2=='PRE-PROD'):
        params = config('preprod_stage','database.ini')
        sqL = read_sql()
        print(sqL)
        exec_db(sqL)
    elif (input2=='UAT'):
        params = config('uat_stage','database.ini')
        sqL = read_sql()
        print(sqL)
        exec_db(sqL)
    else:
        print("INVALID INPUT")
        
