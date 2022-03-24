import ffmpeg

supported_formats = [
    'png',
    'jpg',
    'jpeg',
    'bmp',
]


def convert_image(url, output_directory, file_type):
    try:
        ffmpeg.input(url).output(output_directory + '/' + url.split("/")[-1].split(".")[0] + '.jpg').run()
        return True
    except ffmpeg.Error as e:
        print(e.stderr)
        return False