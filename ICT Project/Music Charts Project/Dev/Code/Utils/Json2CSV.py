"""
Dublin Business School
Student: Daniel Pereira (10391381@mydbs.ie)
ICT PROJECT
________________________________________________________________________________

This file is a simple python code to convert a json into CSV file
"""

##################################################
import pandas as pd

def convert_chart_to_csv(input_json, output_csv):
    try:
        print("*** Json to CSV: started - file: ", input_json)
        dataset_charts = pd.read_json(input_json)
        
        # convert the date column to the correct date format
        dataset_charts = dataset_charts.assign(chart_week=pd.to_datetime(dataset_charts['chart_week']))
        dataset_charts.to_csv(output_csv, index = None)
        print("*** Json to CSV: finished")
    except Exception as e:
        print("Error: {0}".format(e))   


## initial load code
if __name__ == '__main__':
    convert_chart_to_csv('Dataset/OfficialUKCharts.json', 'Dataset/OfficialUKCharts.csv')



