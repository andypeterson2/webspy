import yagmail
from bs4 import BeautifulSoup
import requests
import os
import sys
import signal
import re
import logging
import argparse
import multiprocessing
from .helpers import check_href_title, send_email_with_yagmail

def main():
    # Create an argument parser object and add a positional argument for the configuration files
    parser = argparse.ArgumentParser(description="A daemon that checks multiple websites for links with partial title matches and sends email notifications")
    parser.add_argument("config_files", type=str, nargs="+", help="The paths to the configuration files")

    # Parse the arguments and get a namespace object
    args = parser.parse_args()

    # Create a queue to store the results of the check_and_send function
    queue = multiprocessing.Queue()

    # Loop through the values of the configuration files argument and create a process that runs the check_and_send function for each configuration file and passes the queue as an argument
    for config_file in args.config_files:
        # Load the configuration file
        with open(config_file) as f:
            config = json.load(f)

        # Create a process that runs the check_and_send function for the configuration and passes the queue as an argument
        process = multiprocessing.Process(target=check_and_send, args=(config, queue))

        # Start the process
        process.start()

    # Get all the active processes
    processes = multiprocessing.active_children()

    # Loop through the processes except the main process
    for process in processes:
        # Wait for the process to finish
        process.join()

    # Get all the results from the queue
    results = []
    while not queue.empty():
        result = queue.get()
        results.append(result)

    # Log the results
    logger.info("The results are: {}".format(results))

    # Exit the application gracefully
    sys.exit(0)