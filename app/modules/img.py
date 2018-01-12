# -*- coding:utf8 -*-

import base

import os
import json
import stat
from StringIO import StringIO
import hashlib
from PIL import Image
from datetime import date, datetime
import decimal

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


class DeleteHandler(base.BaseHandler):
    def post(self):
        self.write(json.dumps({'code': 0}, default=CJsonEncoder.default))


class ImageHandler(base.BaseHandler):
    def get(self, d, f):
        ty = self.get_argument('ty', 'ori')
        img = Image.open('/'.join([self.application.CP.get('picture', 'domain'), d, f]))

        if ty == 'ori':
            pass
        elif ty == 'thum':
            img = self.resize(img, 500, 0)
        elif ty == 'full':
            img = self.full(img)
        elif ty == 'zfx':
            img = self.crop(img, 300, 300)
        elif ty == '100h':
            img = self.resize(img, 0, 100)
        elif ty == 'wap':
            img = self.crop(img, 400, 250)
        elif ty == 'design_web':
            img = self.resize(img, 0, 600)
        elif ty == 'design_wap':
            img = self.resize(img, 0, 300)

        out = StringIO()
        img.save(out, img.format)
        data = out.getvalue()
        out.close()

        self.write(data)
        self.set_header("Content-Type", "image")
        # self.set_header("Content-Length", img)
        return self.finish()

    def resize(self, im, x, y):
        ori_x, ori_y = im.size
        if 0 == y:  # x或y=0，按比例缩放
            y = int(x * (float(ori_y) / ori_x))
            return im.resize((x, y), Image.ANTIALIAS)
        if 0 == x:
            x = int(y * (float(ori_x) / ori_y))
            return im.resize((x, y), Image.ANTIALIAS)

    def crop(self, im, x, y):  # 先缩放到合适大小，再切图
        ori_x, ori_y = im.size
        if float(x) / y > float(ori_x) / ori_y:  # 要求的尺寸宽，以x为标准
            im = self.resize(im, x, 0)
        else:
            im = self.resize(im, 0, y)
        new_x, new_y = im.size
        start_x = int(new_x / 2 - x / 2)
        start_y = int(new_y / 2 - y / 2)
        area = (start_x, start_y, start_x + x, start_y + y)
        return im.crop(area)

    def full(self, im):  # 填充白色背景
        ori_x, ori_y = im.size

        if ori_x == ori_y:
            return im

        x, y = 0, 0
        if ori_x > ori_y:
            l = ori_x
            y = (ori_x - ori_y) / 2
        else:
            l = ori_y
            x = (ori_y - ori_x) / 2

        try:
            p = Image.new('RGBA', (l, l), (255, 255, 255))
        except:
            p = Image.new('RGB', (l, l), (255, 255, 255))

        p.paste(im, (x, y))
        return p


class UploadHandler(base.BaseHandler):
    def post(self):
        args = dict()
        req = dict(self.request.arguments, **self.request.files)
        for key in req:
            args[key.lower()] = req[key][0]

        if 'file' in args:
            args['filedata'] = args['file']

        filename = args['file']['filename']
        name, ext = filename.rsplit('.', 1)

        data = args['filedata']["body"]
        img = Image.open(StringIO(data))
        w, h = img.size
        now = datetime.now()
        filename = hashlib.md5(str(now)).hexdigest() + '_' + str(w) + '_' + str(h) + '_ori' + '.' + ext

        stub = now.strftime("%Y_%m_%d/") + filename
        self.ensure_path(stub)
        img.save(os.path.join(self.application.CP.get('picture', 'domain'), stub))

        self.write(json.dumps({'imgsrc': '/uploads/' + stub}, default=CJsonEncoder.default))

    def ensure_path(self, path):
        '''path默认应该以root_path开头'''
        path = path.replace(self.application.CP.get('picture', 'domain') + '/', "").strip("/").strip(".")
        current_path = self.application.CP.get('picture', 'domain') + '/'
        for dir in path.split("/")[:-1]:
            current_path += dir + "/"
            if not os.path.exists(current_path):
                os.mkdir(current_path)
                os.chmod(current_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)


class CJsonEncoder:
    @classmethod
    def default(ss, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            raise TypeError('%r is not JSON serializable' % obj)

    @classmethod
    def timestamp(ss, obj):
        if isinstance(obj, datetime):
            return time.mktime(obj.timetuple())
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            raise TypeError('%r is not JSON serializable' % obj)
