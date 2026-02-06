def findJudge(n: int, trust: list[list[int]]) -> int:
    # Edge case: If there is only 1 person, they are the judge by default 
    # (since there is no one else to trust them)
    if n == 1:
        return 1

    # Create a list of 0s to store the score for each person.
    # We use n + 1 size so we can use indices 1 to n directly.
    trust_scores = [0] * (n + 1)
    # Loop through the trust array
    # 'a' trusts 'b'
    for a, b in trust:
        print("a: ", a, ", b: ", b)
        trust_scores[a] -= 1  # Person 'a' trusts someone (lose point)
        trust_scores[b] += 1  # Person 'b' is trusted (gain point)
    print("Trust Score: ", trust_scores)
        

    # Check for the person with score n - 1
    for i in range(1, n + 1):
        if trust_scores[i] == n - 1:
            return i

    return -1

print(findJudge(n = 2, trust = [[1,2]]))
print(findJudge(n = 3, trust = [[1,3],[2,3]]))
print(findJudge(n = 3, trust = [[1,3],[2,3],[3,1]]))