# Min and Max Normalization
dataset = [10, 20, 30, 40]
min_a = min(dataset)
max_b = max(dataset)
new_min = 0
new_max = 1

normalized = []

for v in dataset:
    result = ((v - min_a) / (max_b - min_a)) * (new_max - new_min) + new_min
    normalized.append(round(result, 2)) 
print("Normalized:", normalized)
