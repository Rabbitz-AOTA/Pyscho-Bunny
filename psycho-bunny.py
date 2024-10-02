import os
import time
import sys

def print_banner():
    print("""
██████╗ ███████╗██╗   ██╗ ██████╗██╗  ██╗ ██████╗ 
██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝██║  ██║██╔═══██╗
██████╔╝███████╗ ╚████╔╝ ██║     ███████║██║   ██║
██╔═══╝ ╚════██║  ╚██╔╝  ██║     ██╔══██║██║   ██║
██║     ███████║   ██║   ╚██████╗██║  ██║╚██████╔╝
╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝ ╚═════╝ 
                                                  
██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗██╗   ██╗    
██╔══██╗██║   ██║████╗  ██║████╗  ██║╚██╗ ██╔╝    
██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║ ╚████╔╝     
██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║  ╚██╔╝      
██████╔╝╚██████╔╝██║ ╚████║██║ ╚████║   ██║       
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝   ╚═╝  
          

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@#   @@@@@@@@@@@@@@@@@@@@@@@@@@. .@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@     -@@@@@@@@@@@@@@@@@@@@@@.    #@@@@@@@@@@@@@@
@@@@@@@@@@@@@@      .@@@@@@@@@@@@@@@@@@@#      %@@@@@@@@@@@@@@
@@@@@@@@@@@@@@=      .@@@@@@@@@@@@@@@@@=.      @@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@       .@@@@@@@@@@@@@@@=       .@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@:        @@@@@@@@@@@@@+.       @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@.       .@@@@@@@@@@@@        .@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@*        :@@@@@@@@@@        .@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@         %@@@@@@@@:        @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@        ...    .=        =@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@.                      -@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@                     :@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@.               ...*@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@             ..-##-.@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@..==.:=.  .:*#+...   @@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@.#########....  .:.  :@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@.#######.       @@@  -@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@%.:###*.       .@@@ .@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@. -              .@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@%:        . =@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@    :@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#     :@@@@@@@@@@@@@@@@.    .@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@.       .%@@@@@@@@@@@@+       .%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@.            =@@@%.     .      *@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@-*@@@@@@*        ..%@@@@@%-+@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@  ..*@@%:.         ..+@@@-  .-@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@           .@@@@@@@+..         -@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%.      @@@@@@@@@@@@@@@=      .@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@*     @@@@@@@@@@@@@@@@@.     @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@.   %@@@@@@@@@@@@@@@@@@:   *@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


                                                                            
    Psycho Bunny Multi-Virus Toolkit v1.0
    Developed by Rabbitz-AOTA
    """)

def boot_sector_virus():
    print("Launching Boot Sector Virus...")
    # Add code to launch Boot Sector Virus

def web_scripting_virus():
    print("Launching Web Scripting Virus...")
    # Add code to launch Web Scripting Virus

def browser_hijacker():
    print("Launching Browser Hijacker...")
    # Add code to launch Browser Hijacker

def resident_virus():
    print("Launching Resident Virus...")
    # Add code to launch Resident Virus

def direct_action_virus():
    print("Launching Direct Action Virus...")
    # Add code to launch Direct Action Virus

def polymorphic_virus():
    print("Launching Polymorphic Virus...")
    # Add code to launch Polymorphic Virus

def file_infector_virus():
    print("Launching File Infector Virus...")
    # Add code to launch File Infector Virus

def multipartite_virus():
    print("Launching Multipartite Virus...")
    # Add code to launch Multipartite Virus

def main_menu():
    print("Select a virus to launch:")
    print("1. Boot Sector Virus")
    print("2. Web Scripting Virus")
    print("3. Browser Hijacker")
    print("4. Resident Virus")
    print("5. Direct Action Virus")
    print("6. Polymorphic Virus")
    print("7. File Infector Virus")
    print("8. Multipartite Virus")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        boot_sector_virus()
    elif choice == '2':
        web_scripting_virus()
    elif choice == '3':
        browser_hijacker()
    elif choice == '4':
        resident_virus()
    elif choice == '5':
        direct_action_virus()
    elif choice == '6':
        polymorphic_virus()
    elif choice == '7':
        file_infector_virus()
    elif choice == '8':
        multipartite_virus()
    elif choice == '9':
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")

def main():
    print_banner()
    while True:
        main_menu()
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
