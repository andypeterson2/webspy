
import yagmail
from bs4 import BeautifulSoup
import requests

def check_href_title(url, terms, case_sensitive=False):
    """Check if a website has a link with a title that partially matches any of the given search terms.

    :param url: The URL of the website to check.
    :type url: str
    :param terms: The list of search terms to match.
    :type terms: list of str
    :param case_sensitive: A flag to indicate whether the matching should be case sensitive or not. Default is False.
    :type case_sensitive: bool
    :return: The href attribute of the matching link if found, None otherwise.
    :rtype: str or None
    """
    
    # Join the search terms with | to form an OR pattern
    pattern = "|".join(terms)

    # If case sensitivity is not required, add the ignore case flag to the pattern
    if not case_sensitive:
        pattern = "(?i)" + pattern

    # Get the HTML content of the website
    website = requests.get(url)

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(website.content, "html.parser")

    # Find all the links in the website
    links = soup.find_all("a")

    # Loop through the links and check if any of them has a title that matches the pattern
    for link in links:
        title = link.get("title")
        href = link.get("href")
        if title and href:
            if re.search(pattern, title):
                # If a matching link is found, return its href attribute
                return href

    # If no matching link is found, return None
    return None

def send_email_with_yagmail(subject, contents):
    # Initialize the server connection with OAuth credentials
    oauth_file = os.path.join(os.path.expanduser("~"), "oauth2_creds.json")
    yag = yagmail.SMTP(user="my_username@gmail.com", oauth2_file=oauth_file)

    # Send the email
    yag.send(to=recipient, subject=subject, contents=contents)
