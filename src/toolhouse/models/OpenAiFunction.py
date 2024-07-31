# This file was generated by liblab | https://liblab.com/

from .base import BaseModel


class OpenAiFunction(BaseModel):
    """
    Represents a function call for OpenAI with an additional type attribute.
    """

    def __init__(self, name: str, arguments: str, **kwargs):
        """
        Initialize OpenAiFunction
        Parameters:
        ----------
            name: str
            arguments: str
        """
        self.name = name
        self.arguments = arguments