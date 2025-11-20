import json
import os

try:
    with open('app/content/copy.json', 'r') as f:
        data = json.load(f)
        print("JSON loaded successfully.")
        if 'about' in data:
            print("About section found.")
            if 'images' in data['about']:
                print(f"Images found: {len(data['about']['images'])}")
                print(data['about']['images'])
            else:
                print("ERROR: 'images' key missing in 'about' section.")
                print(data['about'].keys())
        else:
            print("ERROR: 'about' section missing.")
except Exception as e:
    print(f"JSON Load Error: {e}")
