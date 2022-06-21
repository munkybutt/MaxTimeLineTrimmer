from pymxs import runtime as mxRt
from Qt import QtWidgets
from Qt import QtGui
from typing import Union


def get_max_version() -> int:

	return mxRt.MaxVersion()[0]


def get_max_main_window() -> Union[None, QtWidgets.QMainWindow]:

	if get_max_version() == 24000:

		from qtmax import GetQMaxMainWindow
		return GetQMaxMainWindow()


def get_native_time_slider():
	for child in get_max_main_window().children():
		if child.objectName() == "TimeSlider":
			return child

def clear_old_time_line_trimmer():
	for child in get_native_time_slider().children()[5].children():
		if child.objectName() == "TimeLineTrimmerWidget":
			child.setParent(None)
			del child

if __name__ == "__main__":

	clear_old_time_line_trimmer()
	# nts = get_native_time_slider()
	# w = nts.children()[5]
	# p = w.palette()
	# p.setColor(QtGui.QPalette.Background, QtCore.Qt.red)
	# w.setAutoFillBackground(True)
	# w.setPalette(p)


