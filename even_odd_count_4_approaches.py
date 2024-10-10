import time

# Approach 1: Using modulus (%)
def even_odd_approach1(ls):
    even_count = 0
    odd_count = 0
    for i in ls:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Approach 2: Using bitwise AND (&)
def even_odd_approach2(ls):
    even_count = 0
    odd_count = 0
    for i in ls:
        if i & 1 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Approach 3: Using sum() and bitwise AND (&)
def even_odd_approach3(ls):
    even_count = 0
    odd_count = 0
    even_count += sum(1 for i in ls if i & 1 == 0)
    odd_count += len(ls) - even_count
    return even_count, odd_count

# Approach 4: Using sum() and modulus (%)
def even_odd_approach4(ls):
    even_count = 0
    odd_count = 0
    even_count += sum(1 for i in ls if i % 2 == 0)
    odd_count += len(ls) - even_count
    return even_count, odd_count

# Performance checker function
def check_performance(approaches, names, ls):
    time_taken = []
    
    # Measure time for each approach
    for approach in approaches:
        temp_time = []
        for _ in range(10):  
            start_time = time.time()
            approach(ls)
            end_time = time.time()
            temp_time.append(end_time - start_time)
        
        # Get average time for the approach
        avg_time = sum(temp_time) / len(temp_time)
        time_taken.append(avg_time)

    # Compare each approach to the first one
    base_time = time_taken[0]  # Time taken by the first approach
    comparisons = []
    
    for i, t in enumerate(time_taken):
        if i == 0:
            comparisons.append((names[i], t, "Baseline"))
        else:
            percentage_diff = ((base_time - t) / base_time) * 100
            comparisons.append((names[i], t, f"{percentage_diff:.2f}% faster than {names[0]}"))
    
    return comparisons

# Running the performance comparison on the list
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
approach_names = [
    "Approach 1 (using %)", 
    "Approach 2 (using &)", 
    "Approach 3 (sum + &)", 
    "Approach 4 (sum + %)"
]

# Check performance
results = check_performance(
    [even_odd_approach1, even_odd_approach2, even_odd_approach3, even_odd_approach4], 
    approach_names, 
    ls
)

# Print the results
for approach_name, time_taken, comparison in results:
    print(f"Approach: {approach_name}, Time: {time_taken:.6f} seconds, Comparison: {comparison}")
