import urllib
import urllib.request
import urllib.parse


def read_text():
    quotes = open(r"movie_quotes.txt")# Add the actual path that the movie_quotes.txt is located (e.g. C:\**\**\**\movie_quotes.txt)
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    final_url = "http://www.wdylike.appspot.com/?q="+urllib.parse.quote(text_to_check)# The wdylike website checks for curse words.
    #For example, if I give the url http://www.wdylike.appspot.com/?q=shit, is going to return true (a curse word exists).
    #print(final_url)
    connection = urllib.request.urlopen(final_url)#Open the url
    output = connection.read().decode('utf-8')#Get the website's output
    #print(output)
    connection.close()

    if "true" in output:
        print ("Profanity Alert!!!")

    if "false" in output:
        print("This doc has no curse words")

read_text()
