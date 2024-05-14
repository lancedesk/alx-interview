#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics:
"""

import sys


def compute_metrics():
    """
    Reads stdin line by line and computes metrics.
    """
    status_counts = {
                     200: 0,
                     301: 0,
                     400: 0,
                     401: 0,
                     403: 0,
                     404: 0,
                     405: 0,
                     500: 0
                    }

    total_file_size = 0
    line_count = 0

    def parse_log_line(log_line):
        """
        Parses a line of the log with the format:
        <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
        <status code> <file size>
        If the line does not match this format, returns None.
        """
        if len(log_line.split()) < 2:
            return None
        file_size = 0
        status_code = None

        try:
            file_size = int(log_line.split()[-1])
            status_code = int(log_line.split()[-2])

            if status_code not in status_counts:
                status_code = None
        finally:
            return {
                "status_code": status_code,
                "file_size": file_size,
            }

    def print_statistics():
        """
        Prints the computed statistics.
        """
        print("Total file size: {}".format(total_file_size))
        for code, count in sorted(status_counts.items()):
            if count > 0:
                print("{}: {}".format(code, count))

    try:
        for log_line in sys.stdin:
            if line_count == 10:
                print_statistics()
                line_count = 0

            parsed_data = parse_log_line(log_line)
            if parsed_data is not None:
                if parsed_data["status_code"] is not None:
                    status_counts[parsed_data["status_code"]] += 1
                total_file_size += parsed_data["file_size"]
                line_count += 1

    except KeyboardInterrupt:
        print_statistics()
        raise

    print_statistics()


if __name__ == "__main__":
    compute_metrics()
