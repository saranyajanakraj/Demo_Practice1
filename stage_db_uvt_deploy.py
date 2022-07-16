from configparser import ConfigParser
import psycopg2
import os

def config(filename='database.ini', section='uat_stage'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


params = config()

fd = open('stage_deploy.sql', 'r')
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')

print(sqlCommands)

for command in sqlCommands[:-1]:
    print(command)
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute(f'{command}')
    #rows = cur.fetchall()
    #print(rows)
    conn.commit()
