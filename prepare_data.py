import random


with open(r"dataset/metadata.csv", "r") as t:
    texts = t.read()

test_p = 0.1
val_p = 0.05

max_c = 200

dataset_path = r"dataset/"

data = []

for j in [i.split(",") for i in texts.split("\n") if len(i.split(",")) == 2]:
    with open(dataset_path + j[1], "r") as t:
        text = t.read()
        text = text.replace("\n", "")
        data.append((dataset_path + j[0], text))

with open(r"dataset/transcript.txt", "r", encoding="utf-8") as t:
    texts = t.read()

data += [("dataset/" + i.split("|")[0], i.split("|")[1]) for i in texts.split("\n") if len(i.split("|")[:2]) == 2]

random.shuffle(data)

test_c = int(min(len(data) * test_p, max_c))
val_c = int(min(len(data) * val_p, max_c))

test = data[:test_c]
val = data[test_c: test_c + val_c]
train = data[test_c + val_c:]

for data, path in zip([test, val, train], ["test", "val", "train"]):
    with open(dataset_path + path + ".txt", "w") as t:
        t.write("\n".join(["|".join(i) for i in data]))
