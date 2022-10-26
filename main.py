from PIL import Image
import os
import glob


SRC_DIRECTORY = r''
PDF_FILE_NAME = ''
IMAGE_SIZE = (800, 600)
EXTENSION_LIST = ('jpg', 'jpeg', 'png')


def main():
    image_path_list = []
    for extension in EXTENSION_LIST:
        finding_image_path_list = glob.glob(f'{SRC_DIRECTORY}/*.{extension}')
        if finding_image_path_list:
            image_path_list.extend(finding_image_path_list)

    image_list = []

    if image_path_list:
        for index, image_path in enumerate(image_path_list):
            filename = os.path.splitext(os.path.basename(image_path))[0]
            print(f'[{index + 1}/{len(image_path_list)}]: "{filename}"')

            img = Image.open(image_path)
            img.thumbnail(size=IMAGE_SIZE)
            image_list.append(img.convert('RGB'))
            image = image_list[0]
            del image_list[0]
            image.save(os.path.join(SRC_DIRECTORY, f'{PDF_FILE_NAME}.pdf'), save_all=True, append_images=image_list)
    else:
        print(f'Image files matching pattern not found from directory "{SRC_DIRECTORY}"')


if __name__ == '__main__':
    main()
