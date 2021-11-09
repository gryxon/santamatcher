import time
from abc import ABC, abstractmethod
from typing import Tuple

from pushbullet import Pushbullet

from santamatcher.models import MatchResult

MESSAGE_TEMPLATE = """
HO! HO! HO! Witaj Mój Drogi Elfie!
Pisze do Ciebie Święty Mikołaj. Czy byłeś grzeczny w tym roku? Bardzo chciałbym odwiedzić Cię osobiście, ale jestem już stary i zmęczony, a rok 2021 nie był lekki dla moich reniferów.
Ale nic straconego! Wciąż możemy uratować te Święta. 
Wystarczy że przygotujesz prezent dla {taker_name}.
Pamiętaj, żeby go ładnie zapakować i umieścić pod choinką na czas - w końcu działasz w moim imieniu!
Na koniec, mała prośba: żeby pod choinką dla każdego znalazł się prezent, podaj, proszę, ten numerek:
{taker_secret_identity} - temu kto o niego zapyta :)
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
        for match_result in match_results:
            taker = match_result.taker
            device = push_bullet_client.devices[self.device_id]
            push_bullet_client.push_sms(
                device,
                match_result.giver.communication_address,
                MESSAGE_TEMPLATE.format(
                    taker_name=taker.name,
                    taker_secret_identity=taker.secret_identity,
                )
            )
            time.sleep(self.interval_gap_between_messages)


class MailNotifier(Notifier):
    pass
