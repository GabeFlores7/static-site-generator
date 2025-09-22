import unittest

from markdown_to_html import markdown_to_html_node, text_to_children

class TestMarkdownToHTML(unittest.TestCase):
# 6 Tests for 'markdown_to_html_node'; 1 test for each blocktype
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_heading(self):
        md = "### A <b>bold</b> claim? No, it's **bold** and _italic_ with `code`"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html, 
            "<div><h3>A <b>bold</b> claim? No, it's <b>bold</b> and <i>italic</i> with <code>code</code></h3></div>"
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = "> Roses are **red**\n> Violets are _blue_\n> I forgot what to write after the **second line**"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote><p>Roses are <b>red</b> Violets are <i>blue</i> I forgot what to write after the <b>second line</b></p></blockquote></div>",
        )
    
    def test_ulist(self):
        md = """
- **Item 1**
- _Item 2_
- Item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li><b>Item 1</b></li><li><i>Item 2</i></li><li>Item 3</li></ul></div>",
        )

    def test_olist(self):
        md = """
1. **Item 1**
2. _Item 2_
3. Item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ol><li><b>Item 1</b></li><li><i>Item 2</i></li><li>Item 3</li></ol></div>",
        )