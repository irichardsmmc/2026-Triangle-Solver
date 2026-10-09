# Create file to hold data
file_name = "write_experiment"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# Strings to write to file
heading = "=== Triangle Solver ===\n"
content = "Random content"
more = "A bit more content"

# List of strings
to_write = [heading, content, more]

# Print output
for item in to_write:
    print(item)

# Write item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
