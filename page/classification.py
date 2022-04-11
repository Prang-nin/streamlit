import streamlit as st
from sklearn import datasets
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def app():
    st.title("Classification Problems")

    st.write("""Let's experiment on different model 🏄‍♂️ """)  

    dataName = st.sidebar.selectbox("select Data", ("Iris", "wine"))
    selectedAlgo = st.sidebar.selectbox("select Algorithm", ("K-NN", "SVM", "Random Forest"))

    # load dataset
    def loadData(dataName):
        if dataName == 'Iris':
            data = datasets.load_iris()
            x = data.data
            y = data.target

        elif dataName == 'wine':
            data = datasets.load_wine()
            x = data.data
            y = data.target
        return x,y

    class algo():
        def __init__(self, algo = 'K-NN'):
            self.algo = algo

        def getParameter(self):
            params = {}
            if self.algo == 'K-NN':
                params['K'] = st.sidebar.slider('K', 1, 15)
                params['weights'] = st.sidebar.selectbox('select weights',('uniform', 'distance'))
            elif self.algo == 'SVM':
                params['C'] = st.sidebar.slider('C', 0.01, 10.0)
                params['gamma'] = st.sidebar.selectbox('select gamma',('scale', 'auto'))
                params['kernel'] = st.sidebar.selectbox('select kernel',('linear', 'poly', 'rbf', 'sigmoid'))
                params['degree']= st.sidebar.slider('Deg', 1, 5)
            elif self.algo == 'Random Forest':
                params['max_depth'] = st.sidebar.slider('Max_depth', 2, 20)
                params['max_features'] = st.sidebar.selectbox('select max_feature',('auto', 'sqrt', 'log2'))
                params['min_samples_leaf'] = st.sidebar.slider('min_sample_leaf', 2, 50)
                params['min_samples_split'] = st.sidebar.slider('min_sample_split', 2, 50)
                params['n_estimators'] = st.sidebar.slider('n_estimators', 1, 100)
            return params
        def getClassifier(self):
            params = algo.getParameter(self)
            if self.algo == 'K-NN':
                clf = KNeighborsClassifier(n_neighbors= params['K'] )#weights = params['weights'])
            elif self.algo == 'SVM':
                clf = SVC(C = params['C'], gamma = params['gamma'], kernel =params['kernel'], degree = params['degree'])
            elif self.algo == 'Random Forest':
                clf = RandomForestClassifier( max_depth= params['max_depth'] ,max_features=params['max_features'], 
                min_samples_leaf=params['min_samples_leaf'], min_samples_split=params['min_samples_split'], n_estimators=params['n_estimators'], random_state=42)
            return clf

    # get data
    x,y = loadData(dataName)
    # make classification
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2 )     
    classifier = algo(algo = selectedAlgo)
    clf = classifier.getClassifier()
    clf.fit(xTrain, yTrain)
    yPred = clf.predict(xTest)
    acc = accuracy_score(yTest, yPred)
    confusion = confusion_matrix(yTest, yPred)
    report = classification_report(yTest, yPred)

    st.header('**Your selected Data**')
    st.write('Dataset : {}'.format(dataName))
    st.write('Number of instance : {}'.format(y.shape[0]))
    st.write('Number of Features : {}'.format(x.shape[1]))

    st.header('**The Classification Result**')
    st.write("Accuracy of selected algorithm is {:.2f}".format(acc))
    st.write('Confusion matrix')
    st.write(confusion)


