# Day 1, Problem 1

data = open('input.txt', 'r').read().split('\n')

left_list = []
right_list = []
distance_list = []

for line in data:
    if line.strip():
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

sorted_left_list = sorted(left_list)
sorted_right_list = sorted(right_list)

distance_list = [abs(l - r) for l, r in zip(sorted_left_list, sorted_right_list)]

sum_distance = sum(distance_list)

print('Sum Distance', sum_distance)

# Day 1, Problem 2

similarity_list = []

for i in range(len(left_list)):
    if left_list[i] in right_list:
        count = right_list.count(left_list[i])
        similarity_list.append(left_list[i] * count)

sum_similarity = sum(similarity_list)

print('Sum Similarity', sum_similarity)
        