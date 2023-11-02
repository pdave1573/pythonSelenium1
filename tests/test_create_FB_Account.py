import time
from commonMethods import common
from conftest import getDriver

class Test_001_AccountPage:
    page = "https://www.facebook.com/r.php?locale=en_US&display=page"

    def test_openPage(self, setup):
        print("Opening page..." + self.page)
        common.openBrowser(self, setup, self.page)
        time.sleep(5)
        common.closeBrowser(self, setup)
