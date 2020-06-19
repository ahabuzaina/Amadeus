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
            self.OverallIndex += 1

    # form reply actually returns a word based on response and likely arrays!
    def getReply(self):
        return self.Response[self.OverallIndex - 1]

    def setWord(self, word):
        self.word = word

    def setType(self, wordType):
        self.wordType = wordType
