from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)  #hashing the password

hash("password") #testing the hash function

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)  #verifying the password

verify("password", hash("password")) #testing the verify function