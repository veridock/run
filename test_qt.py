import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
label = QLabel("If you can see this, PyQt5 is working!")
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)
window.setLayout(layout)
window.setWindowTitle("PyQt5 Test")
window.resize(400, 200)
window.show()
sys.exit(app.exec_())
