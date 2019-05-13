import os,time
def googleDirector():
    decisionGoogle=2
    while(decisionGoogle!=0):
        print("Enter which tool to open:\n1.Google Search\n2.Google Translator\n3.Google Drive\n4.Google Mail\n5.Google Play Music\n6.Google Docs\n7.Google Alerts\n8.Google Books\n9.Google Analytics\n0.Exit")
        decisionGoogle=int(input())

        if decisionGoogle==1:
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\" www.google.com/search?q="+"+".join(input("Enter the text to search:\n").split()))

        elif decisionGoogle==2:
            print("Opening Google Translator...")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\" https://translate.google.com/")

        elif decisionGoogle==3:
            print("Opening Google Drive")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://www.google.com/drive/")

        elif decisionGoogle==4:
            print("Opening Google Mail(GMAIL)")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://www.google.com/gmail/")

        elif decisionGoogle==5:
            print("Opening Google Play Music")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"   https://play.google.com/music")

        elif decisionGoogle==6:
            print("Opening Google Docs")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\" https://docs.google.com/")

        elif decisionGoogle==7:
            print("Opening Google Alerts")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\" https://www.google.co.in/alerts")

        elif decisionGoogle==8:
            print("Opening Google Books")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"   https://books.google.co.in/")

        elif decisionGoogle==9:
            print("Opening Google Analytics")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://analytics.google.com/analytics/web/")

        elif decisionGoogle==0:
            print("\nReturning to Main Menu\n")

def socialMediaDirector():
    decision=2
    while(decision!=0):
        print("Enter which tool to open:\n1.Whatsapp Web\n2.Facebook\n3.Instagram\n4.Snapchat\n5.Twitter\n0.Exit")
        decision=int(input())

        if decision==1:
            print("Opening Whatsapp Web")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"   https://web.whatsapp.com")

        elif decision==2:
            print("Opening Facebook")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"   https://facebook.com")

        elif decision==3:
            print("Opening Instagram")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://instagram.com")

        elif decision==4:
            print("Opening Snapchat")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://www.snapchat.com/")

        elif decision==5:
            print("Opening Twitter")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://twitter.com/")

        elif decision==0:
            print("\nReturning to Main Menu\n")

def onlineShoppingServices():
    decision=2
    while(decision!=0):
        print("Enter which tool to open:\n1.Amazon\n2.Flipkart\n3.Myntra\n4.Jabong\n5.Snapdeal\n0.Exit")
        decision=int(input())

        if decision==1:
            print("Opening Amazon")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"   https://www.amazon.in/")

        elif decision==2:
            print("Opening Flipkart")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"   https://www.flipkart.com/")

        elif decision==3:
            print("Opening Myntra")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://www.snapdeal.com/")

        elif decision==4:
            print("Opening Jabong")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://www.myntra.com/")

        elif decision==5:
            print("Opening SnapDeal")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://www.snapdeal.com/")

        elif decision==0:
            print("\nReturning to Main Menu\n")

if __name__ == '__main__':
    decision = 1
    while decision!=0:
        print("\nEnter the service to use as per:\n1.Google Services\n2.Social Media Services\n3.Online Shopping Services\n4.Youtube\n5.Wikipedia\n6.rknec.edu\n0.Exit\n")
        decision=int(input())

        if decision==1:
            googleDirector()

        elif decision==2:
            socialMediaDirector()

        elif decision==3:
            print("Opening Online Shopping Services")
            onlineShoppingServices()

        elif decision==4:
            print("Opening YouTube")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://www.youtube.com/")

        elif decision==5:
            print("Opening Wikipedia")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"  https://www.wikipedia.org/")

        elif decision==6:
            print("Opening rknec.edu")
            os.system( "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"   http://rknec.edu/")

        elif decision==0:
            print("\nMade by Vedant Khairnar(Kingsmanvk)\nThank You\n:)")
            time.sleep(3)
