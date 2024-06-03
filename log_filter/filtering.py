from collections.abc import Iterable
from datetime import datetime
from ipaddress import IPv4Address

from pandas import DataFrame


def create_dataframe(logs: Iterable[tuple[IPv4Address, datetime, str]]) -> DataFrame:
    """
    Create a pandas DataFrame from an iterable of tuples extracted from a log.

    Args:
        logs: tuples representing a log line: ip address, datetime and log message.

    Returns:
        pandas DataFrame with a datetime index and two columns: ip address and log
        message.
    """
    df = DataFrame(logs, columns=["ip", "datetime", "log"])
    df.set_index("datetime", inplace=True)
    return df


def filter_range(df: DataFrame, start: str | None, end: str | None) -> DataFrame:
    """
    Filter a DataFrame with a datetime index to the given range.

    Args:
        df: The DataFrame to filter.
        start: A string representing the starting date from which to filter.
        end (str): A string representing the ending date to which to filter.

    Returns:
        The filtered DataFrame.
    """
    return df.loc[start:end]  # type: ignore
