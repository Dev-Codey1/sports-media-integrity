import firebase_admin
from firebase_admin import credentials, firestore
import imagehash
from PIL import Image
import datetime

# 1. Firebase Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def protect_media(image_path, owner_name):
    try:
        # 2. Generate Perceptual Hash (Digital Fingerprint)
        # Ye normal hash se behtar hai kyunki ye edit ki hui images ko bhi pehchan leta hai
        hash_value = str(imagehash.phash(Image.open(image_path)))
        
        # 3. Firestore mein data upload karna
        doc_ref = db.collection('sports_assets').document(hash_value)
        doc_ref.set({
            'hash': hash_value,
            'owner': owner_name,
            'registered_at': datetime.datetime.now(),
            'status': 'verified'
        })
        
        print(f"✅ Success! Asset Protected.\nHash: {hash_value}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Test karne ke liye (Apne mobile se kisi image ka path dein)
# protect_media('test_sports_photo.jpg', 'My Sports Org')
