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
from qtdatasetviewer.qt_dataset_viewer import run_qt_dataset_viewer


class Convert(AbstractConvertToPil):
    def convert(self, item) -> Image:
        image, mask = item
        transform = T.ToPILImage()
        return transform(image)


if __name__ == "__main__":
    dataset = SampleDataset(files=glob("data/*.*"))
    run_qt_dataset_viewer(Convert(dataset))
