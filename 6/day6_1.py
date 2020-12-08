# Day 6
# Part 1
with open('6/input6', 'r') as f:
    groups = f.read().split('\n\n')

results = []
for group in groups:
    persons = group.split('\n')
    answers = []
    for person in persons:
        for c in person:
            if not c in answers:
                answers.append(c)
    results.append(len(answers))

print(sum(results))
