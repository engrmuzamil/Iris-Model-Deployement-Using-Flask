from flask import  Flask, render_template, request
app = Flask(__name__,template_folder="templates")
import iris
@app.route('/')
def load():
    return render_template('index.html')

# Route 'classify' accepts GET request
@app.route('/classify',methods=['POST'])
def classify_type():
    try:
        if request.method == "POST":
            sepal_len = request.form["first"]
            sepal_wid = request.form["second"]
            petal_len = request.form["third"]
            petal_wid = request.form["fourth"]

            variety = iris.classify(sepal_len, sepal_wid, petal_len, petal_wid)

            return render_template('result.html', variety=variety)
    except:
        return 'Error'

# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)