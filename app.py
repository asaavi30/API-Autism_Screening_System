from flask import Flask, jsonify
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from flask_cors import CORS
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning)

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/algo/<int:algo>/data/<string:arr>')
def predictFunction(arr, algo):
    arr = [int(i) for i in arr.split(',')]
    le = LabelEncoder()
    df = pd.read_csv("dataset.csv")
    df.drop(['Case_No', 'Who_completed_the_test', 'Qchat-10-Score'], axis=1, inplace=True)
    data = pd.DataFrame(df, columns=['Ethnicity', 'Family_mem_with_ASD', 'ClassASD_Traits', 'Sex', 'Jaundice'])
    data['Family_mem_with_ASD_encoded'] = le.fit_transform(data['Family_mem_with_ASD'])
    data['Ethnicity_encoded'] = le.fit_transform(data['Ethnicity'])
    data['ClassASD_Traits_encoded'] = le.fit_transform(data['ClassASD_Traits'])
    data['Sex_encoded'] = le.fit_transform(data['Sex'])
    data['Jaundice_encoded'] = le.fit_transform(data['Jaundice'])
    columns = ['Ethnicity', 'Family_mem_with_ASD', 'ClassASD_Traits', 'Sex', 'Jaundice']
    for col in columns:
        df[col] = le.fit_transform(df[col])
    x = df.drop('ClassASD_Traits', axis='columns')
    y = df['ClassASD_Traits']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=7, stratify=y)
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
    clf = clf.fit(x_train, y_train)
    log_reg = LogisticRegression()
    log_reg.fit(x_train, y_train)
    knn = KNeighborsClassifier(n_neighbors=13, p=2, metric='euclidean')
    knn.fit(x_train, y_train)
    if algo == 1:
        a = log_reg.predict([arr])
        if a == 1:
            return jsonify({'prediction': '1', 'message': 'The child has autism'})
        else:
            return jsonify({'prediction': '0', 'message': 'The child does not have autism'})
    elif algo == 2:
        a = clf.predict([arr])
        if a == 1:
            return jsonify({'prediction': '1', 'message': 'The child has autism'})
        else:
            return jsonify({'prediction': '0', 'message': 'The child does not have autism'})
    elif algo == 3:
        a = knn.predict([arr])
        if a == 1:
            return jsonify({'prediction': '1', 'message': 'The child has autism'})
        else:
            return jsonify({'prediction': '0', 'message': 'The child does not have autism'})

if __name__ == '__main__':
    app.run()