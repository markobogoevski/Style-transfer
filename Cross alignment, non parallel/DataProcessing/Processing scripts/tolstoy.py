from utils import *
import os


def main():
    # Specify input folder path
    input_folder_path = "../Authors/Raw/Tolstoy"

    # Merge the txt files into a single txt file and clean or clean if already merged
    merge_path = '../Authors/Raw/Tolstoy/tolstoy.txt'
    if not os.path.exists(merge_path):
        merged_txt = merge_files(input_folder_path, 'tolstoy.txt')
        cleaned_lines = clean_text(merged_txt, path=False, capital=False)
    else:
        cleaned_lines = clean_text(merge_path)

    # Split the cleaned into train dev and test sets
    # Train = 0.7, dev = 0.1, test = 0.2
    train_split = 0.7
    dev_split = 0.1
    train_lines, dev_lines, test_lines = split_text(cleaned_lines, train_split, dev_split)

    # Save the processed lines
    path_save = "../Authors/Processed/Tolstoy"
    os.makedirs(path_save, exist_ok=True)
    train_path = os.path.join(path_save, "tolstoy.train.txt")
    dev_path = os.path.join(path_save, "tolstoy.dev.txt")
    test_path = os.path.join(path_save, "tolstoy.test.txt")

    with open(train_path, 'w', encoding='utf8') as f:
        f.writelines(train_lines)
    with open(dev_path, 'w', encoding='utf8') as f:
        f.writelines(dev_lines)
    with open(test_path, 'w', encoding='utf8') as f:
        f.writelines(test_lines)


if __name__ == "__main__":
    main()
