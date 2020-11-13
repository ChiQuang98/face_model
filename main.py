from flask import Flask, request, render_template, jsonify
import json
from model import load_model,load_Labels,face_detector_by_image,load_Pretrain_model,load_model_face_detector
from sklearn.preprocessing import LabelEncoder
import numpy as np
import json
from flask import Flask, request, render_template
model_fd = load_model_face_detector()
classify_model = load_model()
pretrain_model = load_Pretrain_model()
labels = load_Labels()
le =  LabelEncoder()
app = Flask(__name__)
@app.route('/attendance', methods=['POST'])
def uploadFile():
    global person_rep
    # person_rep  = load_person_rep(pathPerson_Rep)
    file = request.files.get('file')
    if file and file.filename != '':
        file.save("DataClient/"+file.filename)
        listJSON = face_detector_by_image("DataClient/"+file.filename,model_fd,classify_model,pretrain_model,labels)
        print(type(listJSON))
    # print((jsonify(listJSON)))
    # return pd.Series(listJSON).to_json(orient='values')
    return json.dumps(np.array(listJSON).tolist())

@app.route('/')
def homePage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
