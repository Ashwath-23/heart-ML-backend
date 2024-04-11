from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from flask import Flask, render_template, request, redirect, session
import os 
import F_model

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class Test(Resource):
    def get(self):
        return "Welcome to Tessst APssssI"

    def post(self):
        try:
            value = request.get_json()
            if(value):
                ans = F_model.get_values(value)
                #print(value)
                return ans

            else:
                return {"error":"Invalid format."}

        except Exception as error:
            return {'error': error}

api.add_resource(Test,'/api')

@app.route('/')
def view_form():
    return render_template('login.html')

if __name__ == "__main__":

    app.run(debug=True)
