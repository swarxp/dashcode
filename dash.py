# Get the number of processes
n = int(input("Enter the number of processes: "))
# Lists to store bids for S1 and S2
b1_list = []
b2_list = []
# Collect bids from the user
for i in range(n):
    print(f"Enter bids for process {i+1}:")
    b1 = float(input("Bid for S1 (request R1 then R2): "))
    b2 = float(input("Bid for S2 (request R2 then R1): "))
    b1_list.append(b1)
    b2_list.append(b2)
# Calculate total bids
total_b1 = sum(b1_list)
total_b2 = sum(b2_list)

# Determine the chosen strategy based on total bids
if total_b1 > total_b2:
    chosen_strategy = "S1 then S2"
    total_utility = total_b1
elif total_b2 > total_b1:
    chosen_strategy = "S2 then S1"
    total_utility = total_b2
else:
    chosen_strategy = "S1 then S2" # Arbitrary choice if equal
    total_utility = total_b1

# Determine each process's preferred strategy
preferred_list = []
for i in range(n):
    if b1_list[i] > b2_list[i]:
        preferred_list.append("S1 then S2")
    elif b2_list[i] > b1_list[i]:
        preferred_list.append("S2 then S1")
    else:
        preferred_list.append("indifferent")

# Calculate utility without coordination
if (all(p == "S1 then S2" for p in preferred_list) or
    all(p == "S2 then S1" for p in preferred_list) or
    all(p == "indifferent" for p in preferred_list)):
    if "S1 then S2" in preferred_list:
        independent_utility = total_b1
    elif "S2 then S1" in preferred_list:
        independent_utility = total_b2
    else:
        independent_utility = total_b1 # All indifferent, choose S1
else:
    independent_utility = 0 # Mixed preferences lead to deadlock

# Output results
print(f"\nChosen strategy: {chosen_strategy}")
print(f"Total utility with coordination: {total_utility}")
print(f"Total utility without coordination: {independent_utility}")
