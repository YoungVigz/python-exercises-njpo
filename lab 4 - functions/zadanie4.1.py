import hashlib, binascii
from os import urandom
import shelve

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_pwdhash = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_pwdhash

def requires_auth(func):
    def wrapper(username, password, *args, **kwargs):
        with shelve.open('user_db') as db:
            if username in db:
                stored_password = db[username]
                if verify_password(stored_password, password):
                    print(f"Autoryzacja przebiegła pomyślnie")
                    return func(*args, **kwargs)
                else:
                    print("Nie udało się zalogować")
            else:
                print(f"Konto '{username}' nie istnieje.")
        return None
    return wrapper

@requires_auth
def protected_function():
    print(f"Dostałeś się do funkcji autroyzowanej")

def add_user(username, password):
    with shelve.open('user_db') as db:
        db[username] = hash_password(password)
        print(f"'{username}' konto stworzone")

if __name__ == "__main__":
    add_user('test', 'haslo123')

    protected_function('test', 'haslo123')
    protected_function('test', 'admin1234') 
    protected_function('admin', 'haslo123')
