# import base64
#
# from cryptography.fernet import Fernet
# import yaml
#
#
# # Generate a key for encryption. This key should be kept secret.
# # You can generate a key once and store it securely.
# def generate_key():
#     return Fernet.generate_key()
#
#
# # Encrypt data using the key
# def encrypt_data(data, key):
#     cipher_suite = Fernet(key)
#     encrypted_data = cipher_suite.encrypt(data.encode())
#     return encrypted_data
#
#
# # Decrypt data using the key
# def decrypt_data(encrypted_data, key):
#     cipher_suite = Fernet(key)
#     decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
#     return decrypted_data
#
#
# # Read YAML file
# def read_yaml_file(file_path):
#     with open(file_path, 'r') as file:
#         return yaml.safe_load(file)
#
#
# # Write YAML file
# def write_yaml_file(data, file_path):
#     with open(file_path, 'w') as file:
#         yaml.dump(data, file, default_flow_style=False)
#
#
# # Example usage
# def main():
#     # Load your YAML file containing credentials
#     yaml_file_path = '/home/marmik/projects/live-projects/usa-273-pre-processing/src/configs/db_creds.yml'
#     credentials = read_yaml_file(yaml_file_path)
#
#     # Generate a key (Keep this key safe)
#     key = generate_key()
#     print(key)
#
#     # Encrypt credentials
#     encrypted_credentials = {}
#     for key_, value in credentials.items():
#         encrypted_value = encrypt_data(str(value), key)
#         encrypted_credentials[key_] = encrypted_value
#
#     # Write encrypted credentials to a new file
#     encrypted_yaml_file_path = '/home/marmik/projects/live-projects/usa-273-pre-processing/src/configs/encrypted_credentials.yaml'
#     write_yaml_file(encrypted_credentials, encrypted_yaml_file_path)
#
#     # Example of how to decrypt and use credentials
#     decrypted_credentials = {}
#     for key_, value in encrypted_credentials.items():
#         decrypted_value = decrypt_data(value, key)
#         decrypted_credentials[key_] = decrypted_value
#
#     print("Decrypted credentials:", decrypted_credentials)
#
#
# if __name__ == "__main__":
#     main()
