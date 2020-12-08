# Day 6
# Part 2
with open('6/input6', 'r') as f:
    groups = f.read().split('\n\n')

results = []
for group in groups:
    persons = group.split('\n')
    answers = {}
    for person in persons:
        for c in person:
            if not c in answers:
                answers[c] = 1
            else:
                answers[c] += 1
    result = 0
    for answer in answers:
        if answers[answer] == len(persons):
            result += 1

    results.append(result)

print(sum(results))
