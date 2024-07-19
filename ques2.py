def min_players_to_remove(test_cases):
    results = []
    for _ in range(test_cases):
        N, K = map(int, input().split())
        heights = list(map(int, input().split()))
        count = sum(1 for height in heights if height > K)
        results.append(count)
    return results


T = int(input())
results = min_players_to_remove(T)


for result in results:
    print(result)