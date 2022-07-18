import os
import sys
import psycopg2
from configparser import ConfigParser
from connection_config import config

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
        
    
   
if __name__ == "__main__":
    #input2='preprod_stage'
    input2 =os.environ['ENV']
    if (input2=='PRE-PROD'):
        params = config('preprod_gba','database.ini')
        sqL = read_sql()
        exec_db(sqL)
        print("GBA DB Deploy completed")
    elif (input2=='UAT'):
        params = config('uat_gba','database.ini')
        sqL = read_sql()
        print(sqL)
        exec_db(sqL)
        print("GBA DB Deploy completed") 
    else:
        print("INVALID INPUT")
