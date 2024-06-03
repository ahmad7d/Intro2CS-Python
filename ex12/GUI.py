from tkinter import *
import tkinter as tk
from ex12_utils import *
import tkinter.messagebox
from math import floor
from PIL import ImageTk, Image
from random import choice
from UTILS import *
import pygame

pygame.mixer.init()


class Menu:
    """
    this class has GUI that run the menu page
    """
    def __init__(self):
        self.flag = False
        self.menu = tk.Tk()
        self.menu.title(GAME_TITLE)
        self.menu_design()

    def menu_design(self):
        """
        creating and design the menu page
        """
        self.image = tk.PhotoImage(file='boggle_bg1.png')
        self.canvas = tk.Canvas(self.menu, width=1280, height=720)
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
        self.canvas.pack()
        self.start_btn_img = ImageTk.PhotoImage(Image.open('strt_btn.png'))
        self.quite_btn_img = ImageTk.PhotoImage(Image.open('ext_btn.png'))
        self.start_btn = Button(self.menu, image=self.start_btn_img, command=self.start_game, borderwidth=10, bg=BLACK)
        self.quite_btn = Button(self.menu, image=self.quite_btn_img, command=self.end_game, borderwidth=10, bg=BLACK)
        self.start_btn.place(x=475, y=500)
        self.quite_btn.place(x=20, y=20)
        self.menu.mainloop()

    def start_game(self):
        """
        this function return a flag to run the boggle game by clicking the start game button
        """
        self.flag = True
        self.menu.destroy()

    def run_game(self):
        """
        change the flag to run the game
        :return: True flag
        """
        return self.flag

    def end_game(self):
        """
        this function close the menu page
        """
        self.menu.destroy()


