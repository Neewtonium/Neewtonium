import os
from pypdf import PdfReader, PdfWriter
from colorama import Fore, Style, init

# Initialize colorama for CLI colors
init(autoreset=True)

def encrypt_pdf(pdf_path):
    try:
        print(Fore.CYAN + "\n🔒 PDF Encryption Mode")
        print(Fore.CYAN + "-----------------------------------")

        password = input(Fore.WHITE + "Set a password for the PDF: ").strip()
        if not password:
            print(Fore.RED + "❌ Password cannot be empty! Aborting.")
            return

        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(pdf_path, "wb") as file:
            writer.write(file)

        print(Fore.GREEN + "✅ PDF is now password-protected!")

    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")

def decrypt_pdf(pdf_path):
    try:
        print(Fore.CYAN + "\n🔓 PDF Decryption Mode")
        print(Fore.CYAN + "-----------------------------------")

        password = input(Fore.WHITE + "Enter the PDF password: ").strip()

        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        if reader.decrypt(password):
            for page in reader.pages:
                writer.add_page(page)

            with open(pdf_path, "wb") as file:
                writer.write(file)

            print(Fore.GREEN + "✅ PDF successfully decrypted! Password removed.")
        else:
            print(Fore.RED + "❌ Incorrect password! Access denied.")

    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")

def main():
    print(Fore.CYAN + "\n📜 Simple PDF Protection Tool")
    print(Fore.CYAN + "-----------------------------------")
    pdf_path = input(Fore.WHITE + "Enter the PDF file path: ").strip()

    if not os.path.exists(pdf_path):
        print(Fore.RED + "❌ Error: File not found!")
        return

    print(Fore.YELLOW + "\n[1] Encrypt PDF")
    print(Fore.YELLOW + "[2] Decrypt PDF")
    choice = input(Fore.WHITE + "Select an option: ").strip()

    if choice == "1":
        encrypt_pdf(pdf_path)
    elif choice == "2":
        decrypt_pdf(pdf_path)
    else:
        print(Fore.RED + "❌ Invalid option!")

if __name__ == "__main__":
    main()