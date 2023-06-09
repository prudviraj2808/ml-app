from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('home.html') 

@app.route('/predictdata',methods=['POST'])
def predict_datapoint():
    if request.method=='POST':
        data=CustomData(
            gender=request.form['gender'],
            race_ethnicity=request.form['ethnicity'],
            parental_level_of_education=request.form['parental_level_of_education'],
            lunch=request.form['lunch'],
            test_preparation_course=request.form['test_preparation_course'],
            reading_score=float(request.form['reading_score']),
            writing_score=float(request.form['writing_score'])

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        print('After Prediction')
        prdicted_results=results[0]
        return render_template('home.html', results='The predicted score is : {}'.format(prdicted_results))
        # return render_template('home.html',results=prdicted_results) # rendering the predicted result

        
if __name__=="__main__":
    app.run(host='0.0.0.0')        


