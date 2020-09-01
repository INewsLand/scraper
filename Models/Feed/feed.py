class Feed(object):
    def __init__(self, title, img, txt, date , url):
        self.title = title
        self.img = img
        self.content = txt
        self.date = date
        self.url = url

    def __str__(self):
        feed = f"""
        ------------- FEED -------------
        [+] URL : {self.url}
        [+] Title : {self.title}
        [+] Image : {self.img}
        [+] Content : {self.content}
        [+] Date : {self.date}
        """
        return feed

    def get_url(self):
        return self.url