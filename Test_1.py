# Write a program to read a file and find the number of lines, words, and characters in the given file.

def find():
    with open("input.txt", 'r') as file:
        no_lines = 0
        no_words = 0
        no_char = 0
        for data in file:
            line = data.strip('\n')
            words = line.split()
            no_lines += 1
            no_words += len(words)
            no_char += len(line)

        file.close()
    return f"Number of lines: {no_lines}\nNumber of words: {no_words}\nNumber of characters: {no_char}"


if __name__ == '__main__':
    print(find())
