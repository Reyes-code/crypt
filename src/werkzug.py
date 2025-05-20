
from werkzeug.security import generate_password_hash, check_password_hash
from private import PrivateKey

class KeyHasher:
    def __init__(self):
        self.__private_key = PrivateKey().get_private_key()
    
    def hash_combined(self, user_password):
        combined = f"{self.__private_key}{user_password}"  # Concatenación
        return generate_password_hash(combined, method='pbkdf2:sha256')

    def verify_combined(self, hashed_combined, user_password):
        combined = f"{self.__private_key}{user_password}"
        return check_password_hash(hashed_combined, combined)
    
    def normal_hash(self,user_password):
        return generate_password_hash(user_password,method='pbkdf2:sha256')





