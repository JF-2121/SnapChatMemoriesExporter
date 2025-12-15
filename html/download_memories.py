import re
import os
import urllib.request
from datetime import datetime

source_file = 'memories_history.html'
output_folder = 'memories_download'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("Reading file...")
try:
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: Could not find {source_file}. Make sure it is in the same folder as this script.")
    exit()

# Extract links and dates using regex
# Matches the pattern: downloadMemories('URL', ...)
matches = re.findall(r"downloadMemories\('([^']+)'", content)

print(f"Found {len(matches)} memories. Starting download...")

for i, url in enumerate(matches):
    try:
        # Try to find the timestamp in the URL to date the file
        ts_match = re.search(r'ts=(\d+)', url)
        if ts_match:
            timestamp = int(ts_match.group(1)) / 1000
            date_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M-%S')
            # We don't know if it's jpg or mp4 yet, defaulting to no extension or guessing
            # The download usually fixes this, or we can rename later.
            # For safety, we treat them as generic files first.
            filename = f"memory_{date_time}_{i+1}"
        else:
            filename = f"memory_{i+1}"

        file_path = os.path.join(output_folder, filename)

        # Skip if already downloaded
        if os.path.exists(file_path) or os.path.exists(file_path + ".jpg") or os.path.exists(file_path + ".mp4"):
            print(f"[{i+1}/{len(matches)}] Skipping {filename} (already exists)")
            continue

        print(f"[{i+1}/{len(matches)}] Downloading {filename}...")

        # Download the file
        local_filename, headers = urllib.request.urlretrieve(url, file_path)

        # Try to add correct extension based o-n content-type header
        content_type = headers.get('Content-Type', '')
        extension = ""
        if 'video' in content_type:
            extension = ".mp4"
        elif 'image' in content_type:
            extension = ".jpg"

        if extension:
            new_name = f"{file_path}{extension}"
            if not os.path.exists(new_name):
                os.rename(file_path, new_name)

    except Exception as e:
        print(f"Failed to download memory {i+1}: {str(e)}")

print("All done! Check the 'memories_download' folder.")
