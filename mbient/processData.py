from influxdb import InfluxDBClient, DataFrameClient
import numpy as np
import pandas as pd
import requests
import datetime
import time
import json
import os
import sys
import logging


def readOutput():

	# Set some boolean success variables for timer
	success = False
	## Go up one directory and to the output folder using shitty path functions
	output_path = os.path.join(os.getcwd(),'output')
	# Archive Path is where files are moved to after processing
	archive_path = os.path.join(os.getcwd(),'archive')

	#Read CSV Inventory of address names corresponding to user IDs
	df_sensors = pd.read_csv('mbientInventory.csv')
	df_sensors.set_index('serialNumber', inplace = True)

	# get list of csv file previous downloaded from the mbient sensor
	filenames = os.listdir(output_path)
	# filter the csvs
	csv_filenames = list(filter(lambda x: x.split('.')[-1] =="csv", filenames))


	# Itterate through csv files in output folder
	for filename in csv_filenames:
		print(filename)

		# Get device address
		address = filename.split('_')[2]

		# Get correspondinguserid 
		user_id = df_sensors.loc[address,  'participantID']

		sensor_location = df_sensors.loc[address, 'sensorLocation']
		

		#Read Data
		try:
			current_dataframe = pd.read_csv(os.path.join(output_path,filename))
		except pd.errors.EmptyDataError:
			print("WARNING: Empty CSV! Skipping")
			print(filename, "has no data, pease delete manually")
			continue

		#Set name of df to device address - may not be useful
		current_dataframe.name = address

		#--Time--
		#Get timestamp in correct format from epoch time 
		timestamp = pd.to_datetime(current_dataframe["epoc (ms)"], unit = 'ms')
		#Convert to Singapore time
		timestamp = timestamp.dt.tz_localize('utc').dt.tz_convert('Asia/Singapore') # use proper timezone
		#set index to timestamp and change name
		current_dataframe.index = timestamp
		current_dataframe.index.names = ["timestamp"]
		# Resampling data to average values of the same minute, and padding the rest with NANs
		current_dataframe = current_dataframe.resample("1min").mean() # make readings evenly 

		#Remove spaces, brackets and symbols from title
		column_names = current_dataframe.columns
		new_column_names = []
		for name in column_names:
			#remove unit
			new_name = name.split(' ')[: -1]
			#join with underscores
			new_name = "_".join(new_name)
			new_column_names.append(new_name)

		#reset column names with new tidier names
		current_dataframe.columns = new_column_names

		#Drop Epoch and Elapsed time from measurement
		current_dataframe =  current_dataframe.drop(['epoc', 'elapsed'], axis = 1)
		
		print(current_dataframe)



#Just in case we end up importing funcitons from this file
if __name__ == "__main__":
	readOutput()
