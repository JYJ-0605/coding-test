c = int(input())

for _ in range(c):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    count = 0
    for x in scores[1:]:
        if x > avg:
            count += 1
    print(f"{count / scores[0] * 100:.3f}%")