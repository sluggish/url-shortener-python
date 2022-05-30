import string
import requests
import colorama
import argparse

from colorama import Fore, Style
from argparse import ArgumentParser

def banner() -> None:
    print(f"""{Fore.RED + Style.BRIGHT}
  _    _ _____  _         _____ _    _  ____  _____ _______ ______ _   _ ______ _____  
 | |  | |  __ \| |       / ____| |  | |/ __ \|  __ \__   __|  ____| \ | |  ____|  __ \ 
 | |  | | |__) | |      | (___ | |__| | |  | | |__) | | |  | |__  |  \| | |__  | |__) |
 | |  | |  _  /| |       \___ \|  __  | |  | |  _  /  | |  |  __| | . ` |  __| |  _  / 
 | |__| | | \ \| |____   ____) | |  | | |__| | | \ \  | |  | |____| |\  | |____| | \ \ 
  \____/|_|  \_\______| |_____/|_|  |_|\____/|_|  \_\ |_|  |______|_| \_|______|_|  \_\ 
                               {Fore.RED + Style.BRIGHT}--> {Fore.WHITE}github.com/sluggish {Fore.RED + Style.BRIGHT}<-- 
                                
    {Fore.RESET}""")

def shorten():
    parser = ArgumentParser()
    parser.add_argument("url", help="url to shorten")
    args = parser.parse_args()    

    shorten_url = requests.get("https://is.gd/create.php?format=simple&url=" + args.url)
    print(f"Shortened {Fore.RED + Style.BRIGHT}URL{Fore.RESET}: {shorten_url.text}")

def main():
    banner()
    shorten()

main()