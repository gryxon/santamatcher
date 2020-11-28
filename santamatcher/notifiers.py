from abc import ABC, abstractmethod


class Notifier(ABC):

    @abstractmethod
    def notify(self, match_result):
        ...


class SmsNotifier(Notifier):
    pass


class MailNotifier(Notifier):
    pass
