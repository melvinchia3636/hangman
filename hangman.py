import random
import os

win_times = 0
lost_times = 0

class hangman():

   global win_times, lost_times
   
   def __init__(self):

      global win_times, lost_times

      self.wordlib = [i.replace('\n', '') for i in open('words.txt','r').readlines()]
      self.word=random.choice(self.wordlib).lower()
      self.word_to_show=self.word

      self.word_guessed = []
      self.letter_guessed = []

      self.chance = 10
      self.word_toguess = self.split(self.word)

      for i in range(len(self.word)):
          self.word_guessed.append('_')

      self.printout()

   def clear(self):
      if os.name == 'posix':
          _ = os.system('clear')
      else:
         _ = os.system('cls')

   def split(self, word_toguess):
         return [char for char in word_toguess]

   def printout(self):
         [print(word, end='') for word in self.word_guessed]

   def start_game(self):

      global win_times, lost_times

      while True:

          self.clear()

          print('     \nCHANCE LEFT: ', self.chance)
          print('YOU WON: ', win_times, ' times')
          print('YOU LOSE: ', lost_times, ' times')

          if self.chance <= 0 and '_' in self.word_guessed:
              
              print('\n\nYOU LOSE')
              print('THE WORD IS ', self.word_to_show)
              lost_times +=  1
              os.system('pause')
              return
              
          if '_' not in self.word_guessed and self.chance >= 0:

              print('\n\nYOU WIN!')
              win_times += 1
              os.system('pause')
              return

          self.inputword=str(input('\npls guess a letter:'))

          if len(self.inputword)==1 and self.inputword != ' ':
              if self.inputword not in self.letter_guessed:
                  if self.inputword in self.word_toguess:
                      self.temp = [index for index, value in enumerate(self.word_toguess) if value==self.inputword]
                      for x in self.temp:
                          self.word_guessed[x]=self.inputword
                      self.letter_guessed.append(self.inputword)
                  else:
                      self.chance-=1
                      self.letter_guessed.append(self.inputword)

          self.printout()

if __name__ == '__main__':

      while True:
         game = hangman()
         game.start_game()

#quit()
