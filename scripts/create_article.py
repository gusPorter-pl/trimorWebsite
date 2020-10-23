import json
import sys
import os
"""
Creates an empty html file
"""

def get_article_type():

    def get_available_article_types():
        filename = "../html/json/articles.json"
        with open(filename, 'r', encoding="utf-8") as json_file:
            articles = json.load(json_file)
        del articles["maps"]
        return articles
    
    def get_article_type(articles):
        article_types = list(articles.keys())
        for i in range(0, len(article_types)):
            print("{}. {}".format(i + 1, article_types[i]))
        article_type = input("Enter number: ")
        try:
            article_int = int(article_type)
            if article_int <= 0:
                raise IndexError()
            article_type = article_types[article_int - 1]
        except (ValueError, IndexError):
            print("Invalid value")
            sys.exit()
        return article_type

    article_types = get_available_article_types()
    return get_article_type(article_types)

def get_article(article_type):
    return input("\nEnter article name for type \"{}\": ".format(article_type))

def confirm_correct_options(article_type, article):
    acceptable_types = ("y", "n", "Y", "N")
    while True:
        boolean = input("\nIs this the correct article and type? (y/n)\n{}: {} ".format(article_type, article))
        if boolean in acceptable_types:
            break
        else:
            print("Invalid value")
    if boolean == "n" or boolean == "N":
        sys.exit(0)

def create_file(article_type, article):
    # Needs to write to articlesToDo.json, and add file in html {article} folder
    article_filename = article.lower()
    for i in range(len(article)):
        if article_filename[i] == " ":
            article_filename = article_filename[:i] + "-" + article_filename[i + 1:]
    filename = "../html/{}/{}.html".format(article_type, article_filename)
    if os.path.isfile(filename):
        print("\nThis file already exists")
        sys.exit(0)

    output_text = [
        "<!DOCTYPE html>\n",
        "<html>\n",
        "   <head>\n",
        "      <title>{}</title>\n".format(article),
        "      <meta charset=\"UTF-8\">\n",
        "      <link rel=\"stylesheet\" href=\"../../styles/styles.css\" type=\"text/css\"/>\n",
        "   </head>\n",
        "   <body>\n",
        "      <header>\n",
        "         <h1 class=\"body\" style=\"padding: 15px;\">{}</h1>\n".format(article),
        "      </header>\n",
        "      <div class=\"body\">\n",
        "         <img class=\"centre\" src=\"../../images/trimorHeader.png\">\n",
        "         <h5><a href=\"../../index.html\">&lt&lt&lt Return to Contents</a></h5>\n",
        "         <h5><a href=\"./index.html\">&lt&lt&lt Return to ________</a></h5>\n",
        "         \n",
        "      </div>\n",
        "   </body>\n",
        "</html>"
    ]
    output_file = open(filename, 'w')
    for line in output_text:
        output_file.write(line)
    output_file.close()

def main():
    article_type = get_article_type()
    article = get_article(article_type)
    confirm_correct_options(article_type, article)
    create_file(article_type, article)

if __name__ == "__main__":
    main()