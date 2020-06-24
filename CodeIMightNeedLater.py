
    # code for NLTK POS
# MyText = Dictionary[i]
# tokenized = sent_tokenize(MyText)
# for i in tokenized:
#     # Word tokenizers is used to find the words
#     # and punctuation in a string
#     wordsList = nltk.word_tokenize(i)
#
#     # removing stop words from wordList
#     # wordsList = [w for w in wordsList if not w in stop_words]
#
#     #  Using a Tagger. Which is part-of-speech
#     # tagger or POS-tagger.
#     tagged = nltk.pos_tag(wordsList)
#     print(tagged)



    # code for sql database
# try:
#     mydb = mysql.connector.connect(
#         user="root",
#         password="waerty90",
#         host="localhost",
#         database="wordsdb"
#     )
#     print(mydb)
# except mysql.connector.Error as e:
#     if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("something wrong with password or user")
#     else:
#         print(e)
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#     print(tb)


        #update likely
    # def updateLikely(self):
    #     for i in range(1000):
    #         if self.Response[i] is not None:
    #             self.Likely[i] += 1


# learn full conversations from array
    # print(input)
    # conversation = []
    # for m in range(len(conversation) - 1):
    #     input = conversation[m]
    #     response = conversation[m+1]
    #     parseInput = input.split(" ")
    #     parseResponse = response.split(" ")
    #     for n in range(len(parseInput)):
    #         resultInput = search(Dictionary, parseInput[n]) // 2
    #         # print(words[resultInput].wordType)
    #         # result contains index of word object!
    #         for j in range(len(parseResponse)):
    #             resultResponse = search(Dictionary, parseResponse[j]) // 2
    #             # print(words[resultResponse].wordType)
    #             if words[resultInput].wordType == words[resultResponse].wordType and resultInput > -1 and resultResponse > -1:
    #                 words[resultInput].updateReply(parseResponse[j])
    #                 # print("the word is = " + words[resultInput].word)
    #                 # print("reply is = " + words[resultInput].getReply())
    #             else:
    #                 l = 0
