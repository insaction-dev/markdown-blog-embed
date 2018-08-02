"""Extensions that uses the Markdown Python API to extend functionality"""

from . import patterns
import markdown

RE_YT_SHORT = r'([^(]|^)https?://youtu\.be/(?P<youtubeid>\S[^?&/]+)?'

RE_YOUTUBE = r'([^(]|^)https?://www\.youtube\.com/watch\?\S*v=(?P<youtubeid>\S[^&/]+)'

RE_VIMEO = r'(?:[^(]|^)https?://(?:www\.)?vimeo\.com/(?:video)?/(?P<vimeoid>\d+)\S*'


class LinksToEmbedExtension(markdown.Extension):
    def add_inline(self, md, name, klass, re):
        pattern = klass(re)
        pattern.md = md
        pattern.ext = self
        md.inlinePatterns.add(name, pattern, "<reference")

    def extendMarkdown(self, md, md_globals):
        self.add_inline(md, 'vimeo', patterns.Vimeo,
                        RE_VIMEO)
        self.add_inline(md, 'youtube', patterns.Youtube,
                        RE_YOUTUBE)
        self.add_inline(md, 'youtube_short', patterns.Youtube,
                        RE_YT_SHORT)
