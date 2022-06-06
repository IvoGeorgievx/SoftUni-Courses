words = input().split(" ")
palindrome = input()
palindromes = []

for p in words:
    if p == ''.join(reversed(p)):
        palindromes.append(p)
print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(palindrome)} times")