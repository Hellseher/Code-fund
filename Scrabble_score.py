# Scrabble Score
#
#
# Scrabble is a game where players get points by spelling words. 
# Words are scored by adding together the point values of each 
# individual letter (we'll leave out the double and triple letter 
# and word scores for now).

def scrabble_score(word)
  word = word.lower()
  restuld = 0
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
           "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
           "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
           "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
           "x": 8, "z": 10}
  for j in word:
    for i n score:
      if j == i:
        result += score[i]
  return restul
