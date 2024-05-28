import json, os, shutil


settings_file = open("backup_settings.txt", 'r')
settings = json.loads(settings_file.read().strip())

minecraft_folder = settings["minecraft_folder"]
to_backup = settings["to_backup"]
destination = settings["destination"]
if destination == "":
    destination = "."
destination = destination + "/.minecraft"

os.makedirs(destination, exist_ok=True)

for path in to_backup:
    print("Saving " + path, end='')
    try:
        file_name = os.path.basename(path)
        new_path = os.path.join(minecraft_folder, path.lstrip('\\/'))
        if os.path.isdir(new_path):
            destination_path = os.path.join(destination, path)
            os.makedirs(destination_path, exist_ok=True)
            shutil.copytree(new_path, destination_path, dirs_exist_ok=True)
        else:
            relative_path = os.path.dirname(path)
            destination_path = os.path.join(destination, relative_path)
            os.makedirs(destination_path, exist_ok=True)
            shutil.copy2(new_path, destination_path)
        print(" Success")
    except:
        print(" Failure")

