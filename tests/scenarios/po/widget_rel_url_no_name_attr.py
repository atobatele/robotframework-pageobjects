
import robot.utils.asserts as asserts

from robotpageobjects.page import Page, robot_alias


class WidgetPage(Page):
    url = "/site/index.html"

    @robot_alias("search__name__for")
    def search(self, term):
        self.input_text("q", "search term")
        self.click_element("go")
        return WidgetSearchResultPage()


class WidgetSearchResultPage(Page):

    @robot_alias("__name__should_have_results")
    def should_have_results(self, expected):
        len_results = len(self._find_element("xpath=id('results')/li", False, False))
        asserts.assert_equals(len_results, int(expected), "Unexpected number of results found on %s, got %s, "
                                                         "expected %s" %(
            self.name, len_results, expected))


