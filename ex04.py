
pop_a = 80000
pop_b = 200000
anos = 0

while pop_a <= pop_b:
    pop_a += pop_a * 0.03
    pop_b += pop_b * 0.015
    anos += 1

print(f"País A ultrapassará ou igualará o país B em {anos} anos.")
