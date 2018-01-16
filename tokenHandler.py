import random
from cryptography.fernet import Fernet

class TokenHandler:
    
    def __init__(self):
        self.secret = bytes(str(random.random() * 10**100), "utf-8")
        self.ttl = 180
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)

    def generateToken(self):
        token = self.f.encrypt(self.secret)
        return token

    def validateToken(self, token):
        try:
            plainText = self.f.decrypt(token, self.ttl)
            return plainText
        except:
            return False