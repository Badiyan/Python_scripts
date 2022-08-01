INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"

reader = open(INPUT_FILENAME, encoding='utf-8')
writer = open(OUTPUT_FILENAME, "w", encoding='utf-8')

for line in reader:
    transformed_line = line.upper()
    writer.write(transformed_line)

reader.close()
writer.close()