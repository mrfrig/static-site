import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
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
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and "
            "<code>code</code> here</p></div>",
        )

    def test_headings(self):
        md = """
    # This is a heading

    some text

    ## This is an h2

    Hello

    ### This is an h3

    #### This is an h4

    ##### This is an h5

    ###### This is an h6

    ####### This is not a heading

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1><p>some text</p>"
            "<h2>This is an h2</h2><p>Hello</p><h3>This is an h3</h3>"
            "<h4>This is an h4</h4><h5>This is an h5</h5>"
            "<h6>This is an h6</h6><p>####### This is not a heading</p></div>",
            html,
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
            "<div><pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n</code></pre></div>",
            html,
        )

    def test_quotes(self):
        md = """
    > This is a quote text
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote text</blockquote></div>",
            html,
        )

    def test_unordered_list(self):
        md = """
    - list item 1
    - list item 2
    - list item 3
    this should be added to list item 3
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul>"
            "<li>list item 1</li>"
            "<li>list item 2</li>"
            "<li>list item 3    this should be added to list item 3</li>"
            "</ul></div>",
            html,
        )

    def test_ordered_list(self):
        md = """
    1. list item 1
    2. list item 2
    3. list item 3
    this should be added to list item 3
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol>"
            "<li>list item 1</li>"
            "<li>list item 2</li>"
            "<li>list item 3    this should be added to list item 3</li>"
            "</ol></div>",
            html,
        )


if __name__ == "__main__":
    unittest.main()
