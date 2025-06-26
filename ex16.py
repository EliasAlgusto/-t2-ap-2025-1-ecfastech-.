
fibonacci = [0, 1]
while (prox := fibonacci[-1] + fibonacci[-2]) <= 500:
    fibonacci.append(prox)

print("Fibonacci até 500:", fibonacci)