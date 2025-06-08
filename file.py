import collections
def count_chars(x):
    with open(x, "r") as file:
        print(f"Number of characters: {len(file.read())}")

def count_words(x):
    with open(x, "r") as file:
        counter = collections.Counter(file.read().split())

    target = input("What word to count? ").strip()
    target_count = counter[target]
    print(f"'{target}' appeared {target_count} times")
def count_lines(x):
    with open(x, "r") as file:
        print(f"Number of lines: {len(file.readlines())}")

file_name = input("Enter a file name: ")
count_chars(file_name)
count_words(file_name)
count_lines(file_name)

