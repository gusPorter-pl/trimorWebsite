import json
import sys
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
    pass

def main():
    article_type = get_article_type()
    article = get_article(article_type)
    confirm_correct_options(article_type, article)
    create_file(article_type, article)

if __name__ == "__main__":
    main()