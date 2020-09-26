#!/usr/bin/env python3

from colorama import Fore, Back, Style

class ColorStr(str):
    
    def __init__(self, string):
        """
        String that support coloration. It also heredate all the funcionalities of str. 

        Args:
            string (str): String
        """        
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

    # Fore(colorama) Functions to permit anidation of syles
        
    def Fore_BLACK(self):
        return ColorStr(f"{Fore.BLACK} {self.str} {Fore.RESET}")
    
    def Fore_RED(self):
        return ColorStr(f"{Fore.RED} {self.str} {Fore.RESET}")

    def Fore_GREEN(self):
        return ColorStr(f"{Fore.GREEN} {self.str} {Fore.RESET}")

    def Fore_YELLOW(self):
        return ColorStr(f"{Fore.YELLOW} {self.str} {Fore.RESET}")

    def Fore_MAGENTA(self):
        return ColorStr(f"{Fore.MAGENTA} {self.str} {Fore.RESET}")

    def Fore_CYAN(self):
        return ColorStr(f"{Fore.CYAN} {self.str} {Fore.RESET}")

    def Fore_WHITE(self):
        return ColorStr(f"{Fore.WHITE} {self.str} {Fore.RESET}")
    
    # Black(colorama) Functions to permit anidation of syles
        
    def Back_BLACK(self):
        return ColorStr(f"{Back.BLACK} {self.str} {Back.RESET}")
    
    def Back_RED(self):
        return ColorStr(f"{Back.RED} {self.str} {Back.RESET}")
    
    def Back_GREEN(self):
        return ColorStr(f"{Back.GREEN} {self.str} {Back.RESET}")
    
    def Back_YELLOW(self):
        return ColorStr(f"{Back.YELLOW} {self.str} {Back.RESET}")
    
    def Back_MAGENTA(self):
        return ColorStr(f"{Back.MAGENTA} {self.str} {Back.RESET}")
    
    def Back_CYAN(self):
        return ColorStr(f"{Back.CYAN} {self.str} {Back.RESET}")
    
    def Back_WHITE(self):
        return ColorStr(f"{Back.WHITE} {self.str} {Back.RESET}")

    # Style(colorama) Functions to permit anidation of syles


    def Style_DIM(self):
        return ColorStr(f"{Style.DIM} {self.str} {Style.RESET_ALL}")

    def Style_NORMAL(self):
        return ColorStr(f"{Style.NORMAL} {self.str} {Style.RESET_ALL}")

    def Style_BRIGHT(self):
        return ColorStr(f"{Style.BRIGHT} {self.str} {Style.RESET_ALL}")

    
    def __repr__(self):
        return ColorStr(self.str)
