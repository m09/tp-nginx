from datetime import datetime
from ipaddress import IPv4Address
from re import VERBOSE
from re import compile as re_compile

_pattern = re_compile(
    r"""
    (\d+\.\d+\.\d+\.\d+)   # IP address
    \ -\ -\                # Separator between the IP address and the datetime
    \[(.*?)\]              # Datetime
    \                      # Separator between the datetime and the rest of the log line
    (.*)
    """,
    flags=VERBOSE,
)


def parse_log_line(line: str) -> tuple[IPv4Address, datetime, str] | None:
    """
    Parse a log line into a tuple (IP address, datetime, rest of the log line).

    Args:
        line: Nginx log line.

    Returns:
        Line parsed into a (IP address, datetime, rest of the log line) tuple or None if
        the parsing failed.
    """
    result = _pattern.match(line)
    if result is None:
        return None
    ip_string, datetime_string, rest = result.groups()
    return (
        IPv4Address(ip_string),
        datetime.strptime(datetime_string, "%d/%b/%Y:%H:%M:%S %z"),
        rest,
    )
