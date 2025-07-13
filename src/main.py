from textnode import *
from inline_markdown import *

def main():
    #new_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    node = TextNode("This is how it is `Some code to write` i dont know", TextType.PLAIN)
    node2 = TextNode("This is how it is `Some other code that does stuff` and somehow `we do it again`", TextType.PLAIN)
    listed = [node,node2]
    img_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

    link_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    extracted = extract_markdown_images(img_text)
    for extract in extracted:
        splited = img_text.split("".join(extract))
        print(splited)


main()