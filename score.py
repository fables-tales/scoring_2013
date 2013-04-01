
import yaml

def score_line(line, letter):
    #find the number of things in the line that match the letter
    count = len([x for x in line if x == letter])

    #pulled from http://oeis.org/A000217
    #basically gives 0, 1, 3, 6 depending on the number in count
    if 0 <= count <= 3:
        return count*(count+1)/2

class StrangeGameScorer:
    def __init__(self, raw_squares):
        self.raw_squares = raw_squares
        #create empty winners array as a 3x3 grid of None
        self.winners = [[None]*3 for i in range(0,3)]

    def compute_cell_winners(self):
        for y in range(3):
            for x in range(3):
                self.winners[y][x] = self.cell_winner(x,y)


    def compute_game_score(self, letter):
        return self.score_rows(letter) + self.score_columns(letter)

    #private functions below!

    def score_columns(self, letter):
        score = 0
        for x in range(3):
            col = self.extract_winner_column(x)
            score += score_line(col, letter)

        return score

    def score_rows(self,letter):
        score = 0
        for y in range(3):
            row = self.winners[y]
            score += score_line(row, letter)
        return score

    def extract_winner_column(self, x):
        return [self.winners[i][x] for i in range(3)]

    def unique_highest(self, cell_scores):
        #determine if the cell scores has a unique highest, return true
        #if it does, and false if it doesn't

        values = cell_scores.values()
        highest = sorted(values, reverse=True)
        return highest[0] != highest[1]

    def cell_winner(self,x,y):
        #determines who has won the cell at x,y
        cell_scores = {}
        for letter in "abcd":
            cell_scores[letter] = self.cell_score(letter, x, y)

        if self.unique_highest(cell_scores):
            return max(cell_scores, key=lambda x:cell_scores[x])
        else:
            return None

    def cell_score(self, letter, x, y):
        score = self.raw_squares[letter]["squares"][y][x]
        #use the character p if something is on a pedestal
        #and if it is we use float("inf") as the score
        if score == 'p':
            score = float("inf")
        return score

if __name__ == "__main__":
    scores = yaml.load(open("tokens.yml").read())
    x = StrangeGameScorer(scores)
    x.compute_cell_winners()
    print "a scores", x.compute_game_score("a")
    print "b scores", x.compute_game_score("b")
    print "c scores", x.compute_game_score("c")
    print "d scores", x.compute_game_score("d")
