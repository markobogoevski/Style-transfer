import nltk
import glob
import os


def clean_text(text_source, path=True, capital=True):
    """
    Expects path to .txt file of full merged text. Tokenizes and converts to lowercase
    :param capital: Whether it contains titles (to avoid them)
    :param path: Whether it is a path or string
    :param text_source: Text or path to text
    :return: Cleaned text ready to be split as list of lines
    """
    text = text_source

    if path:
        with open(text_source, 'r', errors="ignore", encoding='utf8') as file:
            text = file.read()

    lines = nltk.sent_tokenize(text)
    valid_punctuation = [',', '.', '!', '?', '-', ';', "'", '(', ')']
    cleaned_lines = []
    for line in lines:
        tokens = nltk.word_tokenize(line)
        tokens = [word for word in tokens if word.isalpha() or word in valid_punctuation]
        if capital:
            # Avoid titles
            tokens = [word for word in tokens if not word.isupper() or len(word) == 1]
        # convert to lower case
        tokens = [word.lower() for word in tokens]
        cleaned_lines.append(" ".join(tokens))
        cleaned_lines.append('\n')
    return cleaned_lines


def split_text(cleaned_lines, train_split, dev_split):
    """
    Splits cleaned lines into train, dev and test sets
    :param cleaned_lines: List of str
    :param train_split:
    :param dev_split:
    :return: Sets(lines of strings)
    """
    num_lines = len(cleaned_lines)
    train_fraction = int(num_lines * train_split)
    dev_fraction = int(num_lines * (train_split + dev_split))
    train_lines = cleaned_lines[:train_fraction]
    dev_lines = cleaned_lines[train_fraction:dev_fraction]
    test_lines = cleaned_lines[dev_fraction:]
    return train_lines, dev_lines, test_lines


def merge_files(input_path, merge_name):
    """
    Merges several txt files into single txt
    :param input_path: Dir to folder
    :return: merged text, str
    """
    read_files = glob.glob(f"{input_path}\\*.txt")
    path = os.path.join(input_path, merge_name)

    with open(path, "wb", encoding='utf8') as outfile:
        for f in read_files:
            with open(f, "rb", encoding='utf8') as infile:
                outfile.write(infile.read())
