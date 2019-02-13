from .sample import estimate, iris_dataset
from sklearn import model_selection, metrics

data_train, data_test, label_train, label_test = model_selection.train_test_split(iris_dataset["data"], iris_dataset["target"])
dataset = {
    "data":data_train,
    "target":label_train
}

result = estimate(dataset, data_test)
print(result)

ac_score = metrics.accuracy_score(label_test, result)
print(ac_score)