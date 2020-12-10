import sys, re, os, json, io

target_folder = './'
translation_folders = []
pilot = 'en'
resources = {}
translations = {}
supported_languages = ['en', 'de', 'es', 'fr', 'ja', 'it', 'pt', 'zh', 'nl']
searchForTranslation = False
#lang_matcher = re.compile(r'(.*)\.json$')

def merge_two_dicts(x, y):
    if x is None:
        x = {}
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def check_file(file_name):
    with open(os.path.abspath(target_folder + '\\' + pilot + '.json'), 'rb') as pilot_json:
        resources[pilot] = json.load(pilot_json)

    pilot_json.close()

    with open(os.path.abspath(target_folder + '\\' + file_name + '.json'), 'rb') as lang_json:
        resources[file_name] = json.load(lang_json)

    lang_json.close()

    if searchForTranslation:
        translations.setdefault(file_name, {})
        for folder in translation_folders:
            resource_path = os.path.abspath(folder + '\\' + file_name + '.json')
            if os.path.exists(resource_path):
                print("\nFound translation files for " + file_name + ": " + resource_path)
                with open(resource_path, 'rb') as tran_json:
                    translations[file_name] = merge_two_dicts(translations[file_name], json.load(tran_json))
        tran_json.close()
    
    result = []
    for key in resources[pilot]:
        if key not in resources[file_name]:
            value = resources[pilot][key]
            if searchForTranslation and key in translations[file_name]:
                value = translations[file_name][key]
                print("Found new value for key %s: %s" % (key, value))
            result.append("\"" + key + "\": \"" + value + "\",")

    # Write result to file
    with io.open('%s_%s_result.txt' % (pilot, file_name), 'w', encoding="utf8") as resultFile:
        for string in result:
            resultFile.write(string + '\n')

    resultFile.close()

if __name__ == '__main__':
    if len(sys.argv) > 4:
        raise Exception('No more than 3 parameters can be specified')
    if len(sys.argv) >= 2:
        if sys.argv[1] not in supported_languages:
            raise Exception('Unsupported language: %s' % sys.argv[1])
    if len(sys.argv) >= 3:
        pilot = sys.argv[1]
        target_folder = sys.argv[2]
    if len(sys.argv) == 4:
        translation_folders = sys.argv[3].split(',')
    
    searchForTranslation = len(translation_folders) != 0
    for resource_file in os.listdir(target_folder):
        if resource_file.endswith('.json') and not resource_file.startswith(pilot):
            root, ext = os.path.splitext(resource_file)
            check_file(root)
