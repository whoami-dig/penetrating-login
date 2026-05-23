from colorama import Fore, init
import login_window as j

def options():
    option_list=['START TEST', 'ABOUT THE TOOL', 'EXIT']
    for i, item in enumerate(option_list):
        print(Fore.WHITE + f"[{i+1}]" + " - " + Fore.CYAN + f"{item}")
    print()


txt=r"""

    ██████╗ ███████╗███╗   ██╗    ██╗  ██╗
    ██╔══██╗██╔════╝████╗  ██║    ╚██╗██╔╝
    ██████╔╝█████╗  ██╔██╗ ██║     ╚███╔╝
    ██╔═══╝ ██╔══╝  ██║╚██╗██║     ██╔██╗
    ██║     ███████╗██║ ╚████║    ██╔╝ ██╗
    ╚═╝     ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝
    
"""
def screen():
    init(autoreset=False)
    r='-='*23
    print(
            Fore.WHITE + 
            r + 
            Fore.MAGENTA + 
            txt + 
            Fore.WHITE +
            r +
            Fore.YELLOW +
"\n\n              [PEN-X INITIALIZED ]\n"
)
    

def start():

    j.create_window()



def about():
    print('More...')


def exitt():
    print('Leaving...')