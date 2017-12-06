import abc


class SdmuxProtocol(abc.ABC):
    @abc.abstractmethod
    def off(self):
        raise NotImplementedError

    @abc.abstractmethod
    def host(self):
        raise NotImplementedError

    @abc.abstractmethod
    def dut(self):
        raise NotImplementedError
