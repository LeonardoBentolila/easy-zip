from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
from tqdm import tqdm
import textwrap


def ask_user(msg):
    inp = input(msg)
    if not inp:
        return False
    return inp


def format_file_path(file_path, limit=50):
    """
    format the string to get fixed size in the loading bar
    :param file_path: str string to format
    :param limit: int limit length of the formatted string
    :return: str formatted string
    """
    if len(file_path) < limit:
        return file_path.ljust(limit, " ")
    split = textwrap.wrap(file_path, int((limit/2) - 3))
    last_part = split[-1]
    return "...".join([split[0], last_part.ljust(int(limit/2), " ")])


def compact_folder(folder, zip_path, add_empty_folders=False, filter_items="*"):
    """
    compact folder and all content into zip file
    :param folder: source folder to compress
    :param zip_path: final zipfile to generate
    :param add_empty_folders: bool to tell if wants do add empty folders to the zip
    :param filter_items: filter items to add in final zip file (default is all files *)
    :return: str zipfile path generated
    """
    error_list = []
    sub_paths = folder.rglob(filter_items)
    if not add_empty_folders:
        sub_paths = list(filter(lambda x: not x.is_dir() or len(x.glob("*")) != 0, sub_paths))
    print(f"{len(sub_paths)} files listed...")
    digits = len(str(len(sub_paths)))
    pb = tqdm(total=len(sub_paths), desc="start compressing...", leave=False)
    with ZipFile(zip_path, 'w', compression=ZIP_DEFLATED) as zip_file:
        for i, item in enumerate(sub_paths):
            pb.set_description_str(f"Compacting File [{i:0{digits}d}/{len(sub_paths)}]: "
                                   f"{format_file_path(item['relative_path'])}")
            pb.update()
            try:
                zip_file.write(item["path"], item["relative_path"])
            except Exception as e:
                print(e)
                error_list.append(item["relative_path"])
    pb.clear()
    print(f"Compress finished with {len(error_list)} errors")
    if len(error_list) != 0:
        print("Files that failed to add in final zip: ")
        for item in error_list:
            print(f"- {item}")
    return zip_path
