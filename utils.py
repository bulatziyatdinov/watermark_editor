import math

from PIL import Image


def resize(image: Image.Image, new_size: tuple[int, int]) -> Image.Image:
    original_width, original_height = image.size
    new_width, new_height = new_size

    image = image.convert('RGBA')

    if image.mode == 'RGBA':
        result_image = Image.new('RGBA', new_size, (0, 0, 0, 0))
    else:
        result_image = Image.new(image.mode, new_size, (0, 0, 0))

    width_ratio = original_width / new_width
    height_ratio = original_height / new_height

    for x_new in range(new_width):
        for y_new in range(new_height):
            x_out = max(0, min(int(round(x_new * width_ratio)), original_width - 1))
            y_out = max(0, min(int(round(y_new * height_ratio)), original_height - 1))

            pixel_color = image.getpixel((x_out, y_out))

            result_image.putpixel((x_new, y_new), pixel_color)

    return result_image


def scale(image: Image.Image, scale_factor: float) -> Image.Image:
    original_width, original_height = image.size

    new_width = max(1, int(original_width * scale_factor))
    new_height = max(1, int(original_height * scale_factor))
    
    result_image = resize(image, (new_width, new_height))

    return result_image


def rotate(image: Image.Image, angle: float) -> Image.Image:
    image = image.convert('RGBA')
    width, height = image.size
    angle_rad = angle * math.pi / 180

    cos_angle = math.cos(angle_rad)
    sin_angle = math.sin(angle_rad)
    new_width = int(abs(width * cos_angle) + abs(height * sin_angle))
    new_height = int(abs(width * sin_angle) + abs(height * cos_angle))

    center_x, center_y = width / 2, height / 2
    new_center_x, new_center_y = new_width / 2, new_height / 2

    result_image = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))

    for x_new in range(new_width):
        for y_new in range(new_height):
            x_shifted = x_new - new_center_x
            y_shifted = y_new - new_center_y

            cos_neg_angle = math.cos(-angle_rad)
            sin_neg_angle = math.sin(-angle_rad)

            x_original = int(round(x_shifted * cos_neg_angle - y_shifted * sin_neg_angle + center_x))
            y_original = int(round(x_shifted * sin_neg_angle + y_shifted * cos_neg_angle + center_y))

            if 0 <= x_original < width and 0 <= y_original < height:
                pixel_color = image.getpixel((x_original, y_original))
                result_image.putpixel((x_new, y_new), pixel_color)
                
    return result_image


def change_alpha(image: Image.Image, opacity_level: int) -> Image.Image:
    result_image = image.copy().convert('RGBA')
    pixels = result_image.load()

    width, height = result_image.size
    opacity_factor = 1 - opacity_level / 100

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            new_a = int(a * opacity_factor)
            pixels[x, y] = (r, g, b, new_a)

    return result_image


def remove_background(image: Image.Image,
                      color_to_remove: tuple[int, int, int] | None = None,
                      color_area: int = 0) -> Image.Image:
    original_width, original_height = image.size
    image_data = image.load()

    if color_to_remove is None:
        color_to_remove = image_data[0, 0][:3]

    result_image = Image.new('RGBA', (original_width, original_height))
    result_image_data = result_image.load()

    for y in range(original_height):
        for x in range(original_width):
            current_pixel = image_data[x, y]
            current_pixel_rgb = current_pixel[:3]

            if (abs(current_pixel_rgb[0] - color_to_remove[0]) <= color_area and
                    abs(current_pixel_rgb[1] - color_to_remove[1]) <= color_area and
                    abs(current_pixel_rgb[2] - color_to_remove[2]) <= color_area):
                result_image_data[x, y] = (0, 0, 0, 0)
            else:
                result_image_data[x, y] = current_pixel
                
    return result_image


def mirror_horizontal(image: Image.Image) -> Image.Image:
    width, height = image.size
    image_data = image.load()

    result_image = Image.new(image.mode, (width, height))
    result_image_data = result_image.load()

    for y in range(height):
        for x in range(width):
            result_image_data[x, y] = image_data[width - 1 - x, y]

    return result_image


def mirror_vertical(image: Image.Image) -> Image.Image:
    width, height = image.size
    image_data = image.load()

    result_image = Image.new(image.mode, (width, height))
    result_image_data = result_image.load()

    for y in range(height):
        for x in range(width):
            result_image_data[x, y] = image_data[x, height - 1 - y]

    return result_image


def blend_images(base_image: Image.Image, overlay_image: Image.Image,
                 overlay_pos: tuple[int, int]) -> Image.Image:
    if base_image.mode != 'RGBA':
        base_image = base_image.convert('RGBA')
    if overlay_image.mode != 'RGBA':
        overlay_image = overlay_image.convert('RGBA')

    base_width, base_height = base_image.size
    overlay_width, overlay_height = overlay_image.size
    overlay_x, overlay_y = overlay_pos

    result_image = Image.new('RGBA', (base_width, base_height))
    result_pixels = result_image.load()
    base_pixels = base_image.load()
    overlay_pixels = overlay_image.load()

    for x in range(base_width):
        for y in range(base_height):
            if overlay_x <= x < overlay_x + overlay_width and overlay_y <= y < overlay_y + overlay_height:
                overlay_x_relative = x - overlay_x
                overlay_y_relative = y - overlay_y

                base_r, base_g, base_b, base_a = base_pixels[x, y]
                overlay_r, overlay_g, overlay_b, overlay_a = (
                    overlay_pixels)[overlay_x_relative, overlay_y_relative]

                alpha_overlay_norm = overlay_a / 255
                alpha_base_norm = base_a / 255

                alpha_out_norm = alpha_overlay_norm + alpha_base_norm * (1 - alpha_overlay_norm)
                alpha_out = int(alpha_out_norm * 255)

                if alpha_out > 0:
                    r_out = int((overlay_r * alpha_overlay_norm * 255 + base_r * alpha_base_norm *
                                 (1 - alpha_overlay_norm) * 255) / (alpha_out_norm * 255))
                    g_out = int((overlay_g * alpha_overlay_norm * 255 + base_g * alpha_base_norm *
                                 (1 - alpha_overlay_norm) * 255) / (alpha_out_norm * 255))
                    b_out = int((overlay_b * alpha_overlay_norm * 255 + base_b * alpha_base_norm *
                                 ( 1 - alpha_overlay_norm) * 255) / (alpha_out_norm * 255))

                    r_out = max(0, min(255, r_out))
                    g_out = max(0, min(255, g_out))
                    b_out = max(0, min(255, b_out))
                else:
                    r_out, g_out, b_out = 0, 0, 0

                result_pixels[x, y] = (r_out, g_out, b_out, alpha_out)
            else:
                result_pixels[x, y] = base_pixels[x, y]

    return result_image


def fill_image(base_image: Image.Image, sign_image: Image.Image) -> Image.Image:
    base_width, base_height = base_image.size
    sign_width, sign_height = sign_image.size
    sign_image = sign_image.convert('RGBA')

    result_image = base_image.copy()

    num_signs_x = (base_width + sign_width - 1) // sign_width
    num_signs_y = (base_height + sign_height - 1) // sign_height

    for i in range(num_signs_x):
        for j in range(num_signs_y):
            pos = (i * sign_width, j * sign_height)
            result_image.paste(sign_image, pos, sign_image)

    return result_image
