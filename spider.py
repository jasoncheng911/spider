from urllib import request
import re

class Spider():
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.6gbvhfcbkbn'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\S\s]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'
    count = 0

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        self.count = 0
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
            self.count+=1

        return anchors

    def __refine(self, anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
        }
        return map(l,anchors)

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        print(anchors)
        print("总数: ", self.count)

spider = Spider()
spider.go()
