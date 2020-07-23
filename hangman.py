import random
import os

class hangman():
   
   def __init__(self):

      self.wordlib = [i.replace('\n', '') for i in open('words.txt','r').readlines()]
      self.word=random.choice(self.wordlib)
      self.word_to_show=self.word

      self.word_guessed = []
      self.letter_guessed = []

      self.chance = 7
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

      while True:

          self.clear()

          print('     \nCHANCE LEFT: ', self.chance)

          if self.chance <= 0 and '_' in self.word_guessed:
              
              print('\n\nYOU LOSE')
              print('THE WORD IS ', self.word_to_show)
              break
              
          if '_' not in self.word_guessed and self.chance >= 0:

              print('\n\nYOU WIN!')
              break

          self.inputword=str(input('\npls guess a letter:'))

          if len(self.inputword)==1:
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
      os.system('pause')

if __name__ == '__main__':

      hangman = hangman()
      hangman.start_game()
