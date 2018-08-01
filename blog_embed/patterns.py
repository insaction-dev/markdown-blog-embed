"""Various patterns that extract links and expose HTML embeds or otherwise dynamic content"""

from .mixins import IFrameRendererMixin
from markdown import inlinepatterns


class Vimeo(inlinepatterns.Pattern, IFrameRendererMixin):
    def handleMatch(self, m):
        url = '//player.vimeo.com/video/%s' % m.group('vimeoid')
        return self.render(url, '1280', '720', extra_attributes=dict(allow='autoplay; encrypted-media'))


class Youtube(inlinepatterns.Pattern, IFrameRendererMixin):
    def handleMatch(self, m):
        url = '//www.youtube.com/embed/%s' % m.group('youtubeid')
        return self.render(url, '1280', '720')
