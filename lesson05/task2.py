# Урок 5. Задание 2 — гласные и согласные в слове
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson05

word = input("Слово из маленьких латинских букв: ")
vowels = "aeiou"

vowel_count = 0
consonant_count = 0
for ch in word:
    if ch in vowels:
        vowel_count += 1
    elif "a" <= ch <= "z":
        consonant_count += 1

print("Гласных:", vowel_count)
print("Согласных:", consonant_count)

for v in vowels:
    count = word.count(v)
    print(f"{v}: {count if count > 0 else False}")
