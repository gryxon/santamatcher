# Santamatcher

A minimalistic tool for matching people in pairs in secret way and sending match results to them.

Current implementation use [Pushbullet API](https://docs.pushbullet.com/) for sending SMS messages for notification purpose.

## Instalation

In downloaded repository run with your Python environment:

```
pip install .
```

## Usage

### Match Request description files

```
{
    "people": [
        {"name": "Kamil", "communication_address": "+XXXXXXXXXXX"},
        {"name": "Kasia", "communication_address": "+XXXXXXXXXXX"},
        {"name": "Ola", "communication_address": "+XXXXXXXXXXX"},
        {"name": "Jarek", "communication_address": "+XXXXXXXXXXX"}
    ],
    "required_matches": [
        {"giver_name": "Jarek", "taker_name": "Ola"}
    ],
    "forbidden_matches": [
        {"giver_name": "Kasia", "taker_name": "Jarek"}
    ]
}
```

- `people` section contains description of people to match. 
  Each record has to contain `name` and `communication address` (for now it should be telephone number).
  
- `required_matches` section contains list of matches which has to be in the result of matching.
- `forbidden_matches` section contains list of matches which must not be in the result of matching.

### CLI Script

#### help output

```
$ santamatcher --help
usage: santamatcher [-h] [--match_request MATCH_REQUEST]
                    [--pushbullet_api_key PUSHBULLET_API_KEY]
                    [--pushbullet_device_id PUSHBULLET_DEVICE_ID]
                    [--poll_link POLL_LINK]
                    [--interval_gap_between_message INTERVAL_GAP_BETWEEN_MESSAGE]

optional arguments:
  -h, --help            show this help message and exit
  --match_request MATCH_REQUEST, -mr MATCH_REQUEST
                        Path to file with request description
  --pushbullet_api_key PUSHBULLET_API_KEY, -pa PUSHBULLET_API_KEY
                        API token for pushbullet
  --pushbullet_device_id PUSHBULLET_DEVICE_ID, -pd PUSHBULLET_DEVICE_ID
                        Device id from which sms will be sent
  --interval_gap_between_messages INTERVAL_GAP_BETWEEN_MESSAGES, -gi INTERVAL_GAP_BETWEEN_MESSAGE
                        Interval of gap between sent messages in seconds
```

- `--interval_gap_between_messages` - if the interval will be too small, it's likely that your phone will block the
stream of messages to send.

#### Example of usage

```
python cli_sender.py -mr path/to/match/request/description/file.json -pa API_KEY -pd 0 -pl link.to.poll.com 
```

## Architecture

```
--------------------------                          ----------------------                              ---------------------
|                        |    PUSHBULLET REST API   |                    |   Pushbullet notifications   |                   |
| Host with santamatcher | <----------------------> | Pushbullet servers | <--------------------------> | Your mobile phone |
|                        |                          |                    |                              |                   |
--------------------------                          ----------------------                              ---------------------
```