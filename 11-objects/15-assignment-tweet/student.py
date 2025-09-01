class Tweet:
    def __init__(self, message, max_length):
        if max_length < 1:
            raise ValueError("max_length moet minstens 1 zijn.")
        self._max_length = max_length
        self._message = self.__truncate(message)

    def __truncate(self, text):
        return text[:self._max_length]

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, new_message):
        self._message = self.__truncate(new_message)

    @property
    def max_length(self):
        return self._max_length

    @max_length.setter
    def max_length(self, new_max_length):
        if new_max_length < 1:
            raise ValueError("max_length moet minstens 1 zijn.")
        self._max_length = new_max_length
        self._message = self.__truncate(self._message)
