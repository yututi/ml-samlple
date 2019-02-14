from sklearn.datasets import make_blobs

x, y = make_blobs(n_samples=100, n_features=4)

dataset = {
    "feature_names":["装置A(V)", "装置B(V)", "装置C(A)", "装置D(V)"],
    "data":x,
    "target":y,
    "target_names":["装置A", "装置B", "装置C", "装置D"]
}
