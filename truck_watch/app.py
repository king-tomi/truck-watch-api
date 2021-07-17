from flask import request
from flask import Flask
import pickle
import numpy as np

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

model = pickle.load(open("Truck-Watch-Analytics/model.pkl","rb"))

class Predict(Resource):

    def get(self,param: int):
        return {"value": param}

    def put(self,param: int):
        predictions = model.predict(param)
        form = {"prediction": predictions}
        return form



api.add_resource(Predict, "/api/predict/v1/<param>")



# @app.route("/api/predict/v1/<param>",methods=["POST"])
# def predict(param):
#     response = dict(request.get_json())
#     predictions = model.predict([np.array(response["param"])])
#     form = {"prediction": predictions}
#     return jsonify(form)



if __name__ == "__main__":
    app.run(debug=True)