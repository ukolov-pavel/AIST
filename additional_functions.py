# -*- coding: utf-8 -*-
import datetime
from dateutil.relativedelta import relativedelta
import csv
import os
import pyodbc
import re
from settings import donor_min_age, donor_max_age
import operator
from selenium.webdriver.support.color import Color


def get_data(file_name, expansion='csv'):
	directory = os.getcwd() + '\\data\\'
	rows = []
	encoding_rows = []
	data_file = open(directory + file_name, 'rt', encoding='utf-8')
	if expansion == 'tsv':
		reader = csv.reader(data_file, delimiter='\t')
	elif expansion == 'csv':
		reader = csv.reader(data_file)
	next(reader, None)
	for row in reader:
		rows.append(list(row))
	for row in rows:
		encoding_rows.append([item.encode('utf-8').decode('utf-8') for item in row])
	return encoding_rows

def sql_query(query, stand='DRIVER={SQL Server};SERVER=10.32.200.142;DATABASE=aistdb_dev;UID=fmba.aist;PWD=fmba.aist'):#stand
	cnxn = pyodbc.connect(stand)
	cursor = cnxn.cursor()
	cursor.execute(query)
	result = cursor.fetchall()
	cursor.close()
	cnxn.close()
	return result

def convert_to_hex(color):
	hex_color = Color.from_string(color).hex
	return hex_color.upper()

def check_setting_xml(setting_path):#/SystemSettingsObj/WorkWithSocialStatus
	return sql_query(
		"DECLARE @settings xml; DECLARE @setting varchar; SET @settings = (SELECT cast(ParamXml AS xml) FROM ref.SystemSettingsXml);" + 
		"SET @setting =  @settings.value('("+setting_path+")[1]', 'varchar(100)' ); SELECT @setting")[0][0]

def check_setting(setting):
	return sql_query('select '+setting+' from ref.SystemSettings')[0][0]

def date_calculation(d): #'today - sys_min_age + one_day'
	x = d.split(' ')

	li = []

	for i in x:
		if i == 'today':
			i = datetime.date.today()
		elif i == 'sys_min_age':
			i = relativedelta(years=donor_min_age())
		elif i == 'sys_max_age':
			i = relativedelta(years=donor_max_age())
		elif i == 'one_day':
			i = relativedelta(days=1)
		elif i == 'one_year':
			i = relativedelta(years=1)
		elif i == 'ten_years':
			i = relativedelta(years=10)
		li.append(i)

	for i in li:
		if i == '-':
			li[li.index(i)]=operator.sub
		elif i == '+':
			li[li.index(i)]=operator.add

	res = li[0]

	operation = None

	for i in li[1:]:
		if i == operator.sub:
			operation = i
			pass
		elif i == operator.add:
			operation = i
			pass
		else:
			res = operation(res, i)

	return res.strftime('%d.%m.%Y')

def convert_phenotype(phenotype):
	phenotype = str(phenotype)
	ph = {0: 'C', 1: 'c', 2: 'Cw', 3: 'D', 4: 'E', 5: 'e'}
	values = {'1':'-', '2':'+', '3':'±', '4':'p'}
	res = ''
	while len(phenotype) < 6:
		phenotype = '0' + phenotype
	for index, i in enumerate(phenotype):
		if i != '0':
			res = res + ph[index]
			res = res + values[i]
	return res

def replace_phenotype(phenotype):
	dic = {'C+c+':'Cc', 'C+c-':'CC', 'C-c+':'cc', 'Cw+':'Cw', 'Cw-':'', 'D+':'D', 'D-':'dd', 'D±':'Dw', 'E+e+':'Ee', 'E+e-':'EE', 'E-e+':'ee'}
	for i in dic:
		if i in phenotype:
			phenotype = phenotype.replace(i, dic[i])
	return phenotype