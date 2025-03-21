import re

class FontTranslator:
    def __init__(self):
        normal_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        mono_chars = "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉" \
                     "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣" \
                     "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
        
        if len(normal_chars) != len(mono_chars):
            raise ValueError("Character mappings must have the same length!")
        
        self.monospace_math = str.maketrans(normal_chars, mono_chars)

    def translate(self, text: str) -> str:
        placeholders = {}
        placeholder_index = 0

        def store_placeholder(match):
            nonlocal placeholder_index
            key = f"¤¤¤{placeholder_index}¤¤¤"
            placeholders[key] = match.group(0)
            placeholder_index += 1
            return key

        # Replace HTML and Markdown tags with placeholders
        temp_text = re.sub(r"<[^>]+>", store_placeholder, text)
        temp_text = re.sub(r"(\*{1,2}.*?\*{1,2}|_.*?_|\uE001.*?\uE001\uE001.*?\uE001)", store_placeholder, temp_text)

        # Convert normal text while preserving placeholders
        translated_text = temp_text.translate(self.monospace_math)

        # Restore placeholders
        for key, original in placeholders.items():
            translated_text = translated_text.replace(key, original)

        return translated_text

# Example Usage
translator = FontTranslator()
input_text = "This is <b>bold</b> and *italic* text with a [link](https://example.com)!"
translated_text = translator.translate(input_text)
print(translated_text)