actor_name = input()
initial_points = float(input())
judges = int(input())
points_needed = 1250.5

for n in range(judges):
    judge_name = input()
    points = float(input())

    initial_points += len(judge_name) * points / 2

    if initial_points > points_needed:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {initial_points:.1f}!')
        break

if initial_points <= points_needed:
    print(f'Sorry, {actor_name} you need {points_needed - initial_points:.1f} more!')
