import argparse

def example_pass_arguments(arg1: int, arg2: int):
    print(arg1, arg2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--arg1", type=int, default=0)
    parser.add_argument("-b", "--arg2", type=int, default=0)
    ns = parser.parse_args()
    example_pass_arguments(**ns.__dict__)
