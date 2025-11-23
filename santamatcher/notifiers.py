import time
from abc import ABC, abstractmethod
from typing import Tuple

from pushbullet import Pushbullet
import requests

from santamatcher.models import MatchResult

MESSAGE_TEMPLATE = """Ho, ho, ho! Dawno żeśmy się nie widzieli! Rok minął jak z bicza strzelił i znowu trzeba iść do pracy...

Apropos pracy, Renifer Rudolf poślizgnął się na skórce od banana i poszedł na L4 do końca stycznia. Cały grafik zrujnowany! Żeby w Puławach odbyły się święta, musisz mi pomóc. Nałożysz czerwoną czapkę Mikołaja, spakujesz prezent i dostarczysz go zgodnie z wytycznymi z Załącznika. Zostaniesz honorowym Zastępcą Mikołaja, a to nie byle jaki awans! Noś ten tytuł z dumą i nie zawiedź mnie. 

Pamiętaj o ładnym opakowaniu prezentu! 
Święty Mikołaj 

Załącznik: 
Honorowy Zastępca Mikołaja: {giver_name}
Obdarowany: {taker_name}
Data Dostawy: 24 grudnia 2025
Adres dostawy: Pod Choinką"""


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
            device = push_bullet_client.devices[self.device_id]
            requests.post(
                "https://api.pushbullet.com/v2/texts",
                headers={"Access-Token": self.token},
                json={
                    "data": {
                        "target_device_iden": device.device_iden,
                        "addresses": [match_result.giver.communication_address],
                        "message": MESSAGE_TEMPLATE.format(
                            taker_name=match_result.taker.name,
                            giver_name=match_result.giver.name,
                        ),
                    }
                },
            )
            time.sleep(self.interval_gap_between_messages)


class MailNotifier(Notifier):
    pass
