#SRobo2013 Scorer

This is a script to do scores for the [Student Robotics](http://srobo.org) 2013
game entitled 'A Strange Game'.
To use it, copy and edit `valid_scorecards/tokens.yml` file,
 and pass the name as the only command line argument.
The entries in the tokens files are the token counts
 (or the letter 'p' if the robot put a token on a pedestal)
 for the given robot.

Example:
~~~~
python scores.py valid_scorecards/tokens.yml
~~~~
