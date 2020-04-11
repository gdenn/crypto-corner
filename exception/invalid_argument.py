class InvalidArgumentException(Exception):
    def __init__(self, algorithm: str, argument: str, reason: str):
        message = "Invalid argument for {argument} at {algorithm}: {reason}".format(
            argument=argument, algorithm=algorithm, reason=reason)

        super(InvalidArgumentException, self).__init__(message=message)
