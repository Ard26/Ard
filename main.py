# модули 
from PIL import Image, ImageFilter
from PyQt5.QtWidgets import *
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
# coздание приложения и окна
app = QApplication([])
maim_win = QWidget()
maim_win.setWindowTitle ("")
# виджеты
folder_btn = QPushButton("Папка и Мамка")
img_list = QListWidget ()
pic = QLabel("Фотокарточка из 80-ых")
left_btn = QPushButton("не право")
right_btn = QPushButton("право")
mirror_btn = QPushButton("все наоборот")
sharp_btn = QPushButton("Резко и жеско ")
bw_btn = QPushButton("Чайник/Бидон")
# макет (лэйауты)
layout_1 = QVBoxLayout()
layout_1.addWidget (folder_btn)
layout_1.addWidget (img_list)

layout_2 = QHBoxLayout()
layout_2.addWidget(left_btn)
layout_2.addWidget(right_btn)
layout_2.addWidget(mirror_btn)
layout_2.addWidget(sharp_btn)
layout_2.addWidget(bw_btn)

layout_3 = QVBoxLayout()
layout_3.addWidget(pic)
layout_3.addLayout(layout_2)

layout_4 = QHBoxLayout()
layout_4.addLayout(layout_1, stretch=1)
layout_4.addLayout(layout_3, stretch=5)

maim_win.setLayout(layout_4)
# функционал
workdir = ""
def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extentios):
    result = []
    for f in files:
        for ext in extentios:
            if f.endswith(ext):
                result.append(f)
    return result

def show_filenames_list():
    extentions = [".jpg",".jpeg", ".png", ".bmp", ".gif"]
    choose_workdir()
    img_list.clear()
    filenames = filter(os.listdir(workdir), extentions)
    for filename in filenames:
        img_list.addItem(filename)


class ImageProctssor():
    def __init__(self):
        self.Image = None
        self.dir = None
        self.filename = None
        self/save_dir = "Modified/"

    def load_image(self, dir, filename):
        self.dir = dir
        self.filename = filename
        img_path = os.path.join(dir, filename)
        print()
        print(img_path)
        print()
        self.Image = Image.open(img_path)

        def show_image (self, path):
            picture .hide()
            pix






# жмаканье на кнопочки (подписка на события)
folder_btn.clicked.connect(show_filenames_list)











# запуск приложения 
maim_win.showMaximized()
app.exec()








