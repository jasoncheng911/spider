from urllib import request
import re

class Spider():
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.6gbvhfcbkbn'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\S\s]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        count = 0
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            names = re.findall('[^\\s]*',name[0])
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':names[73], 'number':number}
            anchors.append(anchor)
            print(anchors[count])
            count+=1
            print("\n")
            # break

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
        self.__refine(anchors)



spider = Spider()
spider.go()
