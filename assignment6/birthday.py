import random
import sys

def run_experiment():
    birthdays = set()
    count = 0
    while True:
        bday = random.randint(0, 364)
        count += 1
        if bday in birthdays:
            return count
        birthdays.add(bday)

def estimate_avg_people(num_trials):
    total = 0
    for _ in range(num_trials):
        total += run_experiment()
    return total / num_trials

num_trials = int(sys.argv[1])
avg_people = estimate_avg_people(num_trials)
print(f"{avg_people:.2f}")