def main():
    try:
        configuration = open('./Documents/Launch/MisAvances/Kata10/config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")