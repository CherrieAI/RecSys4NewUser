

def minkow_dist(rating1, rating2, n):
	distance = 0
	common_ratings = False
	for key in rating1:
		if key in rating2:
			distance += abs((rating1[key] - rating2[key]) ** n)
			common_ratings = True
	if common_ratings:
		return distance ** 1 / n
	else:
		return -1  # Indicates no ratings in common


def compute_nearest_neighbor(username, users):
	distances = []
	for user in users:
		if user != username:
			distance = minkow_dist(users[user], users[username], 2)
			distances.append((distance, user))
	# sort based on distance -- closest first
	distances.sort()
	return distances


def recommend(username, users):
	# first find nearest neighbor
	nearest = compute_nearest_neighbor(username, users)[0][1]

	recommendations = []
	# now find bands neighbor rated that user didn't
	neighbor_ratings = users[nearest]
	user_ratings = users[username]
	for topic in neighbor_ratings:
		if topic not in user_ratings:
			recommendations.append((topic, neighbor_ratings[topic]))
	# using the fn sorted for variety - sort is more efficient
	return sorted(recommendations, key=lambda topicTuple: topicTuple[1], reverse=True)
