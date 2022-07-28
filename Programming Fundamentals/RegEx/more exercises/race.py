import re

participants = input().split(", ")
pdict = {}

for p in participants:
    if p not in pdict:
        pdict[p] = 0

command = input()

while command != 'end of race':
    participant = "".join(re.findall("[a-zA-Z]+", command))
    participant_points = "".join(re.findall("[0-9]+", command))
    participant_points = list(map(int, participant_points))
    if participant in pdict:
        pdict[participant] += int(sum(participant_points))

    command = input()

pdict = dict(sorted(pdict.items(), key=lambda x: x[1], reverse=True))
keys = list(pdict.keys())
print(f'1st place: {keys[0]}')
print(f'2nd place: {keys[1]}')
print(f'3rd place: {keys[2]}')





