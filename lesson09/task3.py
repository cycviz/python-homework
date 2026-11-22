# Урок 9. Задание 3 — встречалось ли число раньше

seen = set()
for x in input().split():
    n = int(x)
    print("YES" if n in seen else "NO")
    seen.add(n)
