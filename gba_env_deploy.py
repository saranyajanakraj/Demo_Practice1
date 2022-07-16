import os
import sys
import psycopg2
from configparser import ConfigParser
from stage_db_clean import config

def read_sql():
    fd = open('gba_db_deploy.sql', 'r')
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
        print("GBA DB Deploy completed")
    
   
if __name__ == "__main__":
    #input2='preprod_stage'
    input2 =os.environ['ENV']
    if (input2=='PRE-PROD'):
        params = config('preprod_gba','database.ini')
        sqL = read_sql()
        exec_db(sqL)
    else (input2=='UAT'):
        params = config('uat_gba','database.ini')
        sqL = read_sql()
        print(sqL)
        exec_db(sqL)
