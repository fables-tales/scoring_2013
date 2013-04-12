#!/usr/bin/env python

import os
import sys
import yaml

import score

MATCH_ID = 'match-{0}'

def usage():
    print "Usage: score-match.py (league|knockout) MATCH_NUMBER"
    print "  Scores the match file at matches/MATCH_NUMBER.yaml"
    print "  Outputs scoring format suitable for piping at compd"


if len(sys.argv) is not 3:
    usage()
    exit(1)

style = sys.argv[1]
if style not in ['league', 'knockout']:
    usage()
    exit(2)

match_num = sys.argv[2]
match_file = "matches/{0}.yaml".format(match_num)

if not os.path.exists(match_file):
    print "Match file '{0}' doesn't exist. Have you created it?".format(match_file)
    usage()
    exit(3)

scores = yaml.load(open(match_file).read())
scorer = score.StrangeGameScorer(scores)
scorer.compute_cell_winners()

match_id = MATCH_ID.format(match_num)

for tla in scores.keys():
    this_score = scorer.compute_game_score(tla)
    print 'set-score {0} {1} {2}'.format(match_id, tla, this_score)

if style == 'league':
    print 'calc-league-points {0}'.format(match_id)
#else:
#    # Knockout
#    print 'update-knockout-after {0}'.format(match_id)