class Boggle:
    """
    class to create the boggle game
    """

    def __init__(self, board, words):
        self.flag = False
        self.words = words
        self.board = board
        self.time = 180
        self.time_flag = True
        self.score = ZERO
        self.boggle = tk.Tk()
        self.boggle.title(GAME_TITLE)
        self.letters = [board[i][j] for j in range(len(board[0])) for i in range(len(board))]
        self.cords = []
        self.guessed_words = []
        self.hint_words = []
        self.design()
        self.build_board()
        self.timer()
        self.submit()
        self.set_timer()
        self.add_score()
        self.create_guessed_words_label()
        self.current_word()
        # self.create_hint()
        # self.search_hint()

    def design(self):
        """
        this function import the background picture and create the page of the game
        """
        self.image = tk.PhotoImage(file='bog-bg.png')
        self.canvas = tk.Canvas(self.boggle, width=1280, height=720)
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
        self.canvas.pack()
        self.exit_btn = Button(self.boggle, text='End game', width=9, height=2, fg=WHITE,
                               bg=BLACK, command=self.end_game, cursor=EXIT_CURSOR)
        self.exit_btn.place(x=10, y=10)

    def build_board(self):
        """
        this function builds the buttons board
        """
        print(self.letters)
        self.board_frame = Frame(self.boggle, width=500, height=500)
        self.board_frame.place(x=460, y=150)
        row = 0
        col = 0
        for i in range(0, 16):
            if i % 4 == 0:
                col += 1
                row = 0
            self.letter_btn = Button(self.board_frame, font=FONT, text=self.letters[i], width=3, height=2,
                                     command=self.add_cor(row, col - 1, self.letters[i]), bg=BLACK, fg=WHITE,
                                     cursor=PENCIL_CURSOR)
            self.letter_btn.grid(row=row, column=col)
            row += 1

    def submit(self):
        """
        this function builds submit button
        """
        self.submit_btn = Button(self.boggle, text=SUBMIT_TXT, font=('@MS Gothic', 30), fg=WHITE, bg=BLACK, width=6,
                                 height=1, command=self.is_valid_path, cursor=SUBMIT_CURSOR)
        self.submit_btn.place(x=550, y=630)

    def timer(self):
        """
        this function create a time label
        """
        self.time_label1 = Label(self.boggle, text=TIME_TXT, font=('@MS Gothic', 20), fg=WHITE, bg=BLACK,
                                 cursor=WRONG_CURSOR)
        self.time_label1.place(x=30, y=280)

    def add_cor(self, i, j, letter):
        def put():
            """
            this function update the current word label while clicking the letters button , and show an error for any
            illegal path.
            """
            self.cords.append((i, j))
            if not legal_path(self.cords):
                tk.messagebox.showwarning('error', WRONG_PATH_MSG)
                self.cords.clear()
                self.cur_word_row_label.configure(text='')
            else:
                self.word = ''
                self.word += self.cur_word_row_label.cget("text") + letter
                self.cur_word_row_label.configure(text=self.word)

        return put

    def is_valid_path(self):
        """
        this function checks if the word is legal then add it to the guessed words list + increase the score and
        play sound if the word is right + showing error if it's not right.
        """
        self.cur_word_row_label.configure(text='')
        word = get_word(self.cords, self.board)
        if word not in self.guessed_words:
            if is_valid_word(word, self.words):
                pygame.mixer.music.load('correct_word.mp3')
                pygame.mixer.music.play(loops=0)
                self.guessed_words.append(word)
                self.score += self.calculate_score(word)
                self.score_label2.configure(text=str(int(self.score)))
                self.guessed_words_label.insert(END, word)
            else:
                tk.messagebox.showwarning('error', 'wrong word')
        else:
            tk.messagebox.showwarning('error', CHOSEN_WORD_MSG)
        self.cords.clear()

    def current_word(self):
        """
        this function create a label to combine the letters that's the user clicked .
        """
        self.cur_word_label = Label(self.boggle, text='current word', font=('@MS Gothic', 20),
                                    fg=WHITE, bg=BLACK, cursor=WRONG_CURSOR)
        self.cur_word_label.place(x=530, y=40)
        self.cur_word_row_label = Label(self.boggle, fg=WHITE, bg=BLACK, width=35, height=2, cursor=WRONG_CURSOR)
        self.cur_word_row_label.place(x=500, y=80)

    def create_guessed_words_label(self):
        """
        this function to do  a list of our words that we guessed it
        """

        self.guessed_words_label = Listbox(self.boggle, font=("Courier", 15), fg=WHITE, bg=BLACK, width=10,
                                           height=15, cursor=LST_WORDS_CURSOR, borderwidth=10)
        self.guessed_words_label_txt = Label(self.boggle, font=("@MS Gothic", 20),
                                             text="your words", fg=WHITE, cursor=WRONG_CURSOR, bg=BLACK)
        self.guessed_words_label_txt.place(x=1080, y=130)
        self.guessed_words_label.place(x=1082, y=170)

    def set_timer(self):
        """
        this function run the time til 0 by the after + ask the user if he wants to play another round.
        """

        if self.time <= 0:
            self.stop_timer_sound()
            end_msg = tk.messagebox.askyesno('Time finished', 'nice ! , your score is ' + str(int(self.score)) + '\n' +
                                             ' do you wanna play another round ?')
            if end_msg:
                self.restart_game()
            else:
                self.boggle.destroy()
                return

        self.play_timer_sound()
        self.time -= 1

        self.time_str = ''
        if self.time % 60 < 10:
            self.time_str += '0' + str(floor(self.time / 60)) + ':' + '0' + str(self.time % 60)
        else:
            self.time_str += '0' + str(floor(self.time / 60)) + ':' + str(self.time % 60)
        self.time_label2 = Label(self.boggle, text=str(self.time_str), font=('@MS Gothic', 20),
                                 fg=WHITE, bg=BLACK, cursor=WRONG_CURSOR)
        self.time_label2.place(x=25, y=320)
        self.boggle.after(1000, self.set_timer)
        if self.time < 30 and self.time % 2 == 0:
            self.time_warring()

    def time_warring(self):
        """
        this function make a time with red color to warring the player
        """

        self.time_label2.configure(fg='red')

    def add_score(self):
        """
        this function builds frame have labels that updated when the player guesses correct word
        """
        self.score_label1 = Label(self.boggle, text=SCORE_txt, font=('@MS Gothic', 25),
                                  fg=WHITE, bg=BLACK, cursor=WRONG_CURSOR)
        self.score_label1.place(x=15, y=150)
        self.score_label2 = Label(self.boggle, text=str(int(self.score)),
                                  font=('@MS Gothic', 20), fg=WHITE, bg=BLACK, cursor=WRONG_CURSOR)
        self.score_label2.place(x=45, y=200)

    def calculate_score(self, word):
        """
        this function calculate the score=len(word)^2
        """
        return math.pow(len(word), 2)

    def create_hint(self):
        """
        this function create a help button
        """
        hint_btn = Button(self.boggle, text='help !', fg=WHITE, bg=BLACK,
                          font=('@MS Gothic', 25), command=self.get_hint)
        hint_btn.place(x=1120, y=630)

    def search_hint(self):
        """
        this function search all the valid words from the board by coordinates .
        """
        all_paths = max_score_paths(self.board, self.words)
        for path in all_paths:
            new_word = ''
            new_word += get_word(path, self.board)
            self.hint_words.append(new_word)

    def get_hint(self):
        """
        this function give a help words that in the board and randomly chose a word from the list then remove it .
        """
        hint = choice(self.hint_words)
        tk.messagebox.showinfo('your hint', hint)
        self.hint_words.remove(hint)

    def play_timer_sound(self):
        """
        this function make sound ticktock clock.
        """
        pygame.mixer.music.load('Clock tick tock SOUND EFFECTS.mp3')
        pygame.mixer.music.play(loops=3)

    def stop_timer_sound(self):
        """
        this function stop the sound when the game end
        """
        pygame.mixer.music.stop()

    def restart_game(self):
        """
        this function restart the game and update the time
        """
        self.time = 181
        self.set_timer()

    def run(self):
        """
        this function run the game
        """
        self.boggle.mainloop()

    def end_game(self):
        """
        this function end the game
        """
        self.boggle.destroy()


def get_word(word_coordinates, board):
    new_word = ''
    for cor in word_coordinates:
        new_word += board[cor[0]][cor[1]]
    return new_word


def is_valid_word(word, words):
    return True if word in words else False


def is_valid_path(board, path):
    return False if False in [False for i in range(len(path) - 1) if abs(path[i + 1][0] - path[i][0]) > 1
                              or abs(path[i + 1][1] - path[i][1]) > 1] \
                    + [False for cor in path if
                       cor[0] >= len(board) or cor[1] >= len(board[0]) or cor[0] < 0 or cor[1] < 0] \
        else True


def legal_path(path):
    """
    this function checks if the word is legal
    """
    if False in [False for i in range(len(path) - ONE) if abs(path[i + ONE][ZERO] - path[i][ZERO]) > ONE
                                                          or abs(path[i + ONE][ONE] - path[i][ONE]) > ONE]:
        return False
    return True
