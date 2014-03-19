import urllib2, string, re, sys
import urllib

# regex returns match result for every group mark by '(' and ')'
# eg, ((a)b) will return (res for ((a)b), res for (a))

def dl_img(url, min_size, outdir):
    try:
        img = urllib2.urlopen(url)
        size = img.info()['content-length']
        if string.atoi(size) > min_size:
            filename = url[url.rindex('/')+1:]
            f = open(outdir + '/' + filename, 'wb')
            f.write(img.read())
            f.close()
            print 'Saved ' + filename + ' in ' + outdir
        else:
            print 'Ignore ' + filename
        img.close()
    except Exception,e:
        print 'Download error: ', e ,url

def analysis(url):
    html = urllib2.urlopen(url)
    regex = r'src="(http\S*?\.(gif|jpg|jpeg|png|bmp))"'
    img_re = re.compile(regex)
    imgset = re.findall(img_re, html.read())
    imgs = list(set(imgset))
    html.close()
    return imgs

def main():
    lu = 2
    wallp = 3
    url = 'http://tu.acfun.tv/picture/index.aspx?channelId=%d&pageNo=%d'
    for i in range(2, 124):
        imgs = analysis(url % (wallp, i))
        for img in imgs:
            dl_img(img[0], 10000, 'wallp')
    print 'Done.'
    f = open('Download_Complete', 'wb')
##    f.write('Done')
    f.close()
##    url = 'http://tu.acfun.tv/picture/index.aspx?channelId=2&pageNo=6'
##    url2 = 'http://tu.acfun.tv/picture/view.aspx?pictureId=6775'
##    url22 = 'src="http://imgsrc.acfun.tv/uploadimg/2014/0107/0000004332.jpeg"'
##    imgs = analysis(url)
##    
##    print imgs[0:3]
if __name__ == '__main__':
    main()
