import argparse

parser = argparse.ArgumentParser(prog="main", description="just a test")
parser.add_argument("--env", type=str, help="environment")
args = parser.parse_args()

print("hello world from main.py : )")
print("env: ", args.env)
