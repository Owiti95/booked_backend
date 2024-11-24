# import os
# from dotenv import load_dotenv
# import my_cloudinary_config
# import cloudinary.uploader
# import cloudinary.api

# # Load environment variables from .env
# load_dotenv()

# # Correctly named dictionary with dynamic environment variable substitution
# Cloudinary_config = {
#     "CLOUD_NAME": os.getenv("duljg3j2l"),
#     "API_KEY": os.getenv("926499949357289"),
#     "API_SECRET": os.getenv("2SNBQ5QhU8uywqzZgGHO6tTNCjg"),
# }


# def upload_image(file_path):
#     try:
#         response = cloudinary.uploader.upload(file_path)
#         print("Image URL:", response['secure_url'])
#         return response['secure_url']
#     except Exception as e:
#         print("Error uploading image:", e)
#         return None
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Correctly named dictionary with dynamic environment variable substitution
Cloudinary_config = {
    "CLOUD_NAME": os.getenv("CLOUD_NAME"),
    "API_KEY": os.getenv("API_KEY"),
    "API_SECRET": os.getenv("API_SECRET"),
}
