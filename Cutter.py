#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

icon_size_list = [
    20,
    60,
    120,
    180,
    76,
    152,
    228,
    167,
    29,
    58,
    87,
    40,
    80,
    120
]

icon_name_list = [
    '20@1x',
    '60@1x',
    '60@2x',
    '60@3x',
    '76@1x',
    '76@2x',
    '76@3x',
    'iPadPro@2x',
    '29@1x',
    '29@2x',
    '29@3x',
    '40@1x',
    '40@2x',
    '40@3x'
]

launch_size_list = [
    [640, 960],
    [640, 1136],
    [750, 1334],
    [768, 1024],
    [1125, 2436],
    [1242, 2208],
    [1536, 2048]
]

launch_name_list = [
    '640x960',
    '640x1136',
    '750x1334',
    '768x1024',
    '1125x2436',
    '1242x2208',
    '1536x2048'
]


def get_org_image(filename):

    return Image.open(filename)


def resize_icons():

    try:

        image = get_org_image('icon.png')
        (width, height) = image.size

        if width != 1024 or height != 1024:
            print('Wrong Icon size, require 1024x1024.')
            return

        for size in icon_size_list:
            result = image.resize((size, size), Image.ANTIALIAS)
            result.save('icon_' + icon_name_list[icon_size_list.index(size)] + '.png')
            print('Complete Icon %sx%s' % (size, size))

        print('Saving Icon complete.')

    except Exception as e:

        print(e)


def resize_launch():

    try:

        image = get_org_image('launch.png')
        (width, height) = image.size

        if width != 2048 or height != 2732:
            print('Wrong LaunchScreen size, require 2048x2732.')
            return

        for size in launch_size_list:

            temp = image.resize((int(width * size[1] / height), size[1]))
            (temp_width, temp_height) = temp.size

            if temp_width != size[0]:
                x = (temp_width - size[0]) / 2
                # fix iPhone X 1125 width
                x = int(x + 0.5)
                w = x + size[0]
                result = temp.crop((x, 0, w, size[1]))
            else:
                result = temp.crop((0, size[0], 0, size[1]))

            result.save('launch_' + launch_name_list[launch_size_list.index(size)] + '.png')
            print('Complete LaunchScreen %sx%s' % (size[0], size[1]))

        print('Saving LaunchScreen complete.')

    except Exception as e:

        print(e)


if __name__ == '__main__':

    resize_icons()
    resize_launch()

    print('Complete.')
