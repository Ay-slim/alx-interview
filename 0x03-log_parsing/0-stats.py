#!/usr/bin/python3
"""Parse logs and print info"""


import re


def prnt(report: dict) -> None:
    """
    prnt - Prints after 10 logs or an exception
    @report: Dictionary
    Returns: Nothing
    """
    for key, val in report.items():
        if val or key == "File size":
            print("{}: {}".format(key, val), flush=True)


if __name__ == "__main__":
    report = {
            "File size": 0, 200: 0, 301: 0, 400: 0, 401: 0,
            403: 0, 404: 0, 405: 0, 500: 0}
    regForm = re.compile(r"""([0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.[0-2]?
    [0-9]?[0-9]\.[0-2]?[0-9]?[0-9]|[^\ ]*[^\ ])\ ?\-\ ?\[([0-9]{4}\-[0-1]{1}
    [0-9]{1}\-[0-3]{1}[0-9]{1}\ [0-2]{1}[0-9]{1}\:[0-5]{1}[0-9]{1}\:
    [0-5]{1}[0-9]{1}\.[0-9]{6})\]\ (\"GET\ \/projects\/260\ HTTP\/1\.1\")
    \ ([^\ ]*[^\ ])\ ([1-9][0-9]*)""", re.X)
    counter = 0
    try:
        while 1:
            std_in = input()
            if counter == 10:
                prnt(report)
                counter = 0
            matched = re.match(regForm, std_in)
            counter += 1
            if not matched:
                continue
            matched = regForm.search(std_in)
            resp = list(matched.groups())
            report["File size"] += int(resp[-1])
            try:
                report[int(resp[-2])] += 1
            except ValueError:
                pass
    except (KeyboardInterrupt, EOFError):
        prnt(report)
