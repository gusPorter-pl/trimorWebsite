import json
"""
Converts html text to json for searching
"""

def get_html(filename):
    input_file = open(filename, 'r')
    html_text = input_file.read()
    input_file.close()
    html_list = html_text.split("\n")
    html_list = [line.strip() for line in html_list]
    return html_list

def html_list_to_dictionary(input_list):

    def get_tag(line):
        line_contents = line.split()
        tag_contents = line_contents[0]
        if tag_contents[-1] == '>':  # Tag has no parameters
            if tag_contents[1] == '/':  # Tag is closing tag
                tag = tag_contents[2: -1]
            else:
                tag = tag_contents[1: -1]
        else:
            tag = tag_contents[1: ]
        return tag

    def get_tag_and_info(line):
        start_closing_tag = line.find('>')
        end_opening_tag = line.rfind('<')
        tag_contents = line[: start_closing_tag].split()[0]
        if tag_contents[-1] == '>':  # Tag has no parameters
            tag = tag_contents[1: -1]
        else:
            tag = tag_contents[1: ]
        info = line[start_closing_tag + 1: end_opening_tag]
        return tag, info

    key_tag = ""
    info_dict = {}
    header_tags = ("h2", "h3", "h4")
    info_tags = ("p", "li")
    span_last = False
    for line in input_list:
        if line[0] == '<':  # Line is a tag
            if line[1] == '/':  # Line is an end tag
                tag = get_tag(line)
            else:
                right_index = line.find('>')
                if right_index != len(line) - 1:  # Line has tag and info
                    tag, info = get_tag_and_info(line)
                    if tag == "title":
                        info_dict[tag] = info
                    elif tag in header_tags:
                        if info[0] == '<':  # If there is a tag inside the tag
                            tag, info = get_tag_and_info(info)
                        key_tag = info
                    elif tag == "span":  # We want to get the info out of span
                        span_tag, span_info = get_tag_and_info(line)
                        inner_tag, inner_info = get_tag_and_info(span_info)
                        if line[-1] != '>':  # There is more text after span tag
                            inner_info += line[line.rfind('>') + 1: ]
                        span_last = True  # So we know how we add to the dictionary
                        if key_tag not in info_dict:
                            info_dict[key_tag] = inner_info
                        else:
                            info_dict[key_tag] += " " + inner_info
                    elif tag == "li":  # Get the info out of the list item and add it straight to the dictionary
                        li_tag, li_info = get_tag_and_info(line)
                        if key_tag not in info_dict:
                            info_dict[key_tag] = li_info
                        else:
                            info_dict[key_tag] += "\n" + li_info
        else:  # This line has just text on it
            key_tag = key_tag if key_tag != "" else "Description"
            if key_tag not in info_dict:
                info_dict[key_tag] = line
                if span_last:
                    span_last = False
            else:
                if span_last:  # Add the span content without new line
                    info_dict[key_tag] += " " + line
                    span_last = False
                else:
                    info_dict[key_tag] += "\n" + line

    # for key, value in info_dict.items():
    #     print("{}\n{}\n".format(key, value))
    return info_dict

def write_json(info_dict, article_type):
    filename = "./info.json"
    page = info_dict["title"].lower()
    for i in range(len(page)):
        if page[i] == " ":
            page = page[:i] + "-" + page[i + 1:]
    del info_dict["title"]
    with open(filename, 'r') as json_file:
        json_obj = json.load(json_file)
        json_obj[article_type][page] = info_dict

    with open(filename, 'w') as outfile:
        json.dump(json_obj, outfile, indent=3)

def main():
    article_type = "lore"
    article = "holidays-of-trimor"
    filename = "../html/{}/{}.html".format(article_type, article)
    try:
        html_list = get_html(filename)
        info_dict = html_list_to_dictionary(html_list)
        write_json(info_dict, article_type)
        print("Successfully saved {} in {}.".format(article, article_type))
    except FileNotFoundError:
        print("This file does not exist.")

main()