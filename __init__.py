"""
This extensions tests some cache or variable reference issue?
"""

from albert import *

md_iid = "0.5"
md_version = "1.2"
# md_id = "cache"
md_name = "CacheTest"
md_description = "looking for a issue"
md_license = "MIT"
md_url = "https://url.com/to/upstream/sources/and/maybe/issues"
md_maintainers = "@bierchermüesli"


class Plugin(QueryHandler):
    def id(self):
        return md_id

    def name(self):
        return md_name

    def description(self):
        return md_description

    def initialize(self):
        info('initialize')

    def finalize(self):
        info('finalize')

    def debug(self,i):
        debug('debug '+i)


    def handleQuery(self, query):
        
        items=[]
        list = ["foo","bar","bazen"]

        for i in list:

            debug("add item "+i)

            items.append(Item(
                id=md_id,
                text=i,
                subtext="Item is: "+i+" ID: "+ str(id(i)),
                icon= ['xdg:folder'],
                actions=[
                    Action(
                        id="notify"+i,
                        text="Send '{}' to Tray".format(i),
                        callable=lambda: sendTrayNotification(i,i+" ID: "+ str(id(i)))),
                    Action("logging","ConsoleLog "+i,lambda: self.debug(i)),
                    Action(
                        id="copy "+i,
                        text="Copy "+i,
                        callable=lambda: setClipboardText(text=i))
                    ]                   
            ))

        query.add(items)

        # del(i)
        # i = "whatever"     
        # two = "two"

        # query.add(Item(
        #     id="something different",
        #     text=i,
        #     subtext="Item is: "+i+" ID: "+ str(id(i)),
        #     icon=["xdg:computer"],
        #     actions=[
        #         Action(
        #                 id="notify"+i,
        #                 text="Send '{}' to Tray".format(i),
        #                 callable=lambda: sendTrayNotification(i,i+" ID: "+ str(id(i)))),
        #         Action(
        #                 id="notify"+two,
        #                 text="Send '{}' to Tray".format(two),
        #                 callable=lambda: sendTrayNotification(two,two+" ID: "+ str(id(two)))),   
        #         Action(
        #         "logging",
        #         "ConsoleLog",
        #         lambda: self.debug(i)
        #     )]
        # ))