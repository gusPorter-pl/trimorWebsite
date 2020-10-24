import json
import sys
import os
"""
Creates an empty html file
"""

def get_article_type():
    
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

    articles = get_available_articles()
    article_types = list(articles.keys())
    print("\nWhich type of article would you like to create?")
    i = get_index(article_types)
    return article_types[i]

def get_article(article_type):
    return input("\nEnter article name for type \"{}\" (Remember to capitalise): ".format(article_type))

def confirm_correct_options(article_type, article, pc=None):
    acceptable_types = ("y", "n", "Y", "N")
    if pc is None:
        show_text = "\nIs this the correct article and type? (y/n)\n{}: {} ".format(article_type, article)
    else:
        show_text = "\nIs this the correct article, type, and PC? (y/n)\n{}: {}, {} ".format(article_type, article, pc)
    while True:
        boolean = input(show_text)
        if boolean in acceptable_types:
            break
        else:
            print("Invalid value")
    if boolean == "n" or boolean == "N":
        sys.exit(0)

def create_file(article_type, article):

    def link_to_pc():
        acceptable_types = ("y", "n", "Y", "N")
        while True:
            boolean = input("\nWould you like to add a link to a PC? (y/n) ")
            if boolean in acceptable_types:
                break
            else:
                print("Invalid value")
        return boolean == "y" or boolean == "Y"

    article_filename = spaces_to_hyphens(article)
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
        "         <h5><a href=\"./index.html\">&lt&lt&lt Return to {}</a></h5>\n".format(
                                                                                    article_type.capitalize() if article_type != "npcs" else "NPC's"
                                                                                  ),
        "         \n",
        "      </div>\n",
        "   </body>\n",
        "</html>"
    ]

    if link_to_pc():
        articles = get_available_articles()
        pcs = articles["pcs"]
        i = get_index(tuple(hyphens_to_spaces(pc) for pc in pcs))
        pc_filename = "../pcs/{}.html".format(pcs[i])
        output_text.insert(15, 
            "         <h5><a href=\"{}\">&lt&lt&lt Return to {}</a></h5>\n".format(pc_filename, hyphens_to_spaces(pcs[i]))
        )
        confirm_correct_options(article_type, article, hyphens_to_spaces(pcs[i]))

    if article_type == "other": output_text.pop(14)
    output_file = open(filename, 'w')
    for line in output_text:
        output_file.write(line)
    output_file.close()

def main():
    article_type = get_article_type()
    article = get_article(article_type)
    confirm_correct_options(article_type, article)
    create_file(article_type, article)

def get_available_articles():
    filename = "../html/json/articles.json"
    with open(filename, 'r', encoding="utf-8") as json_file:
        articles = json.load(json_file)
    del articles["maps"]
    return articles

def get_index(a_list):
    for i in range(0, len(a_list)):
        print("{}. {}".format(i + 1, a_list[i]))
    input_str = input("Enter number: ")
    try:
        input_int = int(input_str)
        if input_int <= 0:
            raise IndexError()
        return input_int - 1
    except (ValueError, IndexError):
        print("Invalid value")
        sys.exit(1)

def spaces_to_hyphens(a_str):
    a_str = a_str.lower()
    for i in range(len(a_str)):
        if a_str[i] == " ":
            a_str = a_str[:i] + "-" + a_str[i + 1:]
    return a_str

def hyphens_to_spaces(a_str):
    a_str = a_str.capitalize()
    for i in range(len(a_str)):
        if a_str[i] == "-":
            a_str = a_str[:i] + " " + a_str[i + 1].upper() + a_str[i + 2:]
    return a_str

if __name__ == "__main__":
    main()