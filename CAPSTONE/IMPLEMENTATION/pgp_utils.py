"""Module 3 - OpenPGP key generation, encryption, decryption, signing and verification (PGPy)."""
import pgpy
from pgpy.constants import (PubKeyAlgorithm, KeyFlags, HashAlgorithm,
                            SymmetricKeyAlgorithm, CompressionAlgorithm)

def generate_keypair(name, email, passphrase=None):
    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 2048)
    uid = pgpy.PGPUID.new(name, email=email)
    key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
                hashes=[HashAlgorithm.SHA256], ciphers=[SymmetricKeyAlgorithm.AES256],
                compression=[CompressionAlgorithm.ZLIB])
    if passphrase:
        key.protect(passphrase, SymmetricKeyAlgorithm.AES256, HashAlgorithm.SHA256)
    return key

def sign_message(text, private_key, passphrase=None):
    msg = pgpy.PGPMessage.new(text)
    if private_key.is_protected:
        with private_key.unlock(passphrase):
            msg |= private_key.sign(msg)
    else:
        msg |= private_key.sign(msg)
    return msg

def encrypt_message(msg, recipient_pub):
    if not isinstance(msg, pgpy.PGPMessage):
        msg = pgpy.PGPMessage.new(msg)
    return recipient_pub.encrypt(msg)

def decrypt_message(armored, private_key, passphrase=None):
    enc = pgpy.PGPMessage.from_blob(str(armored))
    if private_key.is_protected:
        with private_key.unlock(passphrase):
            return private_key.decrypt(enc)
    return private_key.decrypt(enc)

def verify_signature(msg, sender_pub):
    try:
        return bool(sender_pub.verify(msg))
    except Exception:
        return False
