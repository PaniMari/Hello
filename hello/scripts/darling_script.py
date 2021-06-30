from colorama import Fore

def say_hello(text):
    print(text)

def main():
    say_hello(Fore.GREEN + "Hey darling")

if __name__ == '__main__':
    main()
