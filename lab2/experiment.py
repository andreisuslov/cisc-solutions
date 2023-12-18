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

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python experiment.py <number_of_guests>")
        sys.exit(1)

    n = int(sys.argv[1])
    fully_propagated, percentage_heard = experiment(n)

    propagation_status = "fully propagated" if fully_propagated else "did not fully propagate"
    print(f"The rumor {propagation_status}.")
    print(f"Percentage of party guests who heard the rumor: {percentage_heard}%")
