from sklearn import datasets, model_selection, tree, linear_model
from sklearn.impute import SimpleImputer

iris_dataset = datasets.load_iris()

def predictByDecisionTree(training_set, label):
    classier = tree.DecisionTreeClassifier()

    imputer = SimpleImputer(strategy="mean")

    imputed_data = imputer.fit_transform(training_set["data"])
    imputed_label = imputer.transform(label)

    classier.fit(imputed_data, training_set["target"])
    predicated = classier.predict(imputed_label)
    return predicated

def predictByLogisticRegression(training_set, label):
    regression = linear_model.LogisticRegression()

    imputer = SimpleImputer(strategy="mean")

    imputed_data = imputer.fit_transform(training_set["data"])
    imputed_label = imputer.transform(label)

    regression.fit(imputed_data, training_set["target"])
    return regression.predict_proba(imputed_label)