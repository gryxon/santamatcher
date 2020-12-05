from abc import ABC, abstractmethod


MESSAGE_TEMPLATE = """
Cześć {giver_name}!

Na święta kupujesz prezent dla {taker_name}.

W celu ostatecznej weryfikacji poprawności działania programu, wypełnij proszę ankietę: {poll_link}. 
Jeżeli ktoś wypełnił osobę, której dajesz prezent prześlij proszę tę informację do {moderator}.

Powodzenia!
"""


class Notifier(ABC):

    @abstractmethod
    def notify(self, match_result):
        ...


class SmsNotifier(Notifier):
    pass


class MailNotifier(Notifier):
    pass
