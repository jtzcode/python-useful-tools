import time

input()
print('Start...')
startTime = time.time()
lastTime = startTime
lapCount = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapCount, totalTime, lapTime), end='')

        lapCount += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone. EXIT.')


