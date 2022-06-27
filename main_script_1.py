import os


def main():
    i = 0
    file_path = "C:/Users/Michael Oladimeji/Pictures"
    # For every file in Pictures
    for file in os.listdir(file_path):
        original_filename = file_path + file
        custom_filename = "img" + str(i) + ".jpg"
        custom_filename = file_path + custom_filename
        os.rename(original_filename, custom_filename)
        i += 1

# If this is the main script in the project, run the code


if __name__ == "__main__":
    main()
