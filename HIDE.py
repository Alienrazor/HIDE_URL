#Alienrazor 


"""
Description:
-----------
    This Script Mask the url behind another url

Usage:
-----
    python3 maskurl.py 
    
"""
import os
import sys
import argparse
from urllib.parse import urlparse

from requests import post


banner = r"""
                 ..              .:.
              ~YJ^.              .~J5!.
            ^G@J                   .J@B!
         ?~ B@Y                      5@&:7?
        ^@5:#@J                      Y@@!P@^
        ~@@#&@&7        ....:~      ?@@@#@@^
       7:J@@@@@7     :75####B7      ?@@@@@J^7
       !#55#@@@~:    :!~P@@@!      :~@@@#55#!
        ~P&@@@@5J?^.    !@@@Y   .^JJ5@@@@&P^
         .7YPB&@BB##BPYY#@@@@YPB##GB@&BPY7.
          ?B##&@@@@@@@@@@@@@@@@@@@@@@@##G7
           :?G&@&G#@@@@@@@@@@@@@&#B&@#P7.
              :~?7~~?#@&@@@@&@B?^!?7^.
                 !!YP5~~&@@&~~PPJ!!
                .^7J^  5@@@@Y .^J7^
                      J@&&&&@?
                     !#&G##B&#!
                     G5&5##P&PG
                     Y7&Y##5#7Y
                     ..GJ##5P..
                       J?#&Y?
                       ~7#&J^
                       .~#&!.
                        .#&:
                        .B&:
                         G#.
                         GB
                         5P
                         7J
                         .   

   """                    
                         


def Shortner(big_url: str) -> str:
    """
    Function short the big urls to short
    """
    return post(f"https://is.gd/create.php?format=json&url={big_url}").json()['shorturl']


def MaskUrl(target_url: str, mask_domain: str, keyword: str) -> str:
    """
    Function mask the url with given domain and keyword
    """
    url = Shortner(target_url)
    return f"{mask_domain}-{keyword}@{urlparse(url).netloc + urlparse(url).path}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mask the URL behind the another URL")

    parser.add_argument(
        "--target",
        type=str,
        help="Target URL to Mask (With http or https)",
        required=True,
    )
    parser.add_argument(
        "--mask",
        type=str,
        help="Mask URL (With http or https)",
        required=True,
    )
    parser.add_argument(
        "--keywords",
        type=str,
        help="Keywords (Use (-) instead of whitespace)",
        required=True,
    )
    os.system ("clear")
    print(f"\033[91m {banner}\033[00m")

    if len(sys.argv) == 1:        
        print ("______________________________________________ ")
        print ( "\033[0;96mAUTHOR : ALIENRAZOR ")
        print ("\033[0;96mTOOL : CUSTOM URL MAKER \033[0;98m")
        print ("______________________________________________ ")
        print("\n")
        target = input("Enter the url (With http or https): ")
        mask = input("Enter the domain name to mask url (With http or https): ")
        keyword = input("Enter the keywords (use '-' instead of whitespace): ")
        print("\n")
    else:
        args = parser.parse_args()
        target = args.target
        mask = args.mask
        keyword = args.keywords

    print(f"\033[91m {MaskUrl(target, mask, keyword)}\033[00m")
