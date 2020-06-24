import random
class Word:
    def __init__(self):
        self.OverallIndex = 0
        self.word = None
        self.WordType = None
        self.Response = [None] * 1000
        self.Likely = [0] * 1000

    # update reply keeps arrays up to date for response selection
    def updateReply(self, word):
        # preset found to false
        found: bool = False
        # Search Response Array for word
        for i in range(len(self.Response)):
            if self.Response[i] == word:
                found = True
                break

        # “i“ will equal index of word in response Array
        if found:  # Word found increment Usage value rate!
            self.Likely[i] += 1
        else:  # Add Word if not seen before!
            self.Response[self.OverallIndex] = word
            self.Likely[self.OverallIndex] += 1
            self.OverallIndex += 1

    # form reply actually returns a word based on response and likely arrays!
    def getReply(self):
        if self.Likely[0] != 0:
            max = 0
            for i in range(self.OverallIndex):
                max += self.Likely[i]
            max = max - random.randrange(max)
            tempIndex = self.OverallIndex - 1
            for j in range(self.OverallIndex):
                if max > 0:
                    max = max - self.Likely[tempIndex]
                    tempIndex -= 1
            return self.Response[tempIndex + 1]
        else:
            return self.word

    def getAllReplies(self):
        return self.Response

    def getLikely(self):
        return self.Likely

    def setWord(self, word):
        self.word = word

    def setType(self, wordType):
        self.wordType = wordType

