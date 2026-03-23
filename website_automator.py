import sys
import webbrowser

urls = {
    "Vanilla+ Production Server *PMF1SV+" : ["",""]
    "Vanilla Production Server *PMF1SV" : ["",""]
    "Vanilla+ Freinds Server *FMF1SV+" : ["",""]
    "Vanilla Freinds Server *FMF1SV" : ["",""]
} # production(P)/friends(F), bedrock(B)/java(J)/multiple(M), floodgate(F)/none(N), #, server(S)/world(W), vanilla(V)/vanilla+(V+)/Modded(Java only, M)/not vanilla(P)


def open_websites():
    print("Welcome To The Server Dashboard! ")
    print("Here Are The Packs You Can Choose From: ")
    for category in urls:
        print(category)
    category = input("Which Pack Would You Like To Download? ")
    if category in urls:
        for url in urls[category]:
            webbrowser.open(url)
    else:
        print("Invalid category. Please try again.")
        open_websites()
    
open_websites()
