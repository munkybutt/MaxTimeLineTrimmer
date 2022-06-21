# import nifty.widgets as nifty_widgets

from . import utils
from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets


class HorizontalBaseWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._parent_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self._parent_layout)

    @property
    def parent_layout(self):
        return self._parent_layout


class EdgeBaseButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setObjectName("EdgeBaseButton")
        self.setMaximumWidth(30)
        self.setMinimumWidth(30)
        self._mouse_down = False
        self._start_position = None

    def mousePressEvent(self, event):
        event_button = event.button()
        if event_button == QtCore.Qt.LeftButton:
            if self._mouse_down is False:
                self._mouse_down = True
                self._start_position = self.pos()
                self._current_y = self._start_position.y()
                self._offset = self._start_position - self.parent().mapFromGlobal(QtGui.QCursor.pos())

        elif event_button == QtCore.Qt.RightButton:
            self._mouse_down = False
            if self._start_position:
                self.move(self._start_position)

        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._mouse_down:
            pos = self.parent().mapFromGlobal(QtGui.QCursor.pos()) + self._offset
            pos.setY(self._current_y)
            self.move(pos)

        return super().mouseMoveEvent(event)


class TimeLineBarButton(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()

        self.setObjectName("TimeLineBarButton")


class TimeSliderWidget(HorizontalBaseWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("TimeSliderWidget")
        self.start_button = EdgeBaseButton()
        self.range_button = QtWidgets.QPushButton()
        self.end_button = EdgeBaseButton()
        self.parent_layout.addWidget(self.start_button)
        self.parent_layout.addWidget(self.range_button)
        self.parent_layout.addWidget(self.end_button)


class TimeLineTrimmerWidget(HorizontalBaseWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("TimeLineTrimmerWidget")
        utils.clear_old_time_line_trimmer()
        # native_time_slider = utils.get_native_time_slider()
        # native_time_slider.children()[5].layout().addWidget(self)

        self.time_slider_widget = TimeSliderWidget()
        self.time_display_combobox = QtWidgets.QComboBox()
        self.time_display_combobox.setMaximumWidth(100)
        self.parent_layout.addWidget(self.time_slider_widget)
        self.parent_layout.addWidget(self.time_display_combobox)


if __name__ == "__main__":

    tltw = TimeLineTrimmerWidget()
    # tltw.show()
