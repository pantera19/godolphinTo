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
import time

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


class DeleteHandler(base.BaseHandler):
    def post(self):
        self.write(json.dumps({'code': 0}, default=CJsonEncoder.default))


class ImageHandler(base.BaseHandler):
    def get(self, d, f):
        ty = self.get_argument('type', 'ori')
        img = Image.open('/'.join([self.application.CP.get('picture', 'domain'), d, f]))

        mimetype = self.get_mime_type(f)

        ext = ".jpg"
        if format == "PNG":
            ext = ".png"
        elif format == "GIF":
            ext = ".gif"

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
        img.save(out, format=mimetype.split('/')[-1])
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

    def get_mime_type(self, filename):  # filename 文件路径

        # 返回文件路径后缀名
        filename_type = os.path.splitext(filename)[1][1:]
        type_list = {
            'html'   : 'text/html',
            'htm'    : 'text/html',
            'shtml'  : 'text/html',
            'css'    : 'text/css',
            'xml'    : 'text/xml',
            'gif'    : 'image/gif',
            'jpeg'   : 'image/jpeg',
            'jpg'    : 'image/jpeg',
            'js'     : 'application/x-javascript',
            'atom'   : 'application/atom+xml',
            'rss'    : 'application/rss+xml',
            'mml'    : 'text/mathml',
            'txt'    : 'text/plain',
            'jad'    : 'text/vnd.sun.j2me.app-descriptor',
            'wml'    : 'text/vnd.wap.wml',
            'htc'    : 'text/x-component',
            'png'    : 'image/png',
            'tif'    : 'image/tiff',
            'tiff'   : 'image/tiff',
            'wbmp'   : 'image/vnd.wap.wbmp',
            'ico'    : 'image/x-icon',
            'jng'    : 'image/x-jng',
            'bmp'    : 'image/x-ms-bmp',
            'svg'    : 'image/svg+xml',
            'svgz'   : 'image/svg+xml',
            'webp'   : 'image/webp',
            'jar'    : 'application/java-archive',
            'war'    : 'application/java-archive',
            'ear'    : 'application/java-archive',
            'hqx'    : 'application/mac-binhex40',
            'doc'    : 'application/msword',
            'pdf'    : 'application/pdf',
            'ps'     : 'application/postscript',
            'eps'    : 'application/postscript',
            'ai'     : 'application/postscript',
            'rtf'    : 'application/rtf',
            'xls'    : 'application/vnd.ms-excel',
            'ppt'    : 'application/vnd.ms-powerpoint',
            'wmlc'   : 'application/vnd.wap.wmlc',
            'kml'    : 'application/vnd.google-earth.kml+xml',
            'kmz'    : 'application/vnd.google-earth.kmz',
            '7z'     : 'application/x-7z-compressed',
            'cco'    : 'application/x-cocoa',
            'jardiff': 'application/x-java-archive-diff',
            'jnlp'   : 'application/x-java-jnlp-file',
            'run'    : 'application/x-makeself',
            'pl'     : 'application/x-perl',
            'pm'     : 'application/x-perl',
            'prc'    : 'application/x-pilot',
            'pdb'    : 'application/x-pilot',
            'rar'    : 'application/x-rar-compressed',
            'rpm'    : 'application/x-redhat-package-manager',
            'sea'    : 'application/x-sea',
            'swf'    : 'application/x-shockwave-flash',
            'sit'    : 'application/x-stuffit',
            'tcl'    : 'application/x-tcl',
            'tk'     : 'application/x-tcl',
            'der'    : 'application/x-x509-ca-cert',
            'pem'    : 'application/x-x509-ca-cert',
            'crt'    : 'application/x-x509-ca-cert',
            'xpi'    : 'application/x-xpinstall',
            'xhtml'  : 'application/xhtml+xml',
            'zip'    : 'application/zip',
            'bin'    : 'application/octet-stream',
            'exe'    : 'application/octet-stream',
            'dll'    : 'application/octet-stream',
            'deb'    : 'application/octet-stream',
            'dmg'    : 'application/octet-stream',
            'eot'    : 'application/octet-stream',
            'iso'    : 'application/octet-stream',
            'img'    : 'application/octet-stream',
            'msi'    : 'application/octet-stream',
            'msp'    : 'application/octet-stream',
            'msm'    : 'application/octet-stream',
            'mid'    : 'audio/midi',
            'midi'   : 'audio/midi',
            'kar'    : 'audio/midi',
            'mp3'    : 'audio/mpeg',
            'ogg'    : 'audio/ogg',
            'm4a'    : 'audio/x-m4a',
            'ra'     : 'audio/x-realaudio',
            '3gpp'   : 'video/3gpp',
            '3gp'    : 'video/3gpp',
            'mp4'    : 'video/mp4',
            'mpeg'   : 'video/mpeg',
            'mpg'    : 'video/mpeg',
            'mov'    : 'video/quicktime',
            'webm'   : 'video/webm',
            'flv'    : 'video/x-flv',
            'm4v'    : 'video/x-m4v',
            'mng'    : 'video/x-mng',
            'asx'    : 'video/x-ms-asf',
            'asf'    : 'video/x-ms-asf',
            'wmv'    : 'video/x-ms-wmv',
            'avi'    : 'video/x-msvideo'
        }
        # 判断数据中是否有该后缀名的 key
        if (filename_type in type_list.keys()):
            return type_list[filename_type]
        else:
            return ''


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
