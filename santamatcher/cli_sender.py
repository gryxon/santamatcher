from argparse import ArgumentParser


def prepare_parser(parser: ArgumentParser):
    parser.add_argument('--match_request', '-r', type=str, help='Path to file with request description')
    parser.add_argument('--pushbullet_api_key', '-pa', type=str, help='Path to file with request description')
    parser.add_argument('--pushbullet_device_id', '-pd', type=str, help='Path to file with request description')
