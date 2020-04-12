import copy
from typing import List


class CryptoHelper:
    @classmethod
    def _strip_whitespaces(cls, msg: str) -> (str, List[int]):
        """Receive a message with white spaces, strip the white spaces and return a list with indexes of the
        whitespaces.

        (Not in place)
        """
        whitespace_index_list = []
        index_counter = 0
        for char in msg:
            if char == " ":
                whitespace_index_list.append(index_counter)
            index_counter += 1

        stripped_msg = copy.deepcopy(msg).strip(" ")
        return stripped_msg, whitespace_index_list

    @classmethod
    def _recover_whitespaces(cls, msg: str, whitespace_index_list: List[int]):
        """Take the index list for white spaces and create a new msg that contains the correct white spaces at the
        indexes.

        This only works for block ciphers, otherwise the indexes for the white spaces are bogus.

        (Not in place)
        """
        buffer_msg = copy.deepcopy(msg)
        for whitespace_index in whitespace_index_list:
            buffer_msg = buffer_msg[:whitespace_index] + " " + buffer_msg[whitespace_index:]
        return buffer_msg

    @classmethod
    def ignore_whitespaces(cls, fun):
        """Reads the "msg" entry from the function kwargs and strips all whitespaces from it.
        Then, calls the function with the stripped message and adds the whitespaces back to the converted message.

        Only works with block ciphers that translate blocks while keeping the identical length.

        (Decorator)
        """
        def wrapper(*args, **kwargs):
            msg = kwargs["msg"]
            stripped_msg, whitespace_index_list = CryptoHelper._strip_whitespaces(msg=msg)
            cc_kwargs = copy.deepcopy(kwargs)
            cc_kwargs["msg"] = stripped_msg

            converted_msg = fun(args, kwargs)
            converted_msg_with_whitespaces = CryptoHelper._recover_whitespaces(
                msg=converted_msg,
                whitespace_index_list=whitespace_index_list
            )
            return converted_msg_with_whitespaces
        return wrapper
