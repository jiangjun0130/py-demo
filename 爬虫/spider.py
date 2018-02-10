"""
    This is a module
"""
from urllib import request
import re
import ssl

class Spider():
    """
        This is a class
    """
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        """
            This is a method
        :return:
        """
        context = ssl._create_unverified_context()

        # This is 
        response = request.urlopen(self.__class__.url, context=context)
        htmls = response.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(self.__class__.root_pattern,htmls)
        anchors = []
        for html in root_html:
            name = re.findall(self.__class__.name_pattern,html)
            number = re.findall(self.__class__.number_pattern,html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number':anchor['number'][0]
        }
        return map(l,anchors)

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank' + str(rank + 1) + ':' + anchors[rank]['name'] + '---' + anchors[rank]['number'])


    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__show(anchors)
        self.__show(anchors)
        return anchors

spider = Spider()
anchors = spider.go()