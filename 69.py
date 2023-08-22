scores = {
    "riazi1": 14,
    "mabani computer": 20,
    "sakhteman dade": 18,
    "vasaya emam": 7,
    "zaban omomi": 19,
    "andishe eslami": 16
}


def status(course):
    if scores[course] >= 10:
        print(course, ": Passed")
    else:
        print(course, ": Failed")


def average(scores):
    avg = sum(scores.values()) / len(scores)
    print("Average :", avg)


# --------------------------------------------------


for i in scores:
    status(i)

average(scores)
