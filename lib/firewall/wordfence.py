import re


__item__ = "Wordfence (Feedjit)"


def detect(content, **kwargs):
    content = str(content)
    detection_schema = (
        re.compile(r"Generated by Wordfence", re.I),
        re.compile(r"Your access to this site has been limited", re.I),
        re.compile(r"<.+>Wordfence<.+.>", re.I)
    )
    for detection in detection_schema:
        if detection.search(content) is not None:
            return True
