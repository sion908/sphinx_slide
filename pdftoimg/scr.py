# import os
from pathlib import Path
from pdf2image import convert_from_path

# poppler/binを環境変数PATHに追加する
# poppler_dir = Path(__file__).parent.absolute() / "poppler/Library/bin"
# os.environ["PATH"] += os.pathsep + str(poppler_dir)

pdf_path = Path("./pdf/R061120_FG紹介.pdf")
image_dir = Path("./img")

# PDFファイルを画像に変換
pages = convert_from_path(pdf_path, dpi=150)
if len(pages) > 1:
    for i, page in enumerate(pages):
        file_name = pdf_path.stem + "_{:02d}".format(i + 1) + ".jpeg"
        image_path = image_dir / file_name
        # JPEGで保存
        page.save(str(image_path), "JPEG")
else:
    file_name = pdf_path.stem + ".jpeg"
    image_path = image_dir / file_name
    # JPEGで保存
    pages[0].save(str(image_path), "JPEG")
