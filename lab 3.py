from collections import deque

def is_goal(state, target):
    return target in state

def get_successors(state, a, b):
    x, y = state
    return [
        (a, y),                           # Fill Jug A
        (x, b),                           # Fill Jug B
        (0, y),                           # Empty Jug A
        (x, 0),                           # Empty Jug B
        (x - min(x, b - y), y + min(x, b - y)),  # Pour A -> B
        (x + min(y, a - x), y - min(y, a - x))   # Pour B -> A
    ]

def bfs(a, b, target):
    visited = set()
    queue = deque()
    queue.append(((0, 0), []))  # ((jugA, jugB), path)

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if target in (x, y):
            return path + [(x, y)]

        for next_state in get_successors((x, y), a, b):
            if next_state not in visited:
                queue.append((next_state, path + [(x, y)]))
    return None

# --------- User Input ----------
try:
    a = int(input("Enter capacity of Jug A: "))
    b = int(input("Enter capacity of Jug B: "))
    target = int(input("Enter target amount: "))

    if target > max(a, b):
        print("❌ Target can't be more than both jug capacities.")
    else:
        result = bfs(a, b, target)
        if result:
            print("\n✅ Steps to reach the target:")
            for step in result:
                print(f"Jug A: {step[0]}  |  Jug B: {step[1]}")
        else:
            print("❌ No solution found.")
except ValueError:
    print("Please enter valid integers.")
