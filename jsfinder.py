import requests
from bs4 import BeautifulSoup
import argparse
from colorama import Fore, Style
import datetime

def extract_js_links(url):
    """Extracts JavaScript links from an HTML page.

    Args:
        url: The URL of the HTML page.

    Returns:
        A list of JavaScript file URLs.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    js_links = []
    for script in soup.find_all('script'):
        src = script.get('src')
        if src:
            js_links.append(src)

    return js_links

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract JavaScript links from an HTML page", add_help=False)

    parser.add_argument("url", help="The URL of the HTML page")
    args = parser.parse_args()

    js_links = extract_js_links(args.url)
    num_js_files = len(js_links)

    print(f"{Fore.RED}##############Ｍａｄｅ ｂｙ Ｂａｂａ０１ｈａｃｋｅｒ############{Style.RESET_ALL}")
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\nJS files found: {num_js_files}")
    for link in js_links:
        print(Fore.GREEN + f"-> {link}" + Style.RESET_ALL)

