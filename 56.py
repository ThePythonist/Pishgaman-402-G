ages = {
    "nima": 23,
    "sara": 30,
    "behnam": 40,
    "behrooz": 13,
    "maryam": 18,
}

oldest = max(ages.values())

for i in ages :
    if ages[i] == oldest:
        print(i)
