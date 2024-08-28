from fontTools.ttLib import TTFont

def convert_font(input_file, output_file):
    # Load the input font file
    font = TTFont(input_file)
    
    # Access the character mapping table (cmap)
    cmap_table = font['cmap']
    cmap = cmap_table.getBestCmap()
    
    # Create a new character mapping table
    new_cmap = {}
    
    # Character replacement logic
    for char_code in cmap:
        next_char_code = char_code + 1
        while True:
            if next_char_code in cmap:
                new_cmap[char_code] = chr(next_char_code)
                print(f"Replaced character {chr(char_code)} with {chr(next_char_code)}")
                break
            else:
                next_char_code += 1
                if next_char_code > 0xFFFF:  # Avoid infinite loop
                    print(f"Skipped character {chr(char_code)}")
                    break
    
    # Update the cmap table with the new cmap
    valid_cmap = {k: v for k, v in new_cmap.items() if v in font.getReverseGlyphMap()}
    cmap_table.tables[0].cmap = valid_cmap
    cmap_table.tables[0].compile(font)  # Ensure the cmap table is compiled correctly
    
    # Save the font
    font.save(output_file)
    print(f"Font saved to {output_file}")

# Example call
convert_font('input.otf', 'output.otf')
