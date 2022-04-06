volume = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

# Use the division operator ( / ) to get the the quotient from two numbers.
# Multiply this quotient by 100 using the multiplication operator ( * ) to get the percentage.
pipe_one_total = p1 * hours
pipe_two_total = p2 * hours
pipe_total = pipe_two_total + pipe_one_total
pipe_one_percentage = pipe_one_total / pipe_total * 100
pipe_two_percentage = pipe_two_total / pipe_total * 100

if pipe_total <= volume:
    pipe_total = pipe_total / volume * 100
    print(f'The pool is {pipe_total:.2f}% full. '
          f'Pipe 1: {pipe_one_percentage:.2f}%. '
          f'Pipe 2: {pipe_two_percentage:.2f}%."')
elif pipe_total >= volume:
    pipe_total = pipe_total - volume
    print(f'For {hours:.2f} hours the pool overflows with {pipe_total:.2f} liters.')



