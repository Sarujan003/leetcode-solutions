n = 3
logs = [[1,3],[2,6],[1,5]]
x = 5
queries = [10,11]

# time_interval = [(q-x, q) for q in queries]

# output = []

# for t in time_interval:
#     a, b = t

#     server_dict = {i:False for i in range(1,n+1)}
#     for server_id, time in logs:

#         if time >= a and time <= b and not server_dict[server_id]:
#             server_dict[server_id] = True

#     count = 0
#     for key in server_dict:
#         if not server_dict[key]:
#             count += 1

#     output.append(count)
# print(output)

queries.sort()
logs.sort(key=lambda x: x[1])

print(logs)