# This file was generated by liblab | https://liblab.com/

"""
Creates a BaseService class.
Performs API calls,sets authentication tokens and handles http exceptions.

Class:
    BaseService
"""
import platform
from typing import List, Union
from enum import Enum
import re
from ..net.http_client import HTTPClient


class BaseService:
    """
    A class to represent a base serivce

    Attributes
    ----------
    _url_prefix : str
        The base URL

    Methods
    -------
    set_api_key(token: str) -> None:
        Sets bearer token key
    def _add_required_headers(headers: dict):
        Request authorization headers
    def set_base_url(url: str):
        Sets the base url
    """

    _url_prefix = "http://api.example.com"

    _http = HTTPClient(None)

    def __init__(self, api_key: str) -> None:
        """
        Initialize client

        Parameters:
        ----------
           api_key : str
                A Api key
        """
        self._api_key = api_key

    @classmethod
    def _pattern_matching(cls, value: str, pattern: str, variable_name: str):
        if re.match(r"{}".format(pattern), value):
            return value
        else:
            raise ValueError(f"Invalid value for {variable_name}: must match {pattern}")

    @classmethod
    def _enum_matching(
        cls, value: Union[str, Enum], enum_values: List[str], variable_name: str
    ):
        str_value = value.value if isinstance(value, Enum) else value
        if str_value in enum_values:
            return value
        else:
            raise ValueError(
                f"Invalid value for {variable_name}: must match one of {enum_values}"
            )

    def set_base_url(self, url: str) -> None:
        """
        Sets the base URL

        Parameters:
        ----------
            url:
                The base URL
        """
        self._url_prefix = url

    def set_api_key(self, api_key: str) -> None:
        """
        Sets access token key

        Parameters
        ----------
        api_key: string
            API key value
        """
        self._api_key = api_key

    def _add_required_headers(self, headers: dict):
        """
        Request authorization headers

        Parameters
        ----------
        headers: dict
            Headers dict to add auth headers to
        """
        headers["User-Agent"] = f"Toolhouse/1.2.1 Python/{platform.python_version()}"
        headers["Authorization"] = f"Bearer {self._api_key}"
        return headers
