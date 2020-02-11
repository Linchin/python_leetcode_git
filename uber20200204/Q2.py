def sharedInterests(friends_nodes, friends_edges, friends_from, friends_to, friends_weight):

    pairs = {}
    for i in range(1, friends_nodes+1):
        for j in range(i+1, friends_nodes+1):
            pairs[(i, j)] = {}

    for from_, to_, weight in zip(friends_from, friends_to, friends_weight):
        small = min(from_, to_)
        big = max(from_, to_)
        pairs[(small, big)][weight] = True

    product_ = []
    weight_ = []

    for key in pairs:
        product_.append(key[0]*key[1])
        weight_.append(len(pairs[key]))

    max_weight = max(weight_)
    max_index = [i for i, j in enumerate(weight_) if j == max_weight]
    max_prod = [product_[i] for i in max_index]
    return max(max_prod)




friends_nodes = 4
friends_edges = 5
friends_from = [1, 1, 2, 2, 2]
friends_to = [2, 2, 3, 3, 4]
friends_weight = [1, 2, 1, 3, 3]
print(sharedInterests(friends_nodes, friends_edges, friends_from, friends_to, friends_weight))




