"""Extensions that uses the Markdown Python API to extend functionality"""

from . import patterns
import markdown

class LinksToEmbedExtension(markdown.Extension):
    def add_inline(self, md, name, klass, re):
        pattern = klass(re)
        pattern.md = md
        pattern.ext = self
        md.inlinePatterns.add(name, pattern, "<reference")

    def extendMarkdown(self, md, md_globals):
        self.add_inline(md, 'vimeo', patterns.Vimeo,
                        r'([^(]|^)http://(www.|)vimeo\.com/(?P<vimeoid>\d+)\S*')
        self.add_inline(md, 'youtube', patterns.Youtube,
                        r'([^(]|^)https?://www\.youtube\.com/watch\?\S*v=(?P<youtubeid>\S[^&/]+)')
        self.add_inline(md, 'youtube_short', patterns.Youtube,
                        r'([^(]|^)https?://youtu\.be/(?P<youtubeid>\S[^?&/]+)?')
