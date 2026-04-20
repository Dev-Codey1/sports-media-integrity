import hashlib

def generate_fingerprint(file_path):
    # File ko read karke uska unique hash generate karna
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # File ko chunks mein read karna taki mobile hang na ho
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "File nahi mili! Path check karein."

# Test karne ke liye
file_name = "test_image.jpg" # Aapke mobile mein jo image ho uska naam
print(f"Digital Signature: {generate_fingerprint(file_name)}")
