import time
from abc import ABC, abstractmethod
from random import shuffle
from typing import Tuple
import logging

from pushbullet import Pushbullet

from santamatcher.models import MatchResult

MESSAGE_TEMPLATE = """
HO! HO! HO! Witaj Mój Drogi Elfie!
Pisze do Ciebie Święty Mikołaj. Czy byłeś grzeczny w tym roku? Bardzo chciałbym odwiedzić Cię osobiście, ale jestem już stary i zmęczony, a rok 2021 nie był lekki dla moich reniferów.
Ale nic straconego! Wciąż możemy uratować te Święta. 
Wystarczy że przygotujesz prezent dla {taker_name}.
Pamiętaj, żeby go ładnie zapakować i umieścić pod choinką na czas - w końcu działasz w moim imieniu!
Dziękuję za pomoc!
"""


class Notifier(ABC):

    @abstractmethod
    def notify(self, match_result):
        ...


class SmsPushbulletNotifier(Notifier):
    def __init__(self, token: str, device_id: int, interval_gap_between_messages: int = 0):
        self.token = token
        self.device_id = device_id
        self.interval_gap_between_messages = interval_gap_between_messages

    def notify(self, match_results: Tuple[MatchResult, ...]):
        push_bullet_client = Pushbullet(self.token)
        takers, givers = [], []
        for match_result in match_results:
            device = push_bullet_client.devices[self.device_id]
            push_bullet_client.push_sms(
                device,
                match_result.giver.communication_address,
                MESSAGE_TEMPLATE.format(taker_name=match_result.taker.name)
            )
            takers.append(match_result.taker.name)
            givers.append(match_result.giver.name)
            time.sleep(self.interval_gap_between_messages)

        shuffle(takers)
        shuffle(givers)
        logging.info(f"Messages were sent to (random order): {givers}")
        logging.info(f"People who will get presents (random order): {takers}")


class MailNotifier(Notifier):
    pass
