import shutil, os, re

datePattern = re.compile(r"""^(.*?)     # all text before the date
    ((0|1)?\d)-                 # one or two digits for the month
    ((0|1|2|3)?\d)-            # one or two digits for the day
    ((19|20)\d\d)             # four digits for the year
    (.*?)$                     # all text after the date
    """, re.VERBOSE)

for fileName in os.listdir('.'):
    matcher = datePattern.search(fileName)

    if matcher == None:
        continue

    beforePart  = matcher.group(1)
    monthPart  = matcher.group(2)
    dayPart  = matcher.group(4)
    yearPart  = matcher.group(6)
    afterPart  = matcher.group(8)

    newFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    fileName = os.path.join(absWorkingDir, fileName)
    newFileName = os.path.join(absWorkingDir, newFileName)

    print('Renaming "%s" to "%s"...' % (fileName, newFileName))

    shutil.move(fileName, newFileName)
