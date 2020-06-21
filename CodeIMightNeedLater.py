
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

