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

## Contact

If you have any questions or feedback, feel free to contact me at your_email@gmail.com.

Source: Conversation with Bing, 4/22/2023(1) How to create a Readme.md file? | Medium. https://bing.com/search?q=how+to+write+a+good+readme+for+python Accessed 4/22/2023.
(2) How to Write a Good README File for Your GitHub Project - FreeCodecamp. https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/ Accessed 4/22/2023.
(3) Writing good README files — Code documentation documentation. https://coderefinery.github.io/documentation/writing-readme-files/ Accessed 4/22/2023.
(4) How to create a Readme.md file? | Medium. https://medium.com/@danielmihai0220/creating-a-readme-md-file-88e0f3791d3d Accessed 4/22/2023.
(5) Make a README & Documentation with Jupyter Notebooks. https://jackmckew.dev/make-a-readme-documentation-with-jupyter-notebooks.html Accessed 4/22/2023.
(6) Making a PyPI-friendly README — Python Packaging User Guide. https://packaging.python.org/guides/making-a-pypi-friendly-readme/ Accessed 4/22/2023.
