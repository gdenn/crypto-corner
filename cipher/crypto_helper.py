import copy
from typing import List


class CryptoHelper:
    @classmethod
    def _strip_sign(cls, msg: str, sign: str) -> (str, List[int]):
        """Receive a message with white spaces, strip the white spaces and return a list with indexes of the
        whitespaces.

        (Not in place)
        """
        sign_indexes = []
        index_counter = 0
        for char in msg:
            if char == sign:
                sign_indexes.append(index_counter)
            index_counter += 1

        stripped_msg = msg.replace(sign, "")
        return stripped_msg, sign_indexes

    @classmethod
    def _recover_sign(cls, msg: str, sign: str, sign_indexes: List[int]):
        """Take the index list for white spaces and create a new msg that contains the correct white spaces at the
        indexes.

        This only works for block ciphers, otherwise the indexes for the white spaces are bogus.

        (Not in place)
        """
        buffer_msg = copy.deepcopy(msg)
        for whitespace_index in sign_indexes:
            buffer_msg = buffer_msg[:whitespace_index] + sign + buffer_msg[whitespace_index:]
        return buffer_msg

    @classmethod
    def ignore_whitespaces(cls, function):
        def wrapper(*args, **kwargs):
            msg = kwargs["msg"]
            stripped_msg, whitespace_indexes = CryptoHelper._strip_sign(msg=msg, sign=" ")
            stripped_msg, new_line_indexes = CryptoHelper._strip_sign(msg=stripped_msg, sign="\n")
            kwargs["msg"] = stripped_msg
            converted_msg = function(*args, **kwargs)
            converted_msg = CryptoHelper._recover_sign(
                msg=converted_msg,
                sign="\n",
                sign_indexes=new_line_indexes
            )
            converted_msg = CryptoHelper._recover_sign(
                msg=converted_msg,
                sign=" ",
                sign_indexes=whitespace_indexes
            )
            return converted_msg

        return wrapper

    @classmethod
    def read_from_file(cls, function):
        def wrapper(*args, **kwargs):
            if "file" in kwargs:
                path: str = kwargs["file"]
                del kwargs["file"]
                with open(path, "r") as file:
                    msg = file.read()
                    kwargs["msg"] = msg
                    result = function(*args, **kwargs)
                    file.close()
                    return result
            else:
                return function(*args, **kwargs)

        return wrapper

    @classmethod
    def to_lowercase(cls, function):
        def wrapper(*args, **kwargs):
            msg: str = kwargs["msg"]
            msg = msg.lower()
            kwargs["msg"] = msg
            return function(*args, **kwargs)

        return wrapper



