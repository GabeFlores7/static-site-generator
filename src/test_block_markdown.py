import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
# 2 Test for 'markdown_to_blocks' function
    def test_markdown_to_blocks(self):
        markdown_text = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(markdown_text)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks2(self):
        markdown_text = """
**This is bolded paragraph**

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)
This is the end of the paragraph, **I suppose**.  





This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)
_Alright I guess we can wrap up the text._ It is getting kinda long.



- This is a list
- with items


1. This too
2. is a list
3. with a couple
4. of items
"""

        blocks = markdown_to_blocks(markdown_text)

        self.assertEqual(
            blocks,
            [
                "**This is bolded paragraph**",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)\nThis is the end of the paragraph, **I suppose**.",
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)\n_Alright I guess we can wrap up the text._ It is getting kinda long.",
                "- This is a list\n- with items",
                "1. This too\n2. is a list\n3. with a couple\n4. of items"
            ],
        )