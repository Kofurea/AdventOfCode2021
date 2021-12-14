import time

def day12():
    start = time.time()

    with open('Day12_input.txt') as file:
        input_file = [line.strip().split('-') for line in file]

    testing = [True, 2]
    if testing[0]:
        if testing[1] == 0:
            input_file = [['start','A'], ['start','b'], ['A','c'], ['A','b'], ['b','d'], ['A','end'], ['b','end']]
        if testing[1] == 1:
            input_file = [['dc', 'end'], ['HN', 'start'], ['start', 'kj'], ['dc', 'start'], ['dc', 'HN'], ['LN', 'dc'], ['HN', 'end'], ['kj', 'sa'], ['kj', 'HN'], ['kj', 'dc']]

    nodelist = list(set([item for sublist in input_file for item in sublist]))

    # Make a graph
    graph = {}
    for node in nodelist:
        connections = []
        for edge in input_file:
            if node == edge[0]:
                connections.append(edge[1])
            if node == edge[1]:
                connections.append(edge[0])
        graph[node] = connections

    any_paths_left = True
    for part in ["part1", "part2"]:
        all_paths = [['start']]
        any_paths_left = True
        while any_paths_left:
            # If the statment doesnt change in the loop, we are done
            any_paths_left = False
            # List of new paths
            new_paths = []
            # For step we took for our paths
            for path_index, path in enumerate(all_paths):
                # If the path is already completed, just add it to the new_paths
                if path[-1] == 'end':
                    new_paths.append(path)
                # Otherwise, look at the neighbors it can still visit, and add a path for all of them
                else:
                    any_paths_left = True
                    # For all neighbors of the most recent node
                    for neighbor in graph[path[-1]]:
                        # For all viable routes that havn't been added yet
                        if part == "part1":
                            if neighbor not in path or neighbor.isupper():
                                new_paths.append(path + [neighbor])
                        if part == "part2":
                            lower_case_list = [item for item in path if item.islower()]
                            frequency = 0
                            for item in set(lower_case_list):
                                if lower_case_list.count(item) > frequency:
                                    frequency = lower_case_list.count(item)
                            if frequency >= 2:
                                if neighbor not in path or neighbor.isupper():
                                    new_paths.append(path + [neighbor])
                            else:
                                if neighbor != 'start':
                                    new_paths.append(path + [neighbor])
                        # If we are stuck (aka no valid paths), we simply don't add it to new_paths,
                        # and our problem should disappear
            # And change the next loop to loop over our new_paths
            all_paths = new_paths
        if part == "part1":
            print("The answer to part 1 is:", len(all_paths))
        if part == "part2":
            print("The answer to part 2 is:", len(all_paths))

    end = time.time()

    print("The elapsed time is:", end-start)