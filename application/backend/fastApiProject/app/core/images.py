from fastapi import UploadFile
from datetime import datetime
import hashlib
import os
def generate_file_id(filename: str) -> str:
    """Generates a unique file ID using the filename and the current timestamp."""
    timestamp = datetime.now().isoformat()
    original_string = f"{filename}-{timestamp}"
    hash_object = hashlib.sha256(original_string.encode())
    return hash_object.hexdigest()

async def save_image(image: UploadFile):
    contents = await image.read()
    unique_id = generate_file_id(image.filename)
    file_path = f"./images/{unique_id + "." + image.filename.split(".")[-1]} "
    with open(file_path, 'wb') as f:
        f.write(contents)
    return unique_id

def get_image_path(image_id: str):
    for file_name in os.listdir("images"):
        # Check if the filename without extension matches
        if os.path.splitext(file_name)[0] == image_id:
            # Create the full file path
            return os.path.join("images", file_name)

    
