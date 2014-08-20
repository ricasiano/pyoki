import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def title():
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
  print(bcolors.HEADER + textart + bcolors.ENDC)
  print("ver 0.1");
