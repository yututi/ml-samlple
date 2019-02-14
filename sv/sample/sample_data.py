from sklearn.datasets import make_classification

x, y = make_classification(n_samples=100, n_features=4, n_informative=2, n_classes=4, n_clusters_per_class=1, scale=2, shift=2, class_sep=1.5)

dataset = {
    "feature_names":["装置A(V)", "装置B(V)", "装置C(A)", "装置D(V)"],
    "data":x,
    "target":y,
    "target_names":["装置A", "装置B", "装置C", "装置D"]
}
