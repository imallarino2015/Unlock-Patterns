from PIL import Image,ImageDraw

def createImage(imagePath,pattern):
    imgWidth,imgHeight=256,256
    colCount,rowCount=3,3
    r=10

    endPoints=[]
    for x in range(rowCount):
        for y in range(colCount):
            endPoints.append((int(imgHeight / (colCount + 1) * (y + 1)), int(imgWidth / (rowCount + 1) * (x + 1))))

    img=Image.new("RGB", (imgWidth,imgHeight))
    draw = ImageDraw.Draw(img)

    for pX, pY in endPoints:
        draw.ellipse(
            (
                (pX - r, pY - r),
                (pX + r, pY + r)
            ),
            fill="white"
        )

    iter=0
    while iter<len(pattern)-1:
        draw.line(endPoints[pattern[iter]]+endPoints[pattern[iter+1]],fill="white",width=r)
        iter+=1

    img.save(imagePath)
    pass