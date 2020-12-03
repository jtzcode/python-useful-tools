import os

jenkinsfile_template = open('generic-template.txt', 'r')
yaml_template = open('pipeline-yaml.txt', 'r')
origin_jenkinsfile = open('Jenkinsfile', 'r')

try:
    jenkinsfile = jenkinsfile_template.readlines()
    yamlfile = yaml_template.readlines()
    originJenkinsfile = origin_jenkinsfile.readlines()
except Exception as error:
    print('File reading error: ' + error)
finally:
    jenkinsfile_template.close()
    yaml_template.close()
    origin_jenkinsfile.close()