import random

capitals = {'Jiangsu': 'Nanjing', 'Liaoning': 'Shenyang', 'Beijing': 'Beijing', 'Jiangxi': 'Nanchang', 'Sichuan': 'Chendu'}
for quizNum in range(5):
    quizFile = open('capitals%s.txt' % (quizNum + 1), 'w')
    answerFile = open('answers%s.txt' % (quizNum + 1), 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    
    provinces = list(capitals.keys())
    random.shuffle(provinces)

    for questionNum in range(5):
        correctAnswer = capitals[provinces[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        options = wrongAnswers + [correctAnswer]
        random.shuffle(options)

        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, provinces[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], options[i]))
        quizFile.write('\n')

        answerFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[options.index(correctAnswer)]))

quizFile.close()
answerFile.close()