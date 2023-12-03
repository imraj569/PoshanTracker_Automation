import os ,sys 
from time import sleep
from colorama import Fore
import colorama
colorama.init(autoreset=True)
import pandas as pd

def banner():
    os.system("cls")
    print(Fore.BLUE+'''
ʕ•́ᴥ•̀ʔっ                                                                         ʕ•́ᴥ•̀ʔっ ʕ•́ᴥ•̀ʔっ 
██████╗░░█████╗░░██████╗██╗░░██╗░█████╗░███╗░░██╗  ██████╗░░█████╗░████████╗░█████╗░
██╔══██╗██╔══██╗██╔════╝██║░░██║██╔══██╗████╗░██║  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
██████╔╝██║░░██║╚█████╗░███████║███████║██╔██╗██║  ██║░░██║███████║░░░██║░░░███████║
██╔═══╝░██║░░██║░╚═══██╗██╔══██║██╔══██║██║╚████║  ██║░░██║██╔══██║░░░██║░░░██╔══██║
██║░░░░░╚█████╔╝██████╔╝██║░░██║██║░░██║██║░╚███║  ██████╔╝██║░░██║░░░██║░░░██║░░██║
╚═╝░░░░░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

███████╗███╗░░██╗████████╗██████╗░██╗░░░██╗
██╔════╝████╗░██║╚══██╔══╝██╔══██╗╚██╗░██╔╝
█████╗░░██╔██╗██║░░░██║░░░██████╔╝░╚████╔╝░
██╔══╝░░██║╚████║░░░██║░░░██╔══██╗░░╚██╔╝░░
███████╗██║░╚███║░░░██║░░░██║░░██║░░░██║░░░
╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░
          ''')

def starting_up():
    banner( )
    print(Fore.GREEN+"please wait starting up...")
    os.startfile("Database\\poshan_assistance.py")
    sys.exit()

def remove_duplicates(excel_file):
    df = pd.read_excel(excel_file)

    # Find duplicates based on all columns (you can specify specific columns if needed)
    duplicates = df[df.duplicated()]

    # Display the duplicate rows (optional)
    print("Duplicate Rows:")
    print(duplicates)

    # Drop the duplicate rows from the DataFrame
    df.drop_duplicates(inplace=True)

    # Save the cleaned DataFrame back to a new Excel file
    cleaned_excel_file = "cleaned_excel_file.xlsx"  # Replace with your desired output file path
    df.to_excel(cleaned_excel_file, index=False)

    print(f"Cleaned data saved to '{cleaned_excel_file}'")

def options():
    banner()
    print(Fore.BLUE+'''
        [1]Start data entry
        [2]remove duplicates data
          ''')
    query = input("enter query: ")
    if "1" in query:
        starting_up()
    elif "2" in query:
        remove_duplicates("Database\\poshana_data.xlsx")

if __name__ == "__main__":
    options()
