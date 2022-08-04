import re

info = input()
pattern = r'([=/])([A-Z][a-zA-Z]{2,})\1'

result = re.finditer(pattern, info)

destinations = []
total_points = 0
for res in result:
    destinations.append(res.group(2))
    total_points += len(res.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_points}")
