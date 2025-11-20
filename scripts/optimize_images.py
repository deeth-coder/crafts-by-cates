import os
import json
import shutil
from PIL import Image

# Configuration
IMG_DIR = 'app/static/img'
BACKUP_DIR = 'app/static/img_backup'
CONTENT_DIR = 'app/content'
MAX_WIDTH = 2000
QUALITY = 80

# Ensure backup directory exists
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

# Track filename changes for updating JSON content
# key: old_filename, value: new_filename
rename_map = {}

# Supported extensions
EXTENSIONS = {'.png', '.jpg', '.jpeg', '.webp'}

print(f"Starting image optimization in {IMG_DIR}...")

# 1. Process Images
for filename in os.listdir(IMG_DIR):
    if filename.startswith('.'): continue # Skip hidden files
    
    name, ext = os.path.splitext(filename)
    if ext.lower() not in EXTENSIONS:
        continue

    file_path = os.path.join(IMG_DIR, filename)
    
    # Open image
    try:
        with Image.open(file_path) as img:
            # Calculate new size
            width, height = img.size
            if width > MAX_WIDTH:
                ratio = MAX_WIDTH / width
                new_height = int(height * ratio)
                img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
                print(f"Resized {filename}: {width}x{height} -> {MAX_WIDTH}x{new_height}")
            else:
                print(f"Processing {filename}...")

            # Construct new filename
            new_filename = f"{name}.webp"
            new_file_path = os.path.join(IMG_DIR, new_filename)

            # Save as WebP
            img.save(new_file_path, 'WEBP', quality=QUALITY)
            
            # Add to rename map if name changed or just extension changed
            # We store just the filename part because that's how they are likely stored in JSON
            if filename != new_filename:
                rename_map[filename] = new_filename

    except Exception as e:
        print(f"Error processing {filename}: {e}")
        continue

    # Move original to backup if it's not the new file (in case we re-run or overwrite)
    # If we converted png -> webp, we move png to backup.
    if filename != new_filename:
        backup_path = os.path.join(BACKUP_DIR, filename)
        shutil.move(file_path, backup_path)

print(f"Processed {len(rename_map)} images.")

# 2. Update Content JSON Files
print("Updating content JSON files...")

json_files = [f for f in os.listdir(CONTENT_DIR) if f.endswith('.json')]

for json_file in json_files:
    file_path = os.path.join(CONTENT_DIR, json_file)
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace filenames
    # We do a simple string replacement. This is safer than parsing JSON 
    # for every field, assuming filenames are unique enough.
    # To be safer, we could parse JSON, but strict string replacement for "filename.png" -> "filename.webp"
    # is usually fine for this scope.
    
    updated_content = content
    for old_name, new_name in rename_map.items():
        # We replace '/static/img/old_name' and just 'old_name' to be safe,
        # but simple replacement of the filename should cover both.
        updated_content = updated_content.replace(old_name, new_name)
    
    if content != updated_content:
        with open(file_path, 'w') as f:
            f.write(updated_content)
        print(f"Updated {json_file}")
    else:
        print(f"No changes in {json_file}")

print("Done! Original images moved to app/static/img_backup.")

