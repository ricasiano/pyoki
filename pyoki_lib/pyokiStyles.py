import os

class colors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'

class Header:
  def title(self):
    textart = """
 _______                       __        __       
/       \                     /  |      /  |      
$$$$$$$  | __    __   ______  $$ |   __ $$/       
$$ |__$$ |/  |  /  | /      \ $$ |  /  |/  |      
$$    $$/ $$ |  $$ |/$$$$$$  |$$ |_/$$/ $$ |      
$$$$$$$/  $$ |  $$ |$$ |  $$ |$$   $$<  $$ |      
$$ |      $$ \__$$ |$$ \__$$ |$$$$$$  \ $$ |      
$$ |      $$    $$ |$$    $$/ $$ | $$  |$$ |      
$$/        $$$$$$$ | $$$$$$/  $$/   $$/ $$/       
          /  \__$$ |                              
          $$    $$/  Just another karaoke                             
           $$$$$$/   

"""
    os.system('clear')
    print(colors.HEADER + textart + colors.ENDC)
    print("ver 0.1");

