from sample import predictByLogisticRegression, iris_dataset, predictByDecisionTree
from sklearn import model_selection, metrics

data_train, data_test, label_train, label_test = model_selection.train_test_split(iris_dataset["data"], iris_dataset["target"])
dataset = {
    "data":data_train,
    "target":label_train
}

print(predictByDecisionTree(dataset, data_test))

result = predictByLogisticRegression(dataset, data_test)
print(result)

