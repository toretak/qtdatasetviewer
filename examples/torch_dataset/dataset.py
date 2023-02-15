# ! python3
# -*- encoding: utf-8 -*-
# mypy: ignore-errors

from __future__ import annotations, generator_stop

from pathlib import Path

import albumentations as A
import numpy as np
from albumentations.pytorch.transforms import ToTensorV2
from PIL import Image
from torch.utils.data import Dataset

Image.MAX_IMAGE_PIXELS = None
RESIZE_PARAM = 640


class SampleDataset(Dataset):
    def __init__(self, files, mode="train"):
        self.files = files
        self._mode = mode
        self._transforms = {
            "train": A.Compose(
                [
                    A.Resize(RESIZE_PARAM, RESIZE_PARAM),
                    A.ShiftScaleRotate(
                        shift_limit=0.2,
                        scale_limit=0.2,
                        rotate_limit=30,
                        p=0.5,
                    ),
                    A.RGBShift(
                        r_shift_limit=25,
                        g_shift_limit=25,
                        b_shift_limit=25,
                        p=0.5,
                    ),
                    A.RandomBrightnessContrast(
                        brightness_limit=0.3, contrast_limit=0.3, p=0.5
                    ),
                    ToTensorV2(),
                ]
            ),
            "val": A.Compose(
                [A.Resize(RESIZE_PARAM, RESIZE_PARAM), ToTensorV2()]
            ),
            "test": A.Compose(
                [A.Resize(RESIZE_PARAM, RESIZE_PARAM), ToTensorV2()]
            ),
        }

    def __get_image(self, image_path: Path) -> np.array:
        image = Image.open(image_path)
        return np.array(image)

    def get_image_and_mask(self, file):
        return self.__get_image(file)

    def __getitem__(self, idx: int):
        raw_sample = self.files[idx]
        image = mask = self.get_image_and_mask(raw_sample)
        mask = mask.astype(np.float32) / 255
        mask[mask > 0.1] = 1.0
        transformed = self._transforms[self._mode](image=image, mask=mask)
        image = transformed["image"]
        mask = transformed["mask"][None, :]
        return image, mask

    def __len__(self):
        return len(self.files)

    def get_mode(self):
        return self._mode

    def __str__(self):
        return self._mode + " SampleDataset"
