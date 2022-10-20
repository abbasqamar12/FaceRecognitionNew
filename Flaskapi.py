from flask import Flask , jsonify , request
import face_analysis_app

app= Flask(__name__)

@app.route('/' , methods= ['GET' , 'POST'])
def index():
    if (request.method == 'GET'):
        data= face_analysis_app.run()
        print('face_analysis_app.run')
        return jsonify({'Age Range':data})
    elif (request.method == 'POST'):
        data = face_analysis_app.run()
        print('face_analysis_app.run')
        return jsonify({'Age Range':data})



if __name__ == "__main__":
    app.run( port=3000, debug=True)