#!/usr/bin/env python

import os
import sys
import yaml

import score

def usage():
    print "Usage: score-match.py MATCH_NUMBER"
    print "  Scores the match file at matches/MATCH_NUMBER.yaml"
    print "  Outputs scoring format suitable for piping at compd"


if len(sys.argv) is not 2:
    usage()
    exit(1)

match_num = sys.argv[1]
match_file = "matches/{0}.yaml".format(match_num)

if not os.path.exists(match_file):
    print "Match file '{0}' doesn't exist. Have you created it?".format(match_file)
    usage()
    exit(2)

scores = yaml.load(open(match_file).read())
scorer = score.StrangeGameScorer(scores)
scorer.compute_cell_winners()

for tla in scores.keys():
    this_score = scorer.compute_game_score(tla)
    print 'set-score {0} {1} {2}'.format(match_num, tla, this_score)
print 'calc-league-points {0}'.format(match_num)
