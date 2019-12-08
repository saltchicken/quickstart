import argparse

def main(arg1: int, arg2: int):
    print(arg1, arg2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--arg1", type=int, default=0)
    parser.add_argument("-b", "--arg2", type=int, default=0)
    ns = parser.parse_args()
    main(**ns.__dict__)
