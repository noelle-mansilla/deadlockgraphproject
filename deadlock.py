def store_file(file_name):
    """
        This is a function to retrieve information from the file provided by the user.
    """

    lst = []
    # Read through the file line by line
    with open(file_name, 'r') as f:
        for line in f:
            # If it starts with a % or if it's an empty line (weird formatting in file) then continue
            if line[0] == "%" or len(line) <= 1:
                continue
            else:
                # If it is a valid line, then shove it into our list
                lst.append(line.strip())

    # Parse through list to recover information we need to solve problem
    num_processes = lst[0].split("=")[1] 
    num_resources = lst[1].split("=")[1]
    each_resource = lst[2].split(",")
    matrix = []
    for row in lst[3:]:
        r = row.split(",")
        matrix.append(r)
    # Returns a set of tuples for each parameter we need
    return num_processes, num_resources, each_resource, matrix

if __name__ == "__main__":
    # Change s to be a CLI in the future with a prompt to user.
    file_name  = "Project-2-input-example.txt"

    # Can recover data like this,
    num_processes, num_resources, each_resource, matrix = store_file(file_name)

    print(f'num_processes -> {num_processes}')
    print(f'num_resources -> {num_resources}')
    print(f'each_resource -> {each_resource}')
    print('Matrix is ...')
    for row in matrix:
        print(row)

