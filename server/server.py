from flask import Flask,request,jsonify
import util

app=Flask(__name__)

@app.route('/classify',methods=['GET','POST'])
def classify_image():
    img_data=request.form['img_data']
    response=jsonify(util.classify_image(img_data))
    response.headers.add('Access-control-allow-origin','*')
    return response

if __name__ == "__main__":
    print("Starting python Server\n")
    util.load_saved_artifacts()
    app.run(port=5000)