## Overview
This tool is designed to help you compare the resource files with the pilot file (e.g. EN) and find out all the missing strings. It can also help you find the the possible translations for those missing keys in the folders specified.
## Usage
### Command
`python app.py en C:\Project\athena\sharefileweb\Src\UI\ShareFileWeb\src\languages C:\Project\athena\identity4\Src\UI\identity\src\languages,C:\Project\athena\activedirectoryweb\Src\UI\ActiveDirectoryWeb\src\languages`
### Parameters
- [pilot language]: The pilot languge, default to `en`
- [target folder]: The working dir to read the files to be compared.
- [translation folder list]: The directory to find translation resources. Files at this folder should be also in JSON format. More than 1 folders can be joined with comma.
### Support
- Languages: 'en', 'de', 'es', 'fr', 'ja', 'it', 'pt', 'zh', 'nl'
- Resource format: JSON

