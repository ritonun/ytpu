# main.py

import sys
import os
import ytpu.downloader as dl
from ytpu.file_io import write_json, load_json


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


def get_local_videos(folder_path):
    files = os.listdir(folder_path)
    all_files = []
    for file in files:
        if os.path.isfile(os.path.join(folder_path, file)):
            all_files.append(file)
    return all_files


def main():
    print("Welcome to ytpu")

    # parse args input
    args = get_args()
    print(f"INPUT URL: {args['url']}\nINPUT OUTPUT_PATH: {args['output_folder']}")

    # find local videos
    local_videos = get_local_videos(args["output_folder"])
    print(f"Found {len(local_videos)} local videos")

    # get videos from playlist
    # data = dl.get_playlist_info(args["url"])
    # write_json("temp.json", data, mode="w")
    data = load_json("temp.json")
