from flask import Flask ,request,render_template
import numpy as np
import pandas as pd
import pickle

#loading models
rfc = pickle.load(open('rfc.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

#creating Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('DriverIndex.html')
@app.route('/Predict',methods=['POST'])
def predict():
    if request.method=='POST':
        Abs_Throttle_Position = request.form['Abs_Throttle_Position']
        Engine_RPM = request.form['Engine_RPM']
        Vehicle_Speed = request.form['Vehicle_Speed']
        Abs_Load_Value = request.form['Abs_Load_Value']

        input_data = pd.DataFrame({
            'Abs_Throttle_Position': [Abs_Throttle_Position],
            'Engine_RPM': [Engine_RPM],
            'Vehicle_Speed': [Vehicle_Speed],
            'Abs_Load_Value': [Abs_Load_Value]
        })

        transformed_data = scaler.fit_transform(input_data)
        predicted_value = rfc.predict(transformed_data)[0]

        return render_template('DriverIndex.html',predicted_value=predicted_value)
# python main
if __name__=='__main__':
    app.run(debug=True)