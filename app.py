from config import app,predict_pipe,PORT_NUMBER,HOST_NAME
from flask import render_template,request


# Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'
@app.route('/',methods = ["GET"])
def base_page():
    return render_template('base_page.html')

@app.route('/predict/',methods = ["POST"])
def predict_page():
    if request.method == 'POST':
        form_data = request.form
        # print(form_data)
        # 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'
        Pclass = int(form_data.get('pclass'))
        Sex = form_data.get('gender')
        Age = int(form_data.get('age'))
        SibSp = int(form_data.get('sibsp'))
        Parch = int(form_data.get('parch'))
        Fare = float(form_data.get('fare'))
        Embarked = form_data.get('parch')
        result = predict_pipe.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
        if result[0] == 1:
            return "Survived !!"
        else:
            return "NOT Survived.."
    

if __name__ == '__main__':
    app.run(debug=False,host=HOST_NAME,port=PORT_NUMBER)