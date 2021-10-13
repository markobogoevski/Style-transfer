from utils import *
import os


def main():
    # Specify input text path
    input_text_path = "../Authors/Raw/Lovecraft/lovecraft.txt"

    # Clean the merged text
    cleaned_lines = clean_text(input_text_path)

    # Split the cleaned into train dev and test sets
    # Train = 0.7, dev = 0.1, test = 0.2
    train_split = 0.7
    dev_split = 0.1
    train_lines, dev_lines, test_lines = split_text(cleaned_lines, train_split, dev_split)

    # Save the processed lines
    path_save = "../Authors/Processed/Lovecraft"
    os.makedirs(path_save, exist_ok=True)
    train_path = os.path.join(path_save, "lovecraft.train.txt")
    dev_path = os.path.join(path_save, "lovecraft.dev.txt")
    test_path = os.path.join(path_save, "lovecraft.test.txt")

    with open(train_path, 'w', encoding='utf8') as f:
        f.writelines(train_lines)
    with open(dev_path, 'w', encoding='utf8') as f:
        f.writelines(dev_lines)
    with open(test_path, 'w', encoding='utf8') as f:
        f.writelines(test_lines)


if __name__ == "__main__":
    main()
