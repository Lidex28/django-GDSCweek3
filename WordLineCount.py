def count_words_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            line_count = len(lines)
            return word_count, line_count
    except FileNotFoundError:
        print("File not found.")
        return None, None

if __name__ == "__main__":
    filename = "sample.txt"  # Change to your file name
    words, lines = count_words_lines(filename)
    if words is not None:
        print(f"Words: {words}, Lines: {lines}")
