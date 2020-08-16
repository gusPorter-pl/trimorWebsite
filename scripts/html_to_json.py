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
        if tag_contents[-1] == '>':
            # Tag has no parameters
            if tag_contents[1] == '/':
                # Tag is closing tag
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
        if tag_contents[-1] == '>':
            # Tag has no parameters
            tag = tag_contents[1: -1]
        else:
            tag = tag_contents[1: ]
        info = line[start_closing_tag + 1: end_opening_tag]
        return tag, info

    current_tag = ""
    key_tag = ""
    info_dict = {}
    header_tags = ("h2", "h3", "h4")
    info_tags = ("p", "li")
    span_last = False
    for line in input_list:
        if line[0] == '<':
            if line[1] == '/':
                # End tag
                current_tag = ""
                tag = get_tag(line)
                # print("End tag:", tag)
            else:
                right_index = line.find('>')
                if right_index == len(line) - 1:
                    # Line has only tag
                    tag = get_tag(line)
                    if tag in info_tags:
                        current_tag = (tag)
                    # print("   Start tag:", tag)
                else:
                    # Line has tag and info
                    tag, info = get_tag_and_info(line)
                    # print("   Tag ({}) and info ({})".format(tag, info))
                    if tag == "title":
                        info_dict[tag] = info
                    elif tag in header_tags:
                        if info[0] == '<':
                            tag, info = get_tag_and_info(info)
                        key_tag = info
                    elif tag == "span":
                        span_tag, span_info = get_tag_and_info(line)
                        inner_tag, inner_info = get_tag_and_info(span_info)
                        span_last = True
                        if key_tag not in info_dict:
                            info_dict[key_tag] = inner_info
                        else:
                            info_dict[key_tag] += " " + inner_info
                    elif tag == "li":
                        li_tag, li_info = get_tag_and_info(line)
                        if key_tag not in info_dict:
                            info_dict[key_tag] = li_info
                        else:
                            info_dict[key_tag] += "\n" + li_info
        else:
            # This line has text on it
            key_tag = key_tag if key_tag != "" else "Description"
            if key_tag not in info_dict:
                info_dict[key_tag] = line
            else:
                if span_last:
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
    del info_dict["title"]
    with open(filename, 'r') as json_file:
        json_obj = json.load(json_file)
        json_obj[article_type][page] = info_dict

    with open(filename, 'w') as outfile:
        json.dump(json_obj, outfile, indent=3)

def main():
    article_type = "lore"
    article = "holidays"
    filename = "../html/{}/{}.html".format(article_type, article)
    try:
        html_list = get_html(filename)
        info_dict = html_list_to_dictionary(html_list)
        write_json(info_dict, article_type)
    except FileNotFoundError:
        print("This file does not exist.")

main()