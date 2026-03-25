import sys
import webbrowser

urls = {
    "*PMF1SV+": ["q", "w"],
    "*PMF1SV": ["e", "r"],
    "*FMF1SV+": ["t", "y"],
    "*FMF1SV": ["u", "i"]
}
labels = {
    "*PMF1SV+": "  - Vanilla+ Production Server",
    "*PMF1SV": "  - Vanilla Production Server",
    "*FMF1SV+": "  - Vanilla+ Friends Server",
    "*FMF1SV": "  - Vanilla Friends Server"
}  # production(P)/friends(F), bedrock(B)/java(J)/multiple(M), floodgate(F)/none(N), #, server(S)/world(W), vanilla(V)/vanilla+(V+)/Modded(M)/not vanilla(P)

def start():
    if ask_yes_no("Is this DEV(y) or DOWNLOAD(n)"):
        open_websites_DEV()
    else:
        open_websites_DOWNLOAD()

def open_websites_DEV():
    print("Welcome To The Server Dashboard! ")
    print("Here Are The Packs You Can Choose From: ")
    for code, label in labels.items():
        print(f"{label}  {code}")
    category = input("Which Pack Would You Like To Download? \nEnter the PACK code (e.g. *PMF1SV+): ").strip()
    if category in urls:
        total = len(urls[category])
        count = 0
        for url in urls[category]:
            count += 1
            print(f"[{count}/{total}]  Loading URL: ", url)  
        count = 0
        
        if ask_yes_no("Would you like to continue with opening the URLs?"):
            print("\nContinuing...\n")
            for url in urls[category]:
                count += 1
                print(f"[{count}/{total}]  Opening: ", url)  
                #webbrowser.open(url)
            exit()
        else:
            print("\nCanceling...\n")
            if ask_yes_no("Would you like to retry(y) or exit(n)?"):
                open_websites_DEV()
            else:    
                exit()
    else:
        print("Invalid category. Please try again.")
        open_websites_DEV()

def open_websites_DOWNLOAD():
    print("Welcome To The Server Dashboard! ")
    print("Here Are The Packs You Can Choose From: ")
    for code, label in labels.items():
        print(f"{label}  {code}")
    category = input("Which Pack Would You Like To Download? \nEnter the PACK code (e.g. *PMF1SV+): ").strip()
    if category in urls:
        total = len(urls[category])
        count = 0
        for url in urls[category]:
            count += 1
            print(f"[{count}/{total}]  Loading URL: ", url)  
        count = 0
        
        if ask_yes_no("Would you like to continue with opening the URLs?"):
            print("\nContinuing...\n")
            for url in urls[category]:
                count += 1
                print(f"[{count}/{total}]  Opening: ", url)  
                webbrowser.open(url)
            exit()
        else:
            print("\nCanceling...\n")
            if ask_yes_no("Would you like to retry(y) or exit(n)?"):
                open_websites_DEV()
            else:    
                exit()
    else:
        print("Invalid category. Please try again.")
        open_websites_DEV()


def ask_yes_no(prompt):
    """
    Prompts the user for a yes/no answer until a valid input is received.
    Returns True for 'yes' or 'y', False for 'no' or 'n'.
    """
    while True:
        # Get user input and convert to lowercase for easier comparison
        user_response = input(prompt + " [Y/N]: ").strip().lower()

        if user_response in ['y', 'yes']:
            return True
        elif user_response in ['n', 'no']:
            return False
        else:
            # Inform the user of invalid input and loop again
            print("Invalid input. Please answer with yes or no.")


if __name__ == '__main__':
    start()
