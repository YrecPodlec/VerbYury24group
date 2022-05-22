import drawSvg as draw
import random

picture = draw.Drawing(900, 700, origin='center',displayInline=False)

back = draw.Circle(-1, 1, 900, fill='blue')
picture.append(back)

c = draw.Circle(400, 300, 100, fill='DarkOrange')
# c.appendAnim(draw.Animate('fill', '1s', 'yellow;green;blue;orange', calcMode='discrete', repeatCount='indefinite'))
picture.append(c)

cloud = draw.Circle(-300, 200, 50, fill='white')
cloud.appendAnim(draw.Animate('cx', '7s', '-300;300;-300',repeatCount='indefinite'))
picture.append(cloud)
cloud2 = draw.Circle(-200, 210, 50, fill='white')
cloud2.appendAnim(draw.Animate('cx', '7s', '-200;400;-200',repeatCount='indefinite'))
picture.append(cloud2)
cloud3 = draw.Circle(-250, 230, 50, fill='white')
cloud3.appendAnim(draw.Animate('cx', '7s', '-250;350;-250',repeatCount='indefinite'))
picture.append(cloud3)
cloud4= draw.Circle(-250, 200, 50, fill='white')
cloud4.appendAnim(draw.Animate('cx', '7s', '-250;350;-250',repeatCount='indefinite'))
picture.append(cloud4)
picture.append(draw.Lines(-450, -350,
                    450, -350,
                    450, -200,
                    -450, -250,
                    close=False,
            fill='LimeGreen'))
picture.append(draw.Circle(60,-200,70, fill='yellow'))
picture.append(draw.Circle(40,-170,20, fill='white', stroke='black', stroke_width=1))
picture.append(draw.Circle(85,-170,20, fill='white', stroke='black', stroke_width=1))
eye1 = draw.Circle(95,-170,5, fill='black')
eye1.appendAnim(draw.Animate('cx', '1s', '95;80;95',repeatCount='indefinite'))
picture.append(eye1)
eye2 = draw.Circle(50,-170,5, fill='black')
eye2.appendAnim(draw.Animate('cx', '1s', '50;35;50',repeatCount='indefinite'))
picture.append(eye2)
picture.append(eye2)
picture.append(draw.Arc(60,-220,20,170,360,cw=False,
            stroke='red', stroke_width=3, fill='none'))
picture.append(draw.Circle(60,-200,10, fill='red'))
cloud5 = draw.Circle(400, 10, 50, fill='white')
cloud5.appendAnim(draw.Animate('cx', '5s', '400;-400;400',repeatCount='indefinite'))
picture.append(cloud5)
cloud6 = draw.Circle(300, 10, 50, fill='white')
cloud6.appendAnim(draw.Animate('cx', '5s', '300;-500;300',repeatCount='indefinite'))
picture.append(cloud6)
cloud7 = draw.Circle(350, 30, 50, fill='white')
cloud7.appendAnim(draw.Animate('cx', '5s', '350;-450;350',repeatCount='indefinite'))
picture.append(cloud7)
cloud8 = draw.Circle(350, -5, 50, fill='white')
cloud8.appendAnim(draw.Animate('cx', '5s', '350;-450;350',repeatCount='indefinite'))
picture.append(cloud8)
picture