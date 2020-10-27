# Implementation by Utkarsh Singh
""" Given a 2D list
scores = [
    ['Jerry', '65'],
    ['Bob', '91'],
    ['Jerry', '23'],
    ['Eric', '83']
]

find the student with the best average and return both the name and the best average.
"""

scores = [
    ['Jerry', '65'],
    ['Bob', '2'],
    ['Jerry', '23'],
    ['Eric', '3']
]

def findBestAverage(scores):
    names_list = [item[0] for item in scores]
    scores_list = [int(item[1]) for item in scores]

    names ={}
    average ={}

    for name, score in zip(names_list, scores_list):
        if name in names:
            average[name] += score
            names[name] += 1
        else:
            average[name] = score
            names[name] = 1

    for name in names:
        average[name] = average[name]/float(names[name])

    student = [k for k, v in average.items() if v == max(average.values())]

    return(str(max(average.values())) + " by " + str(student[0]))


print(findBestAverage(scores))