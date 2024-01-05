import argparse
from pathlib import Path
from utils import compact_folder

# current working directory
CWD = Path.cwd()


def main(input_folder, output_zip, add_empty_folders, filters):
    # get output zip file path
    if bool(output_zip):
        out = Path(output_zip)
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
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("output")
    parser.add_argument("addEmpty")
    parser.add_argument("filter")
    parser.add_argument("help")
    args = parser.parse_args()

    target_dir = Path(args.path)
    output = args.output
    add_empty = args.addEmpty
    files_filter = args.filter
    help = args.help

    # if help argument
    if help:
        readme = CWD / "README.md"
        print(readme.read_text())
        raise SystemExit(0)

    if not target_dir.exists():
        print("The target directory doesn't exist!")
        raise SystemExit(1)

    # runs main script
    if main(target_dir, output, add_empty, files_filter):
        raise SystemExit(0)
    else:
        raise SystemExit(1)