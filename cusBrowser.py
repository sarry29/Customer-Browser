import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# for defining a window we use module
# from PyQt5.QtWidgets import *
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        
        # create browser ;wanna see webview in this place
        # from PyQt5.QtWebEngineWidgets import *
        self.browser = QWebEngineView()
        
        # set url for search engine ; it will as for QUrl fomrat 
        # QUrl fomrat = use (from PyQt5.QtCore import *)
        self.browser.setUrl(QUrl('http://google.com'))
        
        # for loading self.browser (link) in our window 
        self.setCentralWidget(self.browser)
        
        # Maximize screen
        self.showMaximized()

        # navbar
        # create a toolbar back forward reload
        
        # these 2 statem ent will create a space for navbar
        navBar = QToolBar()
        self.addToolBar(navBar)

        
        # create home button  and name it
        home_btn = QAction('Home', self)
        # giving event it trigger than reload page
        home_btn.triggered.connect(self.navigate_home)
        # add button to navBar
        navBar.addAction(home_btn)

        # create back button  and name it
        back_btn = QAction('Back', self)
        # giving event it trigger than go one link back
        back_btn.triggered.connect(self.browser.back)
        # add button to navBar
        navBar.addAction(back_btn)

        # create forward button  and name it
        fwrd_btn = QAction('Forward', self)
        # giving event it trigger than go one link forward
        fwrd_btn.triggered.connect(self.browser.forward)
        # add button to navBar
        navBar.addAction(fwrd_btn)

        # create reload button  and name it
        re_btn = QAction('Reload', self)
        # giving event it trigger than reload page
        re_btn.triggered.connect(self.browser.reload)
        # add button to navBar
        navBar.addAction(re_btn)


        # add search bar 
        self.url_bar = QLineEdit()
        # when return press then connect navigate_url which return url connect to 
        self.url_bar.returnPressed.connect(self.navigate_url)
        navBar.addWidget(self.url_bar)

        #  if url changes ; set url  in  url_bar  in which page you are in
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))


    def navigate_url(self):
        # create home button  and name it
        home_btn = QAction('Home', self)
        # giving event it trigger than reload page
        home_btn.triggered.connect(self.navigate_home)
        # add button to navBar
        navBar.addAction(home_btn)
        # fetch data from url_bar as self is instance
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


# create application pass some system argument
app = QApplication(sys.argv)
# write application name
QApplication.setApplicationName('Custom Browser')
# create window from windowclass
window = MainWindow()
# for execute application
app.exec_()