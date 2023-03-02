.. |nbsp| unicode:: U+00A0 .. NO-BREAK SPACE

.. |pic1| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue
.. |pic2| image:: https://img.shields.io/github/license/mashape/apistatus.svg
.. |pic3| image:: https://img.shields.io/badge/code%20style-black-000000.svg
.. |pic4| image:: https://img.shields.io/badge/%20type_checker-mypy-%231674b1?style=flat
.. |pic5| image:: https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey
.. |pic6| image:: https://github.com/toretak/qtdatasetviewer/actions/workflows/testing.yml/badge.svg
.. |pic7| image:: https://img.shields.io/readthedocs/qtdatasetviewer
.. |pic8| image:: https://img.shields.io/pypi/v/qtdatasetviewer

.. _qtdatasetviewer: https://github.com/toretak/qtdatasetviewer/tree/main/qtdatasetviewer
.. _examples: https://github.com/toretak/qtdatasetviewer/tree/main/examples
.. _contribute: https://github.com/toretak/qtdatasetviewer/blob/main/CONTRIBUTING.rst

.. _poetry: https://python-poetry.org/docs/
.. _pip: https://mypy.readthedocs.io/en/stable/config_file.html#the-mypy-configuration-file

.. _bandit: https://bandit.readthedocs.io/en/latest/
.. _black: https://black.readthedocs.io/en/stable/index.html
.. _pytest: https://docs.pytest.org/en/stable/index.html
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/stable/index.html
.. _mypy: https://mypy.readthedocs.io/en/stable/index.html
.. _shields: https://shields.io/
.. _README: https://www.makeareadme.com/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _Read the Docs: https://readthedocs.org/
.. _isort: https://pycqa.github.io/isort/index.html
.. _templates: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates

.. _changelog: https://keepachangelog.com/en/1.0.0/
.. _code of conduct: https://www.contributor-covenant.org/version/1/4/code-of-conduct/

.. _Twitter: https://twitter.com/DataLabBE
.. _website: https://data.research.vub.be/
.. _papers: https://researchportal.vub.be/en/organisations/data-analytics-laboratory/publications/

.. _repo: https://github.com/toretak/qtdatasetviewer

.. _Dynamic versioning: https://pypi.org/project/poetry-dynamic-versioning/


qtdatasetviewer
==========

|pic2| |nbsp| |pic5| |nbsp| |pic1| |nbsp| |pic8|

|pic6| |nbsp| |pic7| |nbsp| |pic3| |nbsp| |pic4|

This module is for debugging ML projects. It is PyQt5 based viewer for torch.utils.dataset.
The `qtdatasetviewer`_ folder contains the python module, and we have some `examples`_.

As best practices are always changing, and people have different experiences, we encourage you to `contribute`_ to this project!



Installation
------------

Use the package manager `pip`_ to install ``qtdatasetviewer`` from PyPi.

.. code-block:: bash

    pip install qtdatasetviewer

For development install, see `contribute`_.

TODO
-----

* Tests


Usage
-----


.. code-block:: python


    from glob import glob
    from dataset import SampleDataset

    from PIL import Image
    from qtdatasetviewer.abstract_convert_to_pil import AbstractConvertToPil
    from qtdatasetviewer.qt_dataset_viewer import run_qt_dataset_viewer

    import torchvision.transforms as T


    class Convert(AbstractConvertToPil):

        def convert(self, item) -> Image:
            image, mask = item
            transform = T.ToPILImage()
            return transform(image)


    if __name__ == '__main__':
        dataset = SampleDataset(files=glob('data/*.*'))
        run_qt_dataset_viewer(Convert(dataset))


Disclaimer
----------

The package and the code is provided "as-is" and there is NO WARRANTY of any kind. 
Use it only if the content and output files make sense to you.


Acknowledgements
----------------

Based on this `repo`_
