import time

import ffmpeg

supported_formats = [
    'png',
    'jpg',
    'jpeg',
    'bmp',
]


def convert_image(url, output_directory, file_type, name=""):
    if name == "":
        name = time.strftime("%Y%m%d-%H%M%S")
    try:
        ffmpeg.input(url).output(output_directory + '/' + name + '.jpg').run()
        return True
    except ffmpeg.Error as e:
        print(e.stderr)
        return False