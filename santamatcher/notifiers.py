import time
from abc import ABC, abstractmethod
from typing import Tuple

from pushbullet import Pushbullet

from santamatcher.models import MatchResult

MESSAGE_TEMPLATE = """
HO! HO! HO! Witaj Mój Drogi Elfie!
Pisze do Ciebie Święty Mikołaj. Czy byłeś grzeczny w tym roku? Bardzo chciałbym odwiedzić Cię osobiście, ale jestem już stary i zmęczony, a rok 2020 nie był lekki dla moich reniferów.
Ale nic straconego! Wciąż możemy uratować te Święta. 
Wystarczy że przygotujesz prezent dla {taker_name}.
Pamiętaj, żeby go ładnie zapakować i umieścić pod choinką na czas - w końcu działasz w moim imieniu!
Na koniec, mała prośba: żeby pod choinką dla każdego znalazł się prezent, uzupełnij, proszę, tę ankietę:
{poll_link}
Dziękuję za pomoc!
"""


class Notifier(ABC):

    @abstractmethod
    def notify(self, match_result):
        ...


class SmsPushbulletNotifier(Notifier):
    def __init__(self, token: str, device_id: int, poll_link: str, between_message_gap_interval: int = 0):
        self.token = token
        self.device_id = device_id
        self.poll_link = poll_link
        self.between_message_gap_interval = between_message_gap_interval

    def notify(self, match_results: Tuple[MatchResult, ...]):
        push_bullet_client = Pushbullet(self.token)
        for match_result in match_results:
            device = push_bullet_client.devices[self.device_id]
            push_bullet_client.push_sms(
                device,
                match_result.giver.communication_address,
                MESSAGE_TEMPLATE.format(
                    giver_name=match_result.giver.name,
                    taker_name=match_result.taker.name,
                    poll_link=self.poll_link,
                )
            )
            time.sleep(self.between_message_gap_interval)


class MailNotifier(Notifier):
    pass
