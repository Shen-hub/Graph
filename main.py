def get_data():

    matrix = {}
    count = int(input())
    for i in range(count):
        inp_str = input()
        if inp_str == '':
            break
        first_point, second_point = inp_str.split(' ')
        first_point, second_point = int(first_point), int(second_point)
        if not matrix.get(first_point):
            matrix[first_point] = [second_point]
        else:
            matrix[first_point].append(second_point)
        if not matrix.get(second_point):
            matrix[second_point] = [first_point]
        else:
            matrix[second_point].append(first_point)
    return matrix, count


def dfs(first_point):
    visited[first_point] = True
    if matrix.get(first_point) == None:
        return
    for point in matrix.get(first_point):
        if not visited[point]:
            dfs(point)


def calculate_result():
    count_components = 0
    for key, value in visited.items():
        if not value:
            dfs(key)
            count_components += 1
    return count_components


matrix, count_points = get_data()
keys = list(matrix.keys())
visited = {}
for key in range(1, count_points+1):
    visited[key] = False
start_point = keys[0]

result = calculate_result()
print(result-1)
