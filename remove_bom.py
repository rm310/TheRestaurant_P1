filepath = 'locale/uz/LC_MESSAGES/django.po'

with open(filepath, 'rb') as f:
    content = f.read()

# Удаляем BOM, если есть
BOM = b'\xef\xbb\xbf'
if content.startswith(BOM):
    content = content[len(BOM):]

with open(filepath, 'wb') as f:
    f.write(content)

print("BOM удалён.")
