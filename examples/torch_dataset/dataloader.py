# ! python3
# -*- encoding: utf-8 -*-
# mypy: ignore-errors

import sys
from glob import glob

import torchvision.transforms as T
from dataset import SampleDataset
from PIL import Image
from PyQt5.QtWidgets import QApplication

from qtdatasetviewer.abstract_convert_to_pil import AbstractConvertToPil
from qtdatasetviewer.qt_dataset_viewer import QtDatasetViewer


class Convert(AbstractConvertToPil):
    def convert(self, item) -> Image:
        image, mask = item
        transform = T.ToPILImage()
        return transform(image)


if __name__ == "__main__":
    the_app = QApplication(sys.argv)
    dataset = SampleDataset(files=glob("data/*.*"))

    imageViewerApp = QtDatasetViewer(Convert(dataset))

    imageViewerApp.show()
    sys.exit(the_app.exec_())
