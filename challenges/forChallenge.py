"""
 Program Flow Challenge
"""

__author__ = 'dev'
SEGLEN = 0
SEGNUM = 0
SEGIDX = 0
IPNUM = input("Enter an IP address: ")
#IPNUM = '127'
if IPNUM != '':
    for i in IPNUM:
        if (i == '.') and (SEGIDX != 0):
            SEGNUM += 1
            print("Length of Segment {0}".format(SEGLEN))
            SEGLEN = 0
        elif (SEGIDX == (len(IPNUM)) - 1) and (i != '.'):
            SEGLEN += 1
            SEGNUM += 1
            print("Length of Segment {0}".format(SEGLEN))
        elif i != '.':
            SEGLEN += 1
        SEGIDX += 1
    print("Number of Segments: {0}".format(SEGNUM))
else:
    print("No Input")


''' SEGNUM = 0
SEGLEN = 0
IPNUM = input('Please enter an IP address: ')
if IPNUM != '':
    for i in IPNUM:
        if i == '.':
            print('Segment {0}\'s length is {1}'.format(SEGNUM, SEGLEN))
            SEGNUM += 1
            SEGLEN = 0
        else:
            SEGLEN += 1
    print('Segment {0}\'s length is {1}'.format(SEGNUM, SEGLEN))
else:
    print('No Input Given') '''
