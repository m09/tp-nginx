from argparse import ArgumentParser

from .filtering import create_dataframe, filter_range
from .parsing import parse_log_line


def main() -> None:
    """Entrypoint of the program."""
    parser = ArgumentParser("log-filter")
    parser.add_argument(
        "--start",
        help="Start date to consider to retrieve the logs in ISO format (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--end",
        help="End date to consider to retrive the logs in ISO format (YYYY-MM-DD).",
    )
    args = parser.parse_args()
    with open("/home/mog/repos/shuuchuu/datasets/nginx-log/access-small.log") as fh:
        logs = []
        for line in fh:
            parsed = parse_log_line(line)
            if parsed is not None:
                logs.append(parsed)
    df = create_dataframe(logs)
    for index, (ip, log) in filter_range(df, args.start, args.end).iterrows():
        print(index.strftime("%d/%m/%Y %H:%M:%S"), ip, log)
