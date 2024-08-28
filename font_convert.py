from fontTools.ttLib import TTFont

def convert_font(input_file, output_file):
    font = TTFont(input_file)
    cmap = font['cmap'].tables[0].cmap
    new_cmap = {}

    for char_code in cmap:
        next_char = chr(char_code + 1)
        try:
            glyph_id = font.getGlyphID(next_char)
            new_cmap[char_code] = next_char
        except KeyError:
            pass  # Skip characters that do not have corresponding glyphs

    # Update the cmap table with the new mapping
    font['cmap'].tables[0].cmap.update(new_cmap)
    font.save(output_file)

if __name__ == "__main__":
    input_file = "input.ttf"
    output_file = "output.ttf"
    convert_font(input_file, output_file)
