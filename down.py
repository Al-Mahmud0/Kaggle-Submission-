import os
import json

# Kaggle credentials সংরক্ষণ
kaggle_creds = {
    "username": "hm0mahmud",  # আপনার Kaggle username
    "key": "53ca4c2680818ddb76b7fbc451a23da7"  # আপনার Kaggle API key
}

# kaggle.json ফাইলটি তৈরি করুন
os.makedirs("/root/.kaggle/", exist_ok=True)
with open("/root/.kaggle/kaggle.json", "w") as f:
    json.dump(kaggle_creds, f)

# Permissions set করুন
os.chmod("/root/.kaggle/kaggle.json", 600)
