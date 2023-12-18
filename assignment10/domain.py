# CISC 120-91
# assignment10/domain.py
# Andrei Suslov
# to test this file, run `python domain.py www.example.edu`

"""
This Python script is designed to extract the domain type from a given website URL. It can be executed from the command line by running `python domain.py www.example.edu`.
Function `get_domain_type(url)`:
   - Extracts the domain type from the provided URL.
   - Removes the protocol part (http, https) if present.
   - Removes any path, query, or fragment parts.
   - Returns the domain type as a string.
Function `main()`:
   - Checks if a URL is provided as a command-line argument.
   - If no URL is provided, it displays a message indicating that no URL was provided.
   - If a URL is provided, it calls the `get_domain_type(url)` function and prints the extracted domain type.
To test the file, run it from the command line with a URL as an argument, like this: `python domain.py www.example.edu`.
"""

import sys
import stdio

def get_domain_type(url):
    """
    Extracts the domain type from a given website URL.
    :param url: A string containing the URL
    :return: The domain type as a string
    """
    # Remove the protocol (http, https) part if present
    if '://' in url:
        url = url.split('://')[1]

    # Remove any path, query, or fragment parts
    url = url.split('/')[0]

    # Split the host name and get the last part
    parts = url.split('.')
    domain_type = parts[-1] if parts else ''

    return domain_type

def main():
    if len(sys.argv) < 2:
        stdio.writeln("No URL provided")
        return

    url = sys.argv[1]
    domain_type = get_domain_type(url)
    stdio.writeln(domain_type)

if __name__ == "__main__":
    main()
