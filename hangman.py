import easygui as g
import random, json


dict2 ={
    1:"O",
    2:"/",
    3:"|",
    4:"\\",
    5:"/",
    6:"\\"    
}


def wrd(word):
    the_word=""
    for ltr in word:
        if ltr in [" ",":","'",",","!","?"]:
            the_word+=ltr
        else:
            the_word+="*"
    return the_word

def board(wrd,num,used,dict1,dict2):
    word_length = len(wrd)
    half_of_it = len(wrd)*" "
    if num == 0:
        pass
    else:
        dict1[num]=dict2[num]
    used=list(used)
    return f'''\"Only one letter, please\"
    {word_length*" "}{(word_length+5)*"_"}
    {30*" "}{word_length*" "}{dict1[1]}{word_length*" "}|
    {30*" "}{half_of_it[:-1]}{dict1[2]}{dict1[3]}{dict1[4]}{half_of_it[:-1]}|
    {30*" "}{half_of_it[:-1]}{dict1[5]} {dict1[6]}{half_of_it[:-1]}|
    {30*" "}{word_length*"  "} |
    {30*" "}{wrd}
    You've already used {",".join(used)}
    \"You have {str(6-num)} tries left\"'''

name = g.enterbox("Hi. What is your name?")
answer = g.ynbox(f"Well {name} nice to meet you, do you wanna play a hangman game?")


while bool(answer):
    with open("movies.json") as json_file:
        data=json.load(json_file)
    word=random.choice(data)
    the_word=wrd(word)
    num=0
    used=set()
    dict1={
    1:" ",
    2:" ",
    3:" ",
    4:" ",
    5:" ",
    6:" "
    
}
    while num < 7:
        if num>=6:
            answer=g.ynbox(f"You've lost!! It was \"{word}\" all the time!! Wanna play again?")
            break

        elif the_word == word:
            g.msgbox(f'''The answer is \"{word}\". You've won!''')
            answer=g.ynbox("Wanna play again?")
            break
        else:

            letter=g.enterbox(board(the_word,num,used,dict1,dict2))
            if len(letter)>1:
                continue

            used.add(letter.upper())

            if letter.lower() not in word.lower():
                num+=1
                g.msgbox(f"There is no {letter.upper()} in the name of this movie")
            
            else:
                the_word=list(the_word)
                for nums in enumerate(word):#creates a pair of touples,first is the number, hence [0]
                    if letter.lower() in nums or letter.upper() in nums:
                        the_word[nums[0]]=nums[1]
                    else:
                        pass
                the_word="".join(the_word)