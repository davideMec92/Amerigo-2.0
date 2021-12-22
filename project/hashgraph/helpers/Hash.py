from hashlib import sha256


class Hash:
    @staticmethod
    def stringToHash(content):
        return sha256(content).hexdigest()
