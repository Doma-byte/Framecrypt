import os
import zipfile

# Unzipping zip file
def extract_password_protected_zip(zip_file_name, password):
    try:
        with zipfile.ZipFile(zip_file_name, "r") as zip_file:
            output_dir = "decoded_files"
            if not os.path.exists(output_dir):
                os.makedir(output_dir)
            zip_file.extractall(pwd=password.encode(), path=output_dir)
        print("Password-protected ZIP file successfully extracted!")
        os.remove(zip_file_name)
    except zipfile.BadZipFile as e:
        print(f"Error: The ZIP file is corrupted or not in the correct format: {str(e)}")
    except RuntimeError as e:
        print(f"Error: Incorrect password or unable to decrypt the ZIP file: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
