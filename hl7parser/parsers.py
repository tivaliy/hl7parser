"""
Converting HL7 messages to dictionaries

http://www.prschmid.com/2016/11/converting-adt-hl7-message-to-json.html
"""

import json
from typing import Any, Union

from hl7apy.parser import Message, parse_message


class HL7MessageParser:
    """
    Hl7 Message Parser class.
    """

    supported_segment_terminators = ("\r", "\n")

    @classmethod
    def hl7_to_dict(
        cls,
        string: str,
        segment_terminator: str = "\r",
        use_long_name: bool = True,
        find_groups: bool = True,
        force_validation: bool = False,
    ) -> Union[dict, str]:
        """Converts an HL7 string to a dictionary.

        :param string: The input HL7 string
        :param segment_terminator: A segment terminator to use, defaults to "\r"
        :param use_long_name: Whether to use the long names
                              (e.g. "patient_name" instead of "pid_5")
        :param find_groups: Whether to find groups, defaults to False
        :param force_validation: Whether to force validation, defaults to False
        :returns: A dictionary representation of the HL7 message
        """
        # hl7apy only supports \r as segment terminator
        string = string.replace(segment_terminator, "\r")
        m = parse_message(string, find_groups=find_groups, force_validation=force_validation)
        return cls.hl7_message_to_dict(m, use_long_name=use_long_name)

    @classmethod
    def hl7_message_to_dict(cls, message: Message, use_long_name: bool = True) -> Union[dict, str]:
        """Converts an HL7 message to a dictionary.

        :param message: The HL7 message as returned by :func:`hl7apy.parser.parse_message`
        :param use_long_name: Whether to use the long names (e.g. "patient_name" instead of "pid_5")
        :returns: A dictionary representation of the HL7 message
        """
        if message.children:
            d: dict[Any, Any] = {}
            for c in message.children:
                name = str(c.name)
                if use_long_name:
                    name = str(c.long_name) if c.long_name else name
                dictified = cls.hl7_message_to_dict(c, use_long_name=use_long_name)
                if name in d:
                    if not isinstance(d[name], list):
                        d[name] = [d[name]]
                    d[name].append(dictified)
                else:
                    d[name] = dictified
            return d
        else:
            return message.to_er7()

    @classmethod
    def hl7_to_json(cls, string: str, **kwargs) -> str:
        """Converts an HL7 string to a JSON string.

        :param string: The input HL7 string/message
        :returns: A JSON string representation of the HL7 message
        """
        res = cls.hl7_to_dict(string, **kwargs)
        return json.dumps(res)
