import sys
import os


def validate_url(url: str):
    pass


def validate_path(path: str):
    if not os.path.exists(path):
        raise FileExistsError(f"Path {path} does not exist.")


def get_args():
    args = {"output_folder": ".", "url": ""}
    if len(sys.argv) == 2:
        args["url"] = sys.argv[1]
    elif len(sys.argv) == 4:
        if sys.argv[1] == "-o":
            args["output_folder"] = sys.argv[2]
            args["url"] = sys.argv[3]
        elif sys.argv[2] == "-o":
            args["output_folder"] = sys.argv[3]
            args["url"] = sys.argv[1]
    else:
        raise SyntaxError(f"Expected 2 or 4 arg. Got {len(sys.argv)}")
    validate_path(args["output_folder"])
    validate_url(args["url"])
    return args


def main():
    print("hello")
    args = get_args()
    print(args)
