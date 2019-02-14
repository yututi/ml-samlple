from sklearn import datasets, model_selection, tree
from sklearn.impute import SimpleImputer

iris_dataset = datasets.load_iris()

def estimate(training_set, label):
    classier = tree.DecisionTreeClassifier()

    imputer = SimpleImputer(strategy="mean")

    imputed_data = imputer.fit_transform(training_set["data"])
    imputed_label = imputer.transform(label)

    classier.fit(imputed_data, training_set["target"])
    predicated = classier.predict(imputed_label)
    # print(classier.apply(imputed_label))
    # print(classier.tree_.__getstate__())
    return predicated