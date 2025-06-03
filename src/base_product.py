from abc import ABC, abstractmethod


class BaseProduct(ABC):
    pass

    @classmethod
    @abstractmethod
    def new_product(self, *args, **kwargs):
        pass
