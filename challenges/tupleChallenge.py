"""
 Tuple Challenge
"""

__author__ = 'dev'
IMELDA = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

TITLE, BAND, YEAR, TRACKS = IMELDA
print("Album Title: {0}".format(TITLE))
print("Album Band:  {0}".format(BAND))
print("Album Year:  {0}".format(YEAR))
''' print("Track {0}: {1}".format(TRACKS[0][0], TRACKS[0][1]))
print("Track {0}: {1}".format(TRACKS[1][0], TRACKS[1][1]))
print("Track {0}: {1}".format(TRACKS[2][0], TRACKS[2][1]))
print("Track {0}: {1}".format(TRACKS[3][0], TRACKS[3][1])) '''
for SONG in TRACKS:
    TRACK, TITLE = SONG
    print('\tTrack {}, Title: {}'.format(TRACK, TITLE))
    #print('\t', SONG)
