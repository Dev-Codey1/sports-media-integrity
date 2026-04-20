from main import protect_media, check_for_violations
import time

# 1. Original Image ko register karna (Owner: Star Sports)
print("--- Registering Original Asset ---")
protect_media('original.jpg', 'Star Sports Official')

# 2. Thoda wait karte hain database update hone ka
time.asleep(2)

# 3. Ab wahi image (ya uska edited version) check karna
print("\n--- Scanning for Violations ---")
check_for_violations('copy_test.jpg')
