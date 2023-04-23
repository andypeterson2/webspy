# WebSpy

WebSpy is a python script that searches websites for links with partial title matches and alerts you by email. You can use WebSpy to find relevant information, explore new possibilities, or satisfy your curiosity.

## Requirements

- Python 3
- BeautifulSoup
- Requests
- Yagmail
- OAuth2 credentials for Gmail

## Installation

To install WebSpy, you need to clone this repository and install the required dependencies. You can do this by running the following commands:

```bash
git clone https://github.com/your_username/WebSpy.git
cd WebSpy
pip install -r requirements.txt
```

You also need to create a file called credentials.json in the same directory as the script, and fill it with your Gmail username and OAuth2 token. You can follow this guide to obtain an OAuth2 token for Gmail: https://yagmail.readthedocs.io/en/latest/oauth2.html

The credentials.json file should look like this:

```json
{
    "user": "your_username@gmail.com",
    "token": "your_oauth2_token"
}
```

## Usage

To use WebSpy, you need to create one or more configuration files in JSON format that specify the options and parameters for each website you want to check. The configuration file should contain the following keys:

- url: The URL of the website to check.
- terms: The list of search terms to match.
- case_sensitive: A boolean flag to indicate whether the matching should be case sensitive or not. Default is false.
- subject: The subject of the email notification.
- recipient: The recipient of the email notification.

Here is an example of a configuration file:

```json
{
    "url": "https://www.python.org/",
    "terms": ["programming", "language", "python"],
    "case_sensitive": false,
    "subject": "Found href with partial title match",
    "recipient": "recipient_username@gmail.com"
}
```

You can pass one or more configuration files as command line arguments to the script, for example:

```bash
./mydaemon.py config1.json config2.json config3.json
```

The script will create a separate process for each configuration file and check the corresponding website for a link with a partial title match. If a matching link is found, it will send an email notification using Yagmail and OAuth2 credentials. The script will also log the results to a file named mydaemon.log and to the console.

To stop the script, you can use Ctrl-C or send a SIGTERM signal to the main process.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

You're welcome. I can try to generate a GitHub issue report format to add to your readme file. Here is a possible format:

## How to report an issue

If you encounter a bug or have a feature request for WebSpy, please open an issue on GitHub using the following template:

### Issue title

A concise and descriptive title that summarizes the issue.

### Issue description

A clear and detailed explanation of what the problem or feature request is. Include any relevant information such as steps to reproduce, expected behavior, actual behavior, screenshots, logs, etc.

### Environment

A description of the environment where the issue occurs, such as the operating system, Python version, dependencies versions, etc.

### Additional context

Any other information that may be helpful to understand or resolve the issue.

Here is an example of an issue report:

### Issue title

WebSpy fails to send email notification when matching link is found

### Issue description

I ran WebSpy with a configuration file that checks https://www.python.org/ for links with the term "python". The script found a matching link but did not send an email notification to the recipient. Instead, it raised an SMTPAuthenticationError and logged the following message:

```bash
ERROR:root:Failed to send email notification: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbs\n5.7.14 0Q8LwBkxZjYf0z9tZl8tXG9pZy3J6yHn6wFm8RvLs2bQ2jKoqWd3q1vYX4a0a7VxOQc2rP\n5.7.14 9fFzWfJm4iXlUcCgMk4e1wKjyM0nYHh6bN4OuOZQYV9DxqJL0i3oT3uqUjgEzRf6lGpH0P\n5.7.14 2sJnBmTbWgIy1d8aUeCpGkMnU6oXw> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 f10sm10142343wmg.13 - gsmtp')
```

I expected the script to send an email notification with the subject "Found href with partial title match" and the body containing the URL of the matching link.

### Environment

- Operating system: Windows 10
- Python version: 3.9.1
- BeautifulSoup version: 4.9.3
- Requests version: 2.25.1
- Yagmail version: 0.14.245
- OAuth2 credentials for Gmail: valid and working

### Additional context

I checked my Gmail settings and enabled less secure app access, but the issue still persists.
