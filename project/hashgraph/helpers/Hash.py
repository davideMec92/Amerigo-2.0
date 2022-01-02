from hashlib import sha256


class Hash:
    @staticmethod
    def stringToHash(content: str):
        return sha256(content.encode()).hexdigest()
