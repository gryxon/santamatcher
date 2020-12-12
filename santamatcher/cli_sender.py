import json
from argparse import ArgumentParser
from base64 import b64encode

from santamatcher.matchers.matchers import match
from santamatcher.models import MatchRequest
from santamatcher.notifiers import SmsPushbulletNotifier


def prepare_parser(parser: ArgumentParser):
    parser.add_argument('--match_request', '-mr', type=str, help='Path to file with request description')
    parser.add_argument('--pushbullet_api_key', '-pa', type=str, help='Api key for pushbullet')
    parser.add_argument('--pushbullet_device_id', '-pd', type=int, help='Device id from which sms will be sent')
    parser.add_argument('--poll_link', '-pl', type=str, help='Link to the poll with confirmation')
    parser.add_argument('--between_message_gap_interval', '-gi', type=str, help='Interval of gap between sent messages')


def main():
    parser = ArgumentParser()
    prepare_parser(parser)

    args = parser.parse_args()
    with open(args.match_request) as file:
        match_request = MatchRequest.from_dict(json.load(file))

    match_results = match(
        people=match_request.people,
        required_matches=match_request.required_matches,
        forbidden_matches=match_request.forbidden_matches,
    )

    print(b64encode(bytes(repr(match_results), 'utf-8')))

    notifier = SmsPushbulletNotifier(
        token=args.pushbullet_api_key,
        device_id=args.pushbullet_device_id,
        poll_link=args.poll_link,
    ).notify(match_results)


if __name__ == "__main__":
    main()
