from src.BotObject import WasherDiscordBot


class WasherLee:
    def __init__(self):
        self._bot_instance = WasherDiscordBot()

    def Start(self) -> None:
        self._bot_instance.run(
            self._bot_instance.Token
        )


if __name__ == '__main__':
    WL = WasherLee()
    WL.Start()