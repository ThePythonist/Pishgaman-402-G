scores = {
    "riazi1": 14,
    "mabani computer": 20,
    "sakhteman dade": 18,
    "vasaya emam": 7,
    "zaban omomi": 19,
    "andishe eslami": 16
}

for k, v in scores.items():
    if v >= 10:
        print(k, ": Passed")
    else:
        print(k, ": Failed")

avg = sum(scores.values()) / len(scores)
print("Average :", avg)
