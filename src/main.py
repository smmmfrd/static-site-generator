import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public dir...")
    copy_files_recursive(dir_path_static, dir_path_public)


def copy_files_recursive(source_path, target_path):
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for filename in os.listdir(source_path):
        from_path = os.path.join(source_path, filename)
        dest_path = os.path.join(target_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)


main()
