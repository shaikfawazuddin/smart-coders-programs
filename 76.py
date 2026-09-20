def count_vowels(s, index=0):
    if index == len(s):
        return 0
    return (1 if s[index].lower() in 'aeiou' else 0) + count_vowels(s, index + 1)

print(count_vowels(input()))
