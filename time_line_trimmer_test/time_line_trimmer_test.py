import os
import site
import sys

from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets


def __setup__():

    package_path = os.path.normpath(
        os.path.join(__file__, os.path.pardir, os.path.pardir)
    )
    print(package_path)
    site.addsitedir(package_path)


if __name__ == "__main__":

    __setup__()

    from importlib import reload
    import time_line_trimmer
    from time_line_trimmer import widgets
    from time_line_trimmer import utils

    reload(time_line_trimmer)
    reload(utils)
    reload(widgets)

    tltw = widgets.TimeLineTrimmerWidget()
    tltw.show()
    # tltw.hide()
    # nts = utils.get_native_time_slider()
    # print(nts.children()[5].layout())

    # print(nts.findChildren(QtWidgets.QWidget))
