"""Various patterns that extract links and expose HTML embeds or otherwise dynamic content"""

from . import mixins
from markdown import inlinepatterns

class Vimeo(inlinepatterns.Pattern, mixins.IFrameRendererMixin):
    def handleMatch(self, m):
        url = '//player.vimeo.com/video/%s' % m.group('vimeoid')
        return self.render(url, '1280', '720')


class Youtube(inlinepatterns.Pattern, mixins.IFrameRendererMixin):
    def handleMatch(self, m):
        url = '//www.youtube.com/embed/%s' % m.group('youtubeid')
        return self.render(url, '1280', '720')
