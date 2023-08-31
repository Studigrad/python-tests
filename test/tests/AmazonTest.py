from TestInit import TestInit
from AmazonPage import AmazonPage


class AmazonTest(TestInit):
    def test_checkHeader(self):
        new_tab = AmazonPage(self.getDriver())
        new_tab.goToAmazon()

        assert new_tab.getTitleField().is_displayed()
        assert new_tab.getDeliverText().is_displayed()
        assert new_tab.getSearchInput().is_displayed()
        assert new_tab.getSearchBtn().is_displayed()
        assert new_tab.getLanguageSelect().is_displayed()
        assert new_tab.getLoginField().is_displayed()
        assert new_tab.getNavOrders().is_displayed()
        assert new_tab.getShoppingCart().is_displayed()


