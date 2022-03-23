import menus
import subapp as app

BYEMSM ='''

 ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄        ▄▄▄▄▄▄▄▄▄▄  ▄         ▄ ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░▌      ▐░░░░░░░░░░▌▐░▌       ▐░▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀▐░█▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀█░▐░▌       ▐░▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌         ▐░▌       ▐░▐░▌       ▐░▐░▌       ▐░▌     ▐░▌       ▐░▐░▌       ▐░▐░▌          
▐░▌ ▄▄▄▄▄▄▄▄▐░▌       ▐░▐░▌       ▐░▐░▌       ▐░▌     ▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌▐░░░░░░░░▐░▌       ▐░▐░▌       ▐░▐░▌       ▐░▌     ▐░░░░░░░░░░▌▐░░░░░░░░░░░▐░░░░░░░░░░░▌
▐░▌ ▀▀▀▀▀▀█░▐░▌       ▐░▐░▌       ▐░▐░▌       ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▐░▌       ▐░▐░▌       ▐░▐░▌       ▐░▌     ▐░▌       ▐░▌    ▐░▌    ▐░▌          
▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄█░▌    ▐░▌    ▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░▌      ▐░░░░░░░░░░▌     ▐░▌    ▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀        ▀▀▀▀▀▀▀▀▀▀       ▀      ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                           

'''

LOGO='''

 _                 _                                              _      
| | __ _ _ __   __| |  ___ _   _ _ ____   _____ _   _    ___ __ _| | ___ 
| |/ _` | '_ \ / _` | / __| | | | '__\ \ / / _ | | | |  / __/ _` | |/ __|
| | (_| | | | | (_| | \__ | |_| | |   \ V |  __| |_| | | (_| (_| | | (__ 
|_|\__,_|_| |_|\__,_| |___/\__,_|_|    \_/ \___|\__, |  \___\__,_|_|\___|
                                                |___/                    
                                      
'''

def main():
    Title = LOGO
    options = ["1. Calculte Coordinates", 
               "2. Calculate Whole Circle Bearing",
               "3. Calculate Bearing",
               "4. Convert decimals angles to DDMMSS and Viceversa",
               "Exit"]

    option = len(options)
    
    while option != len(options)-1 and option != None:
        option = menus.list_menu(Title, options)
        # Application 1 Calculate Coordinates is ok
        if option == 0:
            app.simplecalculatecoordinates()
        elif option == 1:
            app.simplecalculatewcb()
        elif option == 2:
            app.simplecalculaterb()
        elif option == 3:
            app.simpleangleconvertion()
        elif option == len(options)-1:
            print(BYEMSM)

    return

if __name__ == "__main__":
    main()
