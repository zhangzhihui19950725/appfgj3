#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from appium import webdriver
import sys
import os.path



# driver = None
desired_caps = {}
url = None


def get_device_info(device_info_filepath):
    if not os.path.exists(device_info_filepath):
        print("输入的设备信息文件不存在：%s" % device_info_filepath)
        sys.exit(0)

    fp = open(device_info_filepath)
    infos = fp.readlines()

    global desired_caps
    global url

    for info in infos:
        key, value = info.strip().split('||')
        if 'url' not in key:
            desired_caps[key] = value
        else:
            url = value
    # print("设备参数化信息：%s" %desired_caps)
    # print("配置的appium url参数地址：%s" %url)
    return (url, desired_caps)


'''


url, desired_caps = get_device_info('device_info_file.txt')
print(url, desired_caps)

get_device_info('device_info_file.txt')
device = webdriver.Remote(url, desired_caps)

'''