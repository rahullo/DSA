n = len(edges)
    if n == 1:
        return 1
    
    score = [0] * 20

    for a, b in edges:
        score[a] += 1
        score[b] += 1

    if max(score) > 1:
        return max(score) - 1
    print("Score: ", score)
    return -1