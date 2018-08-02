import unittest
import markdown

from blog_embed.extensions import LinksToEmbedExtension

EXTENSION_REGISTERS = True


class TestMarkdownExtensionRegisters(unittest.TestCase):
    def setUp(self):
        self.markdown = markdown.Markdown()

    # noinspection PyBroadException
    def test_extension_registers(self):
        global EXTENSION_REGISTERS
        try:
            markdown.Markdown(extensions=[LinksToEmbedExtension()])
        except Exception:
            EXTENSION_REGISTERS = False
            self.fail('Cannot register Markdown extension')


@unittest.skipUnless(EXTENSION_REGISTERS, reason='Cannot run tests when extension doesn\'t register')
class TestMarkdownExtension(unittest.TestCase):
    markdown: markdown.Markdown

    def setUp(self):
        self.markdown = markdown.Markdown(extensions=[LinksToEmbedExtension()])

    def test_parses_no_embed(self):
        md_text = 'This is **bold** text, and *italic* text.'
        expected_text = '<p>This is <strong>bold</strong> text, and <em>italic</em> text.</p>'
        actual_text = self.markdown.convert(md_text)
        self.assertEqual(actual_text, expected_text)

    def test_parses_embed(self):
        md_text = 'text: https://www.youtube.com/watch?v=7Ijd_iN9Blk'
        expected_text = '<p>text:<div class="video-container">\n<iframe allow="autoplay; encrypted-media" ' \
                        'allowfullscreen="true" frameborder="0" height="720" ' \
                        'src="//www.youtube.com/embed/7Ijd_iN9Blk" ' \
                        'width="1280"></iframe>\n</div>\n</p>'
        actual_text = self.markdown.convert(md_text)
        self.assertEqual(actual_text, expected_text)
