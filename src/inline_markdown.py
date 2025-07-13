from textnode import *
import re

def split_node_delimiter(olds_nodes, delimiter, text_type):
    new_nodes = []
    for node in olds_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter, maxsplit=2)
        # If the delimiter is not valid raise error
        if len(split_text) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        delimiter_text = split_text[1]
        plain_text = split_text[0]
        # If there is text add it to the list
        if len(plain_text) != 0:
            plain_node = TextNode(plain_text, TextType.PLAIN)
            new_nodes.append(plain_node)
        delimiter_node = TextNode(delimiter_text, text_type)
        new_nodes.append(delimiter_node)

        # If there are more delimiters in the text handle them
        if delimiter in split_text[2]:
            unexpected_node = [TextNode(split_text[2], TextType.PLAIN)]
            other_node = split_node_delimiter(unexpected_node, delimiter, text_type)
            new_nodes.extend(other_node)
        else:
            if len(split_text[2]) != 0:
                other_node = TextNode(split_text[2], TextType.PLAIN)
                new_nodes.append(other_node)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

def split_nodes_link(old_nodes):
    new_nodes = []