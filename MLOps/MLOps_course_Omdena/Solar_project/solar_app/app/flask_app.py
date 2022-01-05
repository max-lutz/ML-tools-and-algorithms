'''
inputs: month, day, Daily_Temp, Daily_Precip, Daily_Humidity, Daily_Pressure, Daily_WindDir,
        Daily_WindSpeed, Daily_DNI, Daily_DHI

output: Daily_radiation
'''

# import modules
from flask import Flask, jsonify, request
import pandas as pd
import joblib
from app.preprocessing_functions import log_transform

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_input():
    '''
    Flask script to interface between user request and ml model selected during POC    
    '''
    # load packets
    packet = request.get_json(force=True)
    print(packet)

    # extract and reshape input data
    #input_data = list(packet.values())

    #print(input_data)

    # reshape data
    data = pd.DataFrame(packet, index=[0])

    print(data)

    # load the ml model
    model_path = 'app/rf_model.joblib'
    model = joblib.load(model_path)

    # generate prediction
    solar_irr = model.predict(data)[0]

    return jsonify(packet, {'Solar irradiation':solar_irr})