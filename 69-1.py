scores = {
    "riazi1": (14, 3),
    "mabani computer": (20, 3),
    "sakhteman dade": (18, 3),
    "vasaya emam": (18, 1),
    "zaban omomi": (19, 2),
    "andishe eslami": (19, 2)
}

nomarat = [i[0] * i[1] for i in scores.values()]
vahedha = [i[1] for i in scores.values()]
avg = sum(nomarat) / sum(vahedha)
print(avg)
