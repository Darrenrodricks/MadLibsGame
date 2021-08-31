# Mad-Libs Game, Mad Libs is a phrasal template word game created by Leonard Stern and Roger Price. It consists of
# one player prompting others for a list of words to substitute for blanks in a story before reading aloud. The game
# is frequently played as a party game or as a pastime.

loop = 1
while (loop < 10):
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")
    loop = loop + 1