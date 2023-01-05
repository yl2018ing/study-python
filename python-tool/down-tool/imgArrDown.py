import requests
# 功能：下载数组里的网络地址图片保存到本地
import os
'''
    本代码实现下载一个网络图片地址数组的全部图片
'''

# 卡杰背景图的网络地址
urls = ['https://wx3.sinaimg.cn/mw2000/007cuCaGgy1h4ny8adsqyj30u01uo4af.jpg',
        'https://wx2.sinaimg.cn/mw2000/007cuCaGgy1h4ny8axjigj30u01uogy9.jpg',
        'https://wx2.sinaimg.cn/mw2000/007cuCaGgy1h4ny8bjomdj30u01uodrt.jpg',
        'https://wx3.sinaimg.cn/mw2000/007cuCaGgy1h4ny8cj87nj30u01uok1e.jpg',
        'https://wx2.sinaimg.cn/mw2000/007cuCaGgy1h4ny8d3zt1j30u01uows7.jpg',
        'https://wx2.sinaimg.cn/mw2000/007cuCaGgy1h4ny8ds5u0j30u01uo4ao.jpg',
        'https://wx3.sinaimg.cn/mw2000/007cuCaGgy1h4ny8egeoij30u01uo7gy.jpg',
        'https://wx1.sinaimg.cn/mw2000/007cuCaGgy1h4ny8ey4fbj30u01uo13u.jpg',
        'https://wx4.sinaimg.cn/mw2000/007cuCaGgy1h4rguy7en3j30u01uogwq.jpg',
        'https://wx1.sinaimg.cn/mw2000/007cuCaGgy1h4rguyht6sj30u01uo14p.jpg',
        'https://wx4.sinaimg.cn/mw2000/007cuCaGgy1h4rguyswc2j30u01uoqdi.jpg',
        'https://wx1.sinaimg.cn/mw2000/007cuCaGgy1h4rguz3wluj30u01uo17d.jpg',
        'https://wx4.sinaimg.cn/mw2000/007cuCaGgy1h4rguzihdfj30u01uok37.jpg',
        'https://wx3.sinaimg.cn/mw2000/007cuCaGgy1h4rguzv5pyj30u01uogwc.jpg',
        'https://wx1.sinaimg.cn/mw2000/007cuCaGgy1h4rgv058lgj30u01uoqeg.jpg',
        'https://wx4.sinaimg.cn/mw2000/007cuCaGgy1h4rgv0f6ufj30u01uo16t.jpg',
        'https://wx3.sinaimg.cn/mw2000/007cuCaGgy1h4rgv0rlvoj30u01uotk7.jpg',
        'https://wx1.sinaimg.cn/mw2000/007cuCaGgy1h4rgv1ehmpj30u01uotk1.jpg',
        'https://wx2.sinaimg.cn/mw2000/007cuCaGgy1h4rgv1nrq8j30u01uotj9.jpg',
        'https://wx2.sinaimg.cn/mw2000/007cuCaGgy1h4rgv1y8pqj30u01uon6v.jpg',
        'https://wx1.sinaimg.cn/mw2000/007cuCaGgy1h4rgv27kguj30u01uojzy.jpg',
        'https://wx2.sinaimg.cn/mw2000/007cuCaGgy1h4rgv2hil7j30u01uo49e.jpg',
        'https://wx2.sinaimg.cn/mw2000/007cuCaGgy1h4rgv2r5owj30u01uoalh.jpg',
        'https://wx1.sinaimg.cn/mw2000/007cuCaGgy1h4rgv32mfuj30u01uotjz.jpg']

if __name__ == '__main__':
    save_dirs = 'img'  # 存储文件夹
    a = []
    for i in urls:
        print(i)
        r = requests.get(i)
        r.raise_for_status()
        # 截图图片名称
        # a.append('/static/bgImg/'+i.split('/')[-1])
        # print(i.split('/')[-1])
        # with open(mulu+i.split('/')[-1], 'wb') as f:
        #     f.write(r.content)
        #     f.close()
        print('保存完成')
    print(a)