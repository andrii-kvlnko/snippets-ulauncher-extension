from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
import json

class JSONRepository:
    def __init__(self, path):
        self.path = path;

    def get_items():
        file = open(filename, 'r')
        content = file.read()
        document = json.loads(content);

        return document["items"]

    __path

class DemoExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        path = extension.preferences['source']
        repository = JSONRepository(path)
        repository_items = repository.get_items()

        result_items = []

        for repository_item in repository_items:
            result_item = ExtensionResultItem(icon='',
                                          name='Item %s' % repository_item,
                                          description='Item description %s' % repository_item,
                                          on_enter=HideWindowAction())
            result_items.append(result_item)

        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()