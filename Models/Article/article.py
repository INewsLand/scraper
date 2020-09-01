class Article(object):
    def __init__(self, title,subtitle, imgs, content, author, date, time):
        self.title = title
        self.subtitle = subtitle
        self.images = imgs
        self.content = content
        self.author = author
        self.date = date
        self.time = time
    
    def get_images(self):
        return self.images

    def __str__(self):
        article = f"""
        *************** ARTICLE ***************
        [+] Title : {self.title}
        [+] Subtitle : {self.subtitle}
        [+] Date : {self.date}
        [+] Time : {self.time}
        [+] Authors : {str(self.author)}
        [+] Images : {str(self.images)}
        [+] Content : \n {self.content}
        """
        return article
