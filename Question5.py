import random

rolled = []
rolledtimes = 0
biggest = []

# freq = int(input('How many times would you like to roll the dice? '))
freq = 1000


def roll():
    randy = str(random.randrange(1, 7))
    sandy = str(random.randrange(1, 7))
    rand = int(randy+sandy)
    return rand


# def probability():
#     for i in range(0, len(count)):
#         print('Calculation of probability:')
#         percentage = "{:.2f}".format((count[i] / freq)*100)
#         percent = str(percentage) + '%'
#         print(' ', i + 1, ':', percent)

def probability(i):
        percentage = "{:.2f}".format((count[i] / freq)*100)
        percent = str(percentage) + '%'
        return percent


def theoretical():
    result = "{:.2f}".format((1/6)*freq)
    denominator = "{:.2f}".format(((1/6)*freq)*6)
    print('\nIn theory, each dice should roll {} out of {} times'.format(
        result, denominator))


def findBiggest():
    for i in range(1, 7):
        biggest.append(rolled.count(i))
    print('\n', 'The most times a dice is rolled is', max(biggest), 'times')


def findSmallest():
    for i in range(1, 7):
        biggest.append(rolled.count(i))
    print('\n', 'The least times a dice is rolled is', min(biggest), 'times')


for i in range(1, freq + 1):
    number = roll()
    rolled.append(number)
    rolledtimes += 1
count = [rolled.count(11), rolled.count(12), rolled.count(13), rolled.count(14), rolled.count(15), rolled.count(16),
         rolled.count(21), rolled.count(22), rolled.count(
             23), rolled.count(24), rolled.count(25), rolled.count(26),
         rolled.count(31), rolled.count(32), rolled.count(
             33), rolled.count(34), rolled.count(35), rolled.count(36),
         rolled.count(41), rolled.count(42), rolled.count(
             43), rolled.count(44), rolled.count(45), rolled.count(46),
         rolled.count(51), rolled.count(52), rolled.count(
             53), rolled.count(54), rolled.count(55), rolled.count(56),
         rolled.count(61), rolled.count(62), rolled.count(63), rolled.count(64), rolled.count(65), rolled.count(66)]
print(count)
print(len(count))
# 35

print('After being rolled {} times\n\n'.format(rolledtimes))
print('Dice \t count')
i = 1
z = 0

while(i < 7):
    j = 1
    while(j < 7):
        print('{}-{}  \t  {} '.format(i, j, count[z]), end="", flush=True)
        for item in range(1, count[z]):
            print("*", end='')
        print(probability(z))
        j += 1
        z += 1
    i += 1

# probability()
# findBiggest()
# findSmallest()
# theoretical()
