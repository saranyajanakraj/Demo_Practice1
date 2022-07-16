import os
import sys
import psycopg2
from configparser import ConfigParser
def main():
#   input1 =os.environ['Branch']
   input2 =os.environ['ENV']
#   print(input1)
   print(input2)
   if (input2=='PRE-PROD'):
      print('SQL GENERATION FOR PRE_PROD ENVIRONMENT')
   else:
      print('SQL GENERATION FOR UAT ENVIRONMENT')
if __name__ == "__main__":
   print('Welcome to SQL GENERATION STAGE')
main()
