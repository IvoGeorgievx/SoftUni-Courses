def isPerfect(n):
    # To store sum of divisors
    sum = 1

    # Find all divisors and add them
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n / i
        i += 1

    # If sum of divisors is equal to
    # n, then n is a perfect number

    return print('We have a perfect number!') if sum == n and n != 1 else print("It's not so perfect.")


isPerfect(n=int(input()))