import sys
import random

def monte_hall_simulation(n):
    stay_wins = 0
    switch_wins = 0

    for _ in range(n):
        prize_door = random.randint(0, 2)
        
        contestant_choice = random.randint(0, 2)
        
        remaining_doors = [door for door in [0, 1, 2] if door != contestant_choice and door != prize_door]
        host_opens = random.choice(remaining_doors)
        
        switch_door = [door for door in [0, 1, 2] if door != contestant_choice and door != host_opens][0]
        
        if contestant_choice == prize_door:
            stay_wins += 1
        if switch_door == prize_door:
            switch_wins += 1

    return stay_wins/n, switch_wins/n

n = int(sys.argv[1])

stay_prob, switch_prob = monte_hall_simulation(n)
print(f"Stay   -- {stay_prob:.3f}")
print(f"Change -- {switch_prob:.3f}")