def load_tle(file_name):
    # Load TLE data from a text file.
    with open(file_name, "r") as file:
        lines = file.readlines()
    return lines
