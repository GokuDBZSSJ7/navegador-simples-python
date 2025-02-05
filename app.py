import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QPalette, QColor

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Browser")
        self.setGeometry(100, 100, 1200, 800)
        
        self.set_gx_theme()
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.navbar = QHBoxLayout()
        self.layout.addLayout(self.navbar)
        
        self.back_btn = QPushButton("⬅")
        self.back_btn.clicked.connect(self.go_back)
        self.navbar.addWidget(self.back_btn)
        
        self.forward_btn = QPushButton("➡")
        self.forward_btn.clicked.connect(self.go_forward)
        self.navbar.addWidget(self.forward_btn)
        
        self.reload_btn = QPushButton("🔄")
        self.reload_btn.clicked.connect(self.reload_page)
        self.navbar.addWidget(self.reload_btn)
        
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Digite a URL ou pesquise no Google...")
        self.url_bar.returnPressed.connect(self.load_url)
        self.navbar.addWidget(self.url_bar)
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.layout.addWidget(self.browser)
        
        self.apply_styles()
        
    def set_gx_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(20, 20, 20))  
        palette.setColor(QPalette.ColorRole.WindowText, QColor(200, 0, 200)) 
        palette.setColor(QPalette.ColorRole.Base, QColor(30, 30, 30))  
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 0, 0))  
        palette.setColor(QPalette.ColorRole.Button, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(255, 0, 0)) 
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        
        self.setPalette(palette)
        
    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #141414;
                border-radius: 10px;
            }
            QPushButton {
                background-color: #ff004d;
                color: white;
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #ff3355;
            }
            QPushButton:pressed {
                background-color: #990033;
            }
            QLineEdit {
                background-color: #1a1a1a;
                color: #ff004d;
                border: 2px solid #ff004d;
                border-radius: 10px;
                padding: 5px;
                font-size: 16px;
            }
        """)
    
    def load_url(self):
        url = self.url_bar.text().strip()
        if not url:
            return  
        
        if "." in url or url.startswith("http"):
            if not url.startswith("http"):
                url = "https://" + url
        else:
            url = f"https://www.google.com/search?q={url.replace(' ', '+')}"
        
        self.browser.setUrl(QUrl(url))
    
    def go_back(self):
        self.browser.back()
    
    def go_forward(self):
        self.browser.forward()
    
    def reload_page(self):
        self.browser.reload()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec())
