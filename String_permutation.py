#code to find all permutations of a string in python

def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        ch = s[i]  # Pick the current character
        left_substr = s[:i]  # Characters before the current character
        right_substr = s[i + 1:]  # Characters after the current character
        rest = left_substr + right_substr  # Exclude the picked character
        permute(rest, answer + ch)  # Recursive call

# Get input from the user
string = input("Enter a string: ")
print(f"Permutations of '{string}':")
permute(string)
