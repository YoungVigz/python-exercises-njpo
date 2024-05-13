def carousel_scheduling(queues):
    result = []

    max_len = max(len(q) for q in queues)

    for i in range(max_len):
        for q in queues:
            if i < len(q):
                result.append(q[i])

    return result

queues = [
    ['A', 'B', 'C'],
    ['D', 'E'],
    ['F']
]

result = carousel_scheduling(queues)
print("Wynik:", result)