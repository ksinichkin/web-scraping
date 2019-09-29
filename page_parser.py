import requests
from lxml import html
import traceback
import logging


class BaseConnectionError(Exception):
    """
    Base exception class for all connection related exceptions.
    :param message: string
    :param status_code: int
    :param traceback: string
    """
    def __init__(self, message, status_code=None, traceback=None):
        self.message = message
        self.traceback = traceback
        self.status_code = status_code

    def __str__(self):
        return self.message


class ClientRequestError(BaseConnectionError):
    """
    This will be raised whenever there is a misconfiguration in
    the client request.
    :param message: string
    :param status_code: int
    :param traceback: string
    """
    def __init__(self, message, status_code=None, traceback=None):
        super().__init__(message, status_code=status_code, traceback=traceback)


class Parser:
    """Base parser class
    All page parsers should be inherited from this class,
    e.g. xPathParser(Parser).
    """


class xPathParser(Parser):
    """ Class for parsing html content to find elements
    according to xPath schema.
    """
    def parse(self, content, schema):
        """ Searching for elements in html content according to xPath schema
        :param content: string
        :returns: values for requested fields
        :rtype: dictionary
        """
        tree = html.fromstring(content)

        parsed_content = {}
        for name, schema_item in schema.items():
            element = tree.xpath(schema_item)
            if element != []:
                result = element[0].text
            else:
                err_msg = f'{name} not found with provided xPath {schema_item}'
                result = f'{name} not found on the page'
                logging.warning(err_msg)

            parsed_content[name] = result

        return parsed_content


class Page:
    """ Class to represent html page.
    Contains raw html page content and parsed page if needed.
    """
    def __init__(self):
        """ Default constructor"""
        self.__content = ""
        self.__parsed_page = {}

    def load(self, url, timeout=10):
        """ Loading html page specified in url and stores in content.
        :param url: string
        :returns none
        """
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
        except requests.Timeout:
            msg = f'Timeout ({timeout}) error during request {url}'
            logging.error(msg)
            raise BaseConnectionError(msg, traceback=traceback.format_exc())
        except requests.HTTPError as err:
            msg = (f'Client error during request {url} with code: '
                   f'{err.response.status_code}')
            logging.error(msg)
            raise ClientRequestError(msg, err.response.status_code,
                                     traceback.format_exc())
        except requests.RequestException:
            msg = f'Cannot access {url}'
            logging.error(msg)
            raise ClientRequestError(msg, traceback=traceback.format_exc())
        else:
            self.__content = resp.text

    def get_content(self):
        """ Returning page content
        :returns: html page content
        :rtype: string
        """
        return self.__content

    def parse_page(self, parser, schema=None):
        """ Parsing page content using parser of Parser type,
        e.g. xPathParser() and stores in __parsed_page.
        :returns: none
        """
        self.__parsed_page = parser.parse(self.__content, schema)

    def get_parsed_page(self):
        """ Returning parsed html page content
        :returns: parsed html page content
        :rtype: string
        """
        return self.__parsed_page
