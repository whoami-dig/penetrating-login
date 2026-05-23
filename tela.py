from colorama import Fore, init

def options():
    option_list=['START TEST', 'MORE ABOUTE THE TOOL', 'EXIT']
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