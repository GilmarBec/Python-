from threading import Thread


class AbstractListener:
    __thread: Thread

    def __init__(self):
        self.__thread = Thread(target=self._run, daemon=True)

    def start(self):
        self.__thread.start()
        return self

    def _run(self, *args: [any]):
        pass
