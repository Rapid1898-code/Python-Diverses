import hashlib, binascii, os
 
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]

    print(f"DEBUG Salt: {salt}")
    print(f"DEBUG StoredPW: {stored_password}")
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

# stored_password = hash_password('ThisIsAPassWord')
# print(stored_password)
storedPW = "d829ae2a16f45382ebdfaffa06fd2aa2e5aa3ae98fcb7667b1a38431a995be5896e3473648db81f0b53aade47955972cacbaf4b390db6a5424e77f66cb86df50569c159c410ad70efc52d2b1f43265153b0ba922ed6dd1a51790e5c50142672f"
print(verify_password(storedPW,"xyz"))
# print(verify_password(storedPW,"ThisIsAPassWord"