import pyodbc
import additional_functions
from base import BaseTest

def sql(query):
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.32.200.142;DATABASE=aistdb_dev;UID=fmba.aist;PWD=fmba.aist')
	cursor = cnxn.cursor()
	cursor.execute(query).commit()

#Минимальный возраст донора в системе
def donor_min_age():
	return additional_functions.sql_query("select donorminage from ref.systemsettings")[0][0]

#Максимальный возраст донора в системе
def donor_max_age():
	return additional_functions.sql_query("select donormaxage from ref.systemsettings")[0][0]