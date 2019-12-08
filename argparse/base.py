import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--arg1", type=int, default=0)
    parser.add_argument("-b", "--arg2", type=int, default=0)
    ns = parser.parse_args()
    print(ns.__dict__)
