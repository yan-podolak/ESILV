from flask import Flask, render_template, request
import joblib
from joblib import dump, load
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/resultat',methods = ['GET'])
def resultat():
    result=request.args
    n = result['nom']
    p = result['prenom']

    a = result['a']
    ad = result['ad']
    i = result['i']
    iD = result['iD']
    pr = result['pr']
    prd = result['prd']
    br = result['br']
    er = result['er']
    pv = result['pv']
    sd = result['sd']
    m = result['m']
    os = result['os']
    b = result['b']
    r = result['r']
    tt = result['tt']
    vt = result['vt']
    w = result['w']

    model = joblib.load('MyModel.pkl')
    model_columns = joblib.load('model_columns.pkl')

    data = [a,ad,i,iD,pr,prd,br,er,pv,sd,m,os,b,r,tt,vt,w]
    df2 = pd.DataFrame(data, index =model_columns).transpose()

    df2.to_csv("test.csv")

    new = pd.read_csv('test.csv')
    new = new.drop(columns="Unnamed: 0")
    if 'Jan' or 'Apr'  in new.Month[0]:
        new.drop(columns="Month")
    new = pd.get_dummies(new)
    month = ['Month_Aug', 'Month_Dec', 'Month_Feb', 'Month_Jul', 'Month_June', 'Month_Mar', 'Month_May', 'Month_Nov', 'Month_Oct', 'Month_Sep','VisitorType_New_Visitor', 'VisitorType_Other',
       'VisitorType_Returning_Visitor']
    for i in month:
        if i not in new.columns:
            new[i] = 0
    
    predicted = model.predict(new)
    print(type(predicted))
    if predicted[0] == 1:
        a="spend your money"
    else:
        a= "keep your money"
    return render_template("resultat.html", nom=n, prenom=p,achat=a)

app.run(debug=True)