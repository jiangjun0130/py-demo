from urllib import request

class Spider():
    url = 'https://www.panda.tv/cate/lol'
    def __fetch_content(self):
        response = request.urlopen(self.__class__.url)
        htmls = response.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        pass

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(self, htmls)
        return htmls

spider = Spider()
htmls = spider.go()
print(htmls)