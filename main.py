def check_for_violations(test_image_path):
    # 1. Test image ka hash nikalna
    test_hash = str(imagehash.phash(Image.open(test_image_path)))
    
    # 2. Firestore mein search karna
    doc_ref = db.collection('sports_assets').document(test_hash)
    doc = doc_ref.get()
    
    if doc.exists:
        data = doc.to_dict()
        print(f"🚨 ALERT: Unauthorized Content Detected!")
        print(f"Original Owner: {data['owner']}")
        print(f"Status: {data['status']}")
    else:
        print("✅ Content is unique or not in our database.")
