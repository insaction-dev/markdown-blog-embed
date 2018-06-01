"""Base mixins to reuse HTML injection code"""
from markdown import util


class HTMLRendererMixin:
    def render(self, *args, **kwargs):
        pass


class minxins.IFrameRendererMixin(HTMLRendererMixin):
    def render(self, url, width, height):
        iframe = util.etree.Element('iframe')
        iframe.set('width', width)
        iframe.set('height', height)
        iframe.set('src', url)
        iframe.set('allowfullscreen', 'true')
        iframe.set('frameborder', '0')

        container = util.etree.Element('div')
        container.set('class', 'video-container')
        container.insert(0, iframe)
        return container
