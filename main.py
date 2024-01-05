import argparse
from pathlib import Path
from utils import compact_folder

# current working directory
CWD = Path.cwd().resolve()


def main(input_folder, output_zip, add_empty_folders, filters):
    # get output zip file path
    if bool(output_zip):
        out = Path(output_zip).resolve()
    else:
        out = CWD / f"{input_folder.name}.zip"

    # test ouput format
    if out.suffix != ".zip":
        print("ERROR! Invalid output file format! Only zip file accepted!")
        return False

    # get add empty folder option
    add_empty = bool(add_empty_folders)

    print(f"Creating zip file {out}...")
    if compact_folder(input_folder, out, add_empty, filters):
        print(f"Zip file was created: {out}")
        return True
    print(f"Fail to Create zip file from folder : {input_folder}")
    return False


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path of the folder to zip", type=str)
    parser.add_argument("-o", "--output", type=str,
                        help="output zipfile path (if none, will create file at the same directory of target folder)")
    parser.add_argument("-ae", "--addEmpty",
                        help="indicate that you want to add empty sub folders to final zip file. Default is False",
                        action="store_true")
    parser.add_argument("-f", "--filter", type=str,
                        help="files filter to add specific files types to final zip. Default is set to ('*') all files")

    # get arguments
    args = parser.parse_args()
    target_dir = Path(args.path)
    output = args.output
    add_empty = args.addEmpty
    files_filter = "*" if not args.filter else args.filter

    if not target_dir.exists():
        print("The target directory doesn't exist!")
        raise SystemExit(1)

    # runs main script
    if main(target_dir, output, add_empty, files_filter):
        raise SystemExit(0)
    else:
        raise SystemExit(1)