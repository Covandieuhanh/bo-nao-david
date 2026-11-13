from PIL import Image
import glob, sys
for v in sys.argv[1:]:
    fs = sorted(glob.glob(f'{v}/sl-*.png')); ims = [Image.open(f).convert('RGB') for f in fs]
    w, h = 800, 450
    for part in range(0, len(ims), 4):
        chunk = ims[part:part + 4]; rows = (len(chunk) + 1) // 2
        sheet = Image.new('RGB', (2 * w + 10, rows * (h + 10)), 'white')
        for i, im in enumerate(chunk): sheet.paste(im.resize((w, h)), ((i % 2) * (w + 10), (i // 2) * (h + 10)))
        sheet.save(f'{v}/sheet-{part // 4 + 1}.png')
    print(v, len(ims))
