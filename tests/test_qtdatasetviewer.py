from qtdatasetviewer.qt_dataset_viewer import QtDatasetViewer


def test_qtdatasetviewer_blank_init():
    v = QtDatasetViewer()

    assert isinstance(v, QtDatasetViewer)
