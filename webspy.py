#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WebSpy: A python script that checks websites for links with partial title matches and sends email notifications.
"""

import argparse
import logging
import multiprocessing
import queue
import sys

from webspy import check_and_send, parse_config

def main():
    """Main function of WebSpy."""
    # Create an argument parser
    parser = argparse.ArgumentParser(description="WebSpy: A python script that checks websites for links with partial title matches and sends email notifications.")
    parser.add_argument("-c", "--config", required=True, help="Path to the configuration file or directory.")
    args = parser.parse_args()

    # Parse the configuration files
    configs = parse_config(args.config)

    # Create a queue to store the results
    result_queue = multiprocessing.Queue()

    # Create a list to store the processes
    processes = []

    # For each configuration, create a process and run the check_and_send function
    for config in configs:
        process = multiprocessing.Process(target=check_and_send, args=(config, result_queue))
        process.start()
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # Get the results from the queue
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    # Log the results
    logging.basicConfig(filename="webspy.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    logging.info("WebSpy results:")
    for result in results:
        logging.info(result)

    # Print the results to the console
    print("WebSpy results:")
    for result in results:
        print(result)

    # Exit gracefully
    sys.exit(0)

if __name__ == "__main__":
    main()