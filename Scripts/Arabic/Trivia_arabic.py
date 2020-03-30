# This code was written by Codegurus on Fiverr
# Compactible to run on Python3.7

### ARABIC CHANNEL BOT
# This is a Trivia Game built into a Telegram Bot
# This Bot reads from  a file named ARABIC.CSV

# Importing the needed dependencies for the program
import telebot
from telebot import types
import time
import csv
import random
import emoji
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import operator
from googletrans import Translator


# Accessing and activating the TriviaBot
token = "700418741:AAGOhJ4OqFwA7ffy49hiPv70b7Zrf2-BtUs"
bot = telebot.TeleBot(token=token)
translator = Translator()

chat_id = -1001253210227

# Needed variables
Admins = [633265213, 865996339]

question = "" # Question
answer = ""  # Answer
pick = []  # Options
winners = []  # List of winners chat information
answers = 0   # Number of answers
correct = 0   # Number of correct answers
incorrect = 0   # Number of incorrect answers

condition = True

scoreboard_x = []
scoreboard = {}

def trivia_file():
        """Trivia file for importing questions"""

        global question
        global answer
        global pick
        with open("arabic.csv", "r") as f:
                reader = csv.reader(f)
                quiz = list(reader) # this is to read the csv file into the program
                question, ans = random.choice(quiz)
                o1, b = random.choice(quiz)
                o2, c = random.choice(quiz)
                o3, d = random.choice(quiz)                
                answer = question.translate(desk=ar)
                option1 = o1.translate(desk=ar)
                option2 = o2.translate(desk=ar)
                option3 = o3.translate(desk=ar)
                pick = [answer, option1, option2, option3]
                random.shuffle(pick)
                # Random selection for the question
                
                return question, answer, pick

@bot.callback_query_handler(func=lambda call: True)
def trivia_answer(call):
        """Options for Trivia Questions"""

        global winners
        global answers
        global correct
        global incorrect
        global condition
        global scoreboard

        print(f"{call.from_user.id} the from user {call.from_user.username}")
        print(call.message.chat)
        if call.data == "start" and call.from_user.id in Admins:
                trivia_game(call.message)
                condition = True
        if call.data == "stop" and call.from_user.id in Admins:
                stop_trivia(call.message)
                condition = False
        if call.data == "pause" and call.from_user.id in Admins:
                condition = False
                pause_trivia(call.message)
        if call.data == "continue" and call.from_user.id in Admins:
                condition = True
                trivia_game(call.message)
        if call.data == "stats":
                trivia_scoreboard(call.message)
                condition = False
        if call.data == "rank":
                user_rank(call.message)

        if call.data == "A" and condition == True:
                if pick[0] in answer:
                        # user got the right answer
                        bot.send_message(chat_id, emoji.emojize(f":trophy: Congratulations {call.from_user.username}, your answer is correct!!! You got 1 point", use_aliases=True))
                        if call.from_user.username in winners:
                                scr = scoreboard.get(call.from_user.username)
                                scr += 1
                                dict = {call.from_user.username: scr}
                                scoreboard.update(dict)
                        else:
                                winners.append(call.from_user.username)
                                dict = {call.from_user.username: 0}
                                scoreboard.update(dict)
                        print(call.from_user.username)
                        answers += 1
                        correct += 1
                        trivia_game(call.message)
                else:
                        # user failed
                        bot.send_message(chat_id, emoji.emojize(f":turtle: Sorry {call.from_user.username}, but your answer is wrong. Better next time", use_aliases=True))
                        print(call.from_user.username)
                        answers += 1
                        incorrect += 1
                
        if call.data == "B" and condition == True:
                if pick[1] in answer:
                        # user got the right answer
                        bot.send_message(chat_id, emoji.emojize(f":trophy: Congratulations {call.from_user.username}, your answer is correct!!! You got 1 point", use_aliases=True))
                        if call.from_user.username in winners:
                                scr = scoreboard.get(call.from_user.username)
                                scr += 1
                                dict = {call.from_user.username: scr}
                                scoreboard.update(dict)
                        else:
                                winners.append(call.from_user.username)
                                dict = {call.from_user.username: 0}
                                scoreboard.update(dict)
                        print(call.from_user.username)
                        answers += 1
                        correct += 1
                        trivia_game(call.message)
                else:
                        # user failed
                        bot.send_message(chat_id, emoji.emojize(f":turtle: Sorry {call.from_user.username}, but your answer is wrong. Better next time", use_aliases=True))
                        print(call.from_user.username)
                        answers += 1
                        incorrect += 1

        if call.data == "C" and condition == True:
                if pick[2] in answer:
                        # user got the right answer
                        bot.send_message(chat_id, emoji.emojize(f":trophy: Congratulations {call.from_user.username}, your answer is correct!!! You got 1 point", use_aliases=True))
                        if call.from_user.username in winners:
                                scr = scoreboard.get(call.from_user.username)
                                scr += 1
                                dict = {call.from_user.username: scr}
                                scoreboard.update(dict)
                        else:
                                winners.append(call.from_user.username)
                                dict = {call.from_user.username: 0}
                                scoreboard.update(dict)
                        print(call.from_user.username)
                        answers += 1
                        correct += 1
                        trivia_game(call.message)
                else:
                        # user failed
                        bot.send_message(chat_id, emoji.emojize(f":turtle: Sorry {call.from_user.username}, but your answer is wrong. Better next time", use_aliases=True))
                        print(call.from_user.username)
                        answers += 1
                        incorrect += 1

        if call.data == "D" and condition == True:
                if pick[3] in answer:
                        # user got the right answer
                        bot.send_message(chat_id, emoji.emojize(f":trophy: Congratulations {call.from_user.username}, your answer is correct!!! You got 1 point",  use_aliases=True))
                        if call.from_user.username in winners:
                                scr = scoreboard.get(call.from_user.username)
                                scr += 1
                                dict = {call.from_user.username: scr}
                                scoreboard.update(dict)
                        else:
                                winners.append(call.from_user.username)
                                dict = {call.from_user.username: 0}
                                scoreboard.update(dict)
                        print(call.from_user.username)
                        answers += 1
                        correct += 1
                        trivia_game(call.message)
                else:
                        # user failed
                        bot.send_message(chat_id, emoji.emojize(f":turtle: Sorry {call.from_user.username}, but your answer is wrong. Better next time", use_aliases=True))
                        print(call.from_user.username)
                        answers += 1
                        incorrect += 1


        return winners, answers, correct, incorrect, scoreboard

@bot.message_handler(commands=['menu'])
def trivia_menu(message):
        """Menu Options"""

        if message.chat.id == chat_id:
                keyboard = types.InlineKeyboardMarkup(row_width=2)
                a = types.InlineKeyboardButton(text="START GAME", callback_data="start")
                b = types.InlineKeyboardButton(text="STOP GAME", callback_data="stop")
                c = types.InlineKeyboardButton(text="PAUSE GAME", callback_data="pause")
                d = types.InlineKeyboardButton(text="SCOREBOARD", callback_data="stats")
                keyboard.add(a, b, c, d)
                bot.send_message(chat_id, "LETS PLAY A TRIVIA GAME", reply_markup=keyboard)

def trivia_game(message):
        """Question Keyboard Options"""

        trivia_file()
        keyboard = types.InlineKeyboardMarkup(row_width=1)        
        a = types.InlineKeyboardButton(text=f"A. {pick[0]}", callback_data="A")
        b = types.InlineKeyboardButton(text=f"B. {pick[1]}", callback_data="B")
        c = types.InlineKeyboardButton(text=f"C. {pick[2]}", callback_data="C")
        d = types.InlineKeyboardButton(text=f"D. {pick[3]}", callback_data="D")
        keyboard.add(a, b, c, d)

        bot.send_message(
                chat_id,
                emoji.emojize(f"""
                :man: AFRICA asks:
{question.upper()} means......
                """,
                use_aliases=True),
                reply_markup=keyboard)
                   
def stop_trivia(message):
        """Stoping the Trivia Game"""

        print(answers)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        a = types.InlineKeyboardButton(text="Click here to see your position on the scoreboard!", callback_data="rank")
        b = types.InlineKeyboardButton(text="Click here continue! (Only Admins)", callback_data="continue")
        keyboard.add(a, b)
        bot.send_message(chat_id, emoji.emojize("GAME OVER :fist:", use_aliases=True), reply_markup=keyboard)

def pause_trivia(message):
        """Stoping the Trivia Game"""

        print(answers)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        a = types.InlineKeyboardButton(text="Click here continue! (Only Admins)", callback_data="continue")
        keyboard.add(a)
        bot.send_message(chat_id, emoji.emojize("GAME PAUSED :raised_hand:"), reply_markup=keyboard) 

def trivia_scoreboard(message):
        """Trivia Game Scoreboard"""


        global scoreboard
        global scoreboard_x

        scoreboard_x = sorted(scoreboard.items(), key=operator.itemgetter(1), reverse=True)
        bot.send_message(chat_id, emoji.emojize(f":smiley: TOP 10 SCOREBOARD :trophy:", use_aliases=True))
        num = 0
        position = 1
        for each in scoreboard_x:
                if num <= 4:
                        # Top 3 winners
                        bot.send_message(chat_id, emoji.emojize(f"{position}.  {each[0]} earned {each[1]} points :star:", use_aliases=True))
                        num += 1
                        position += 1
                else:
                        bot.send_message(chat_id, f"{position}.  {each[0]} earned {each[1]} points")
                        num += 1
                        position += 1
        bot.send_message(
                chat_id,
                emoji.emojize(f"""
                And in total,
{correct} correct answers
{incorrect} incorrect answers
{answers} total answers sent
                """,
                use_aliases=True)
                )

def user_rank(message):
        """Checking position of user on scoreboard"""

        scoreboard_x = sorted(scoreboard.items(), key=operator.itemgetter(1), reverse=True)
        user = message.from_user.username
        points = scoreboard.get(user)
        position = scoreboard_x.index((user, points))
        if user in scoreboard.keys():
                position += 1
                bot.send_message(chat_id, emoji.emojize(f"Good news {user}!! You have {points} points and ranked at number {position} on the scoreboard :thumbsup:", use_aliases=True))
        else:
                bot.send_message(chat_id, f"Bad News {user}!! You are not on the scoreboard!")
        
print("Arabic Listening......")

bot.polling()

