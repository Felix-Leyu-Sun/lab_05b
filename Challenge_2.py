def get_scores():
    names = []
    scores = []
    n = int(input("How many students?"))
    for i in range(n):
        name = input("Name: ")
        score = int(input("Score(0,100): "))
        names.append(name)
        scores.append(score)
    return names , scores

def class_average(scores):
    return sum(scores)/len(scores)

def highest_scorer(names, scores):
    best = max(scores)
    index = scores.index(best)
    return names[index]

def print_report(names, scores):
    print("Name".ljust(12) + "Score")
    print("-" * 20)
    for i in range(len(names)):
        print(names[i].ljust(12) + str(scores[i]))
    print("-" * 20)
    print(f"Class average: {class_average(scores):.1f}")
    print(f"Top student: {highest_scorer(names, scores)}")

names, scores = get_scores()
print_report(names, scores)



