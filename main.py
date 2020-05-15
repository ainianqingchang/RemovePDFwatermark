import fitz
import os


def delete_watermark(src, dst, width=963, height=215):
    doc = fitz.open(src)
    for page in range(doc.pageCount):
        images = doc.getPageImageList(page)
        lpage=doc.loadPage(page)
        sr=lpage.searchFor("书诚教育专营店",hit_max=16)
        # print("这是page："+str(page+1))

        for content in doc[page]._getContents():
            c = doc._getXrefStream(content)
            c = c.replace("/Fm0 Do".encode(), b"")
            print(c)
            # for _, _, width, height, _, _, _, img, _ in images:
            #     if width == width and height == height:
            #         c = c.replace("/Fm0 Do".format(img).encode(), b"")
            doc._updateStream(content, c)
        
        # print("page %s结束"%(page+1,))

    dir = os.path.dirname(dst)
    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(dir)
    doc.save(dst)


SRC = "C:/BaiduYunDownload/银行招聘笔试"
DST = "C:/BaiduYunDownload/银行招聘笔试-处理"

for root, dirs, files in os.walk(SRC):
    for file in files:
        if not file.endswith("pdf"):
            continue
        src = os.path.join(root, file)
        dst = os.path.join(root.replace(SRC, DST), file)
        delete_watermark(src, dst)