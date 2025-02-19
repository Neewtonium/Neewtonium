

**🔐 PDF Encryption & Decryption CLI Tool**

A simple command-line tool to encrypt and decrypt PDF files using a password. This tool ensures document security by allowing users to set and remove passwords from PDFs.

**✨ Features**

✅ Encrypt PDFs with a password for security

✅ Decrypt PDFs by removing the password

✅ Simple and interactive CLI interface

✅ Error handling for incorrect passwords and missing files

✅ Uses Python's pypdf and colorama for PDF processing and CLI styling

**🛠️ How It Works**

**1. Encryption:**

The tool reads an existing PDF file.

It asks the user to set a password.

It then encrypts the PDF and overwrites the original file with password protection.




**2. Decryption:**

The tool prompts the user for the correct password.

If the password is correct, it removes the encryption.

The updated PDF replaces the original, now without a password.




**📦 Dependencies**

Ensure you have Python 3 installed, then install the required packages:

`pip install pypdf colorama`

**🚀 Usage**

Run the script in the terminal:

`python pdf_tool.py`

you can also clone it
`git clone` https://github.com/Neewtonium/pdf_encryption

Follow the on-screen instructions to:

*[1] Encrypt a PDF: Set a password to protect the file.*


*[2] Decrypt a PDF: Enter the correct password to remove protection.*



**⚠️ Notes**

The script modifies the original file (no backup). Make a copy before encryption if needed.

Password recovery is not possible if forgotten.


**🏗️ Future Improvements**

🔹 Option to save the encrypted/decrypted PDF as a new file

🔹 Support for batch processing multiple PDFs

🔹 GUI version for a more user-friendly experience

