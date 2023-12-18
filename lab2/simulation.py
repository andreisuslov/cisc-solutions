import sys
import random

def experiment(n):
    if n <= 1:
        return False, 0.0

    heard_rumor = [False] * n
    rumor_spreader = 0  # Bob starts the rumor
    heard_rumor[rumor_spreader] = True
    spread_count = 1

    while spread_count < n:
        potential_targets = [i for i in range(n) if not heard_rumor[i]]
        if not potential_targets:
            break  # No more guests to tell

        next_guest = random.choice(potential_targets)
        heard_rumor[next_guest] = True
        spread_count += 1

        if next_guest == rumor_spreader or (spread_count > 2 and random.random() < 0.5):
            break  # Rumor stops spreading

        rumor_spreader = next_guest

    fully_propagated = spread_count == n
    percentage_heard = (spread_count / n) * 100

    return fully_propagated, percentage_heard

def monte_carlo_simulation(n, m):
    full_propagations = 0
    total_percentage_heard = 0.0

    for _ in range(m):
        fully_propagated, percentage_heard = experiment(n)
        if fully_propagated:
            full_propagations += 1
        total_percentage_heard += percentage_heard

    average_percentage_heard = total_percentage_heard / m
    percentage_full_propagation = (full_propagations / m) * 100

    return percentage_full_propagation, average_percentage_heard

if __name__ == "__main__":
    if len(sys.argv) != 3 or not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        print("Usage: python simulation.py <number_of_guests> <number_of_runs>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])
    percentage_full_propagation, average_percentage_heard = monte_carlo_simulation(n, m)

    print(f"Percentage of runs where the rumor fully propagated: {percentage_full_propagation}%")
    print(f"Average percentage of guests who heard the rumor: {average_percentage_heard}%")