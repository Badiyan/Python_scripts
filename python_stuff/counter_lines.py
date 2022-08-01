FILENAME = "input2.txt"

reader = open(FILENAME, encoding='utf-8')
lines = reader.readlines()
reader.close()

writer = open("output2.txt", "w", encoding='utf-8')
lines_counter = 0

for line in lines:
    stripped_line = line.strip()
    if stripped_line:
        writer.write(stripped_line)
        writer.write("\n")
        lines_counter += 1

writer.close()
print(lines_counter)