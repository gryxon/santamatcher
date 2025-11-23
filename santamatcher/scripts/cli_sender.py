import json
from argparse import ArgumentParser

from santamatcher.matchers.matchers import match
from santamatcher.models import MatchRequest
from santamatcher.notifiers import SmsPushbulletNotifier


def prepare_parser(parser: ArgumentParser):
    parser.add_argument('--match_request', '-mr', type=str, help='Path to file with request description')
    parser.add_argument('--pushbullet_api_key', '-pa', type=str, help='API token for pushbullet')
    parser.add_argument('--pushbullet_device_id', '-pd', type=int, help='Device id from which sms will be sent')
    parser.add_argument('--interval_gap_between_messages', '-gi', type=int, default=2,
                        help='Interval of gap between sent messages in seconds')


def main():
    parser = ArgumentParser()
    prepare_parser(parser)

    args = parser.parse_args()
    print("Arguments parsed\n")
    with open(args.match_request) as file:
        match_request = MatchRequest.from_dict(json.load(file))

    print("Match request loaded\n")
    match_results = match(
        people=match_request.people,
        required_matches=match_request.required_matches,
        forbidden_matches=match_request.forbidden_matches,
    )
    print("Match results calculated\n")

    SmsPushbulletNotifier(
        token=args.pushbullet_api_key,
        device_id=args.pushbullet_device_id,
        interval_gap_between_messages=args.interval_gap_between_messages
    ).notify(match_results)

    print("Messages sent\n")


if __name__ == "__main__":
    main()
