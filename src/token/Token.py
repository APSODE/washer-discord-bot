import base64


class Token:
    @staticmethod
    def GetToken():
        etoken = "TVRBM056STNNak16TURZeU1EZzVOVEk1TWcuR0JDdXhKLlRyRjVFV1luRHRpalB2OWQyWl9FNnN4V1NxZmlMSmhQNzUwNVp3"
        return base64.b64decode(etoken).decode("ascii")
