#!/usr/bin/env python3

from click.testing import CliRunner
import ev_group46
import urllib3
import json
import os
from os.path import expanduser
urllib3.disable_warnings()

home = expanduser("~")	#https://stackoverflow.com/questions/4028904/how-to-get-the-home-directory-in-python		
path_of_token = "%s/softeng20bAPI.token" % home

def test_healthcheck():
	runner = CliRunner()
	result = runner.invoke(ev_group46.healthcheck)
	assert result.exit_code == 0
	assert result.output == 'we are connected with the database\n'
	
def test_login():
	runner = CliRunner()
	result = runner.invoke(ev_group46.Login, ['--username', 'admin', '--passw' ,'petrol4ever'])
	assert result.exit_code == 0
	assert result.output == 'login was successful\n'
	
	
def test_SessionsPerPoint():
	runner = CliRunner()
	token_file = open(path_of_token, 'r')
	tok = json.load(token_file)
	apikey = tok['token']
	result = runner.invoke(ev_group46.SessionsPerPoint, ['--point', '5f69795300355e4c010658b6_119350', '--datefrom', '20190901', '--dateto', '20190902', '--apikey', apikey])
	#print(result.output)
	assert result.exit_code == 0
	assert '0.747' in result.output
	
def test_SessionsPerStation():
	runner = CliRunner()
	token_file = open(path_of_token, 'r')
	tok = json.load(token_file)
	apikey = tok['token']
	result = runner.invoke(ev_group46.SessionsPerStation, ['--station', '5f69795300355e4c010658b6', '--datefrom', '20190901', '--dateto', '20190902', '--apikey', apikey])
	#print(result.output)
	assert result.exit_code == 0
	assert '0.747' in result.output
	
def test_SessionsPerProvider():
	runner = CliRunner()
	token_file = open(path_of_token, 'r')
	tok = json.load(token_file)
	apikey = tok['token']
	result = runner.invoke(ev_group46.SessionsPerProvider, ['--provider', '(Business Owner at Location)', '--datefrom', '20190901', '--dateto', '20190902', '--apikey', apikey])
	#print(result.output)
	assert result.exit_code == 0
	assert '0.747' in result.output
	
def test_SessionsPerEV():
	runner = CliRunner()
	token_file = open(path_of_token, 'r')
	tok = json.load(token_file)
	apikey = tok['token']
	result = runner.invoke(ev_group46.SessionsPerEV, ['--ev', '926efa33-4c55-43df-80f3-4b8d2d65a00a', '--datefrom', '20190901', '--dateto', '20190902', '--apikey', apikey])
	print(result.output)
	assert result.exit_code == 0
	assert '0.747' in result.output

def test_logout():
	runner = CliRunner()
	token_file = open(path_of_token, 'r')
	tok = json.load(token_file)
	apikey = tok['token']
	result = runner.invoke(ev_group46.logout, ['--apikey', apikey])
	assert result.exit_code == 0
	assert result.output == 'logout was successful\n'

