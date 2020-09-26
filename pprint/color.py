#!/usr/bin/env python3

from colorama import Fore, Back, Style

class ColorStr(str):
    def __init__(self, string):
        super().__init__()
        self.str = string
        # Funcionalities of Fore (colorama) 
        self.ForeBLACK = f"{Fore.BLACK} {self.str} {Fore.RESET}"
        self.ForeRED = f"{Fore.RED} {self.str} {Fore.RESET}"
        self.ForeGREEN = f"{Fore.GREEN} {self.str} {Fore.RESET}"
        self.ForeYELLOW = f"{Fore.YELLOW} {self.str} {Fore.RESET}"
        self.ForeMAGENTA = f"{Fore.MAGENTA} {self.str} {Fore.RESET}"
        self.ForeCYAN = f"{Fore.CYAN} {self.str} {Fore.RESET}"
        self.ForeWHITE = f"{Fore.WHITE} {self.str} {Fore.RESET}"

        # Funcionalities of Fore (colorama) 
        self.BackBLACK = f"{Back.BLACK} {self.str} {Back.RESET}"
        self.BackRED = f"{Back.RED} {self.str} {Back.RESET}"
        self.BackGREEN = f"{Back.GREEN} {self.str} {Back.RESET}"
        self.BackYELLOW = f"{Back.YELLOW} {self.str} {Back.RESET}"
        self.BackMAGENTA = f"{Back.MAGENTA} {self.str} {Back.RESET}"
        self.BackCYAN = f"{Back.CYAN} {self.str} {Back.RESET}"
        self.BackWHITE = f"{Back.WHITE} {self.str} {Back.RESET}"


        # Functionalities of Style (colorama)
        self.StyleDIM = f"{Style.DIM} {self.str} {Style.RESET_ALL}"
        self.StyleNORMAL = f"{Style.NORMAL} {self.str} {Style.RESET_ALL}"
        self.StyleBRIGHT = f"{Style.BRIGHT} {self.str} {Style.RESET_ALL}"

    def __repr__(self):
        return ColorStr(self.str)
        