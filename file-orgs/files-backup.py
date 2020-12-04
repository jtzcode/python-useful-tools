import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1
    
    print("Creating zip file %s..." % (zipFileName))
    backup = zipfile.ZipFile(zipFileName, 'w')

    for folder_name, sub_folders, file_names in os.walk(folder):
        backup.write(folder_name)

        for file in file_names:
            new_base = os.path.basename(folder) + '_'
            if file.startswith(new_base) and file.endswith('.zip'):
                continue
            backup.write(os.path.join(folder_name, file))

    backup.close()

backupToZip("C:\\Project\\python\\python-useful-tools")