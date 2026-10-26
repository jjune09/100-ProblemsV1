import pickle

data = {"name": "Alice", "age": 25}
with open("data.bin", "wb") as f:
    pickle.dump(data, f)