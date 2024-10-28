competitors_scores = [
    (17, 15, 16, 17, 15),
    (16, 18, 19, 17, 19),
    (19, 15, 15, 19, 18),
    (18, 17, 19, 15, 16)
]

def calculate_total_score(scores):
    scores = sorted(scores)
    total_score = sum(scores[1:4])
    return total_score

total_points = list(map(calculate_total_score, competitors_scores))
print("Total points obtained by each competitor:", total_points)

