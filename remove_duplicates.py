from colorama import Fore,init
init(autoreset=True)
import pandas as pd
import os

def banner():
    clear_screen()
    print(Fore.RED+"make sure if you do not change"+Fore.GREEN+"\nAnything like file path and file data")

def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def remove_duplicates(excel_file):
    df = pd.read_excel(excel_file)

    # Find duplicates based on all columns (you can specify specific columns if needed)
    duplicates = df[df.duplicated()]

    # Display the duplicate rows (optional)
    print(Fore.CYAN+"Duplicate Rows:")
    print(duplicates)

    # Drop the duplicate rows from the DataFrame
    df.drop_duplicates(inplace=True)

    # Save the cleaned DataFrame back to a new Excel file
    cleaned_excel_file = "cleaned_excel_file.xlsx"  # Replace with your desired output file path
    df.to_excel(cleaned_excel_file, index=False)

    print(Fore.MAGENTA+f"Cleaned data saved to '{cleaned_excel_file}'")

if __name__ == "__main__":
    banner()
    if os.name == 'nt':
        remove_duplicates("poshana_data.xlsx")
    else:
        remove_duplicates("data/data/com.termux/files/home/storage/downloads/poshana_data.xlsx")