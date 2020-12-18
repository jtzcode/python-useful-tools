import sys, json, requests

if len(sys.argv) < 2:
    print('Usage: weather-report.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])