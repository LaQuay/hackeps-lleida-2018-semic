def get_OK_html_nesting():
    return list(["<div>Bienvenidos a la web de <span>SEMIC</span></div>",
                 "<div>Bienvenidos a la web de <span>SEMIC</span></div>"])


def get_FAIL_html_nesting():
    return list(["<div>Bienvenidos a la web de <span>SEMIC</span></div>",
                 "<div>Bienvenidos a la web de <span>SEMIC</div></span>"])


def get_OK_google_analytics():
    return "window['ga-disable-UA-6091890-1'] = true;"


def get_FAIL_google_analytics_1():
    return "window['ga-disable-UA-6A91890-1'] = true;"


def get_FAIL_google_analytics_2():
    return "window['ga-disable-UA-1-1'] = true;"


def get_FAIL_google_analytics_3():
    return "window[''] = true;"


def get_OK_google_tag_manager():
    return "<noscript><iframe src='https://www.googletagmanager.com/ns.html?id=GTM-MSMTBR3'"


def get_FAIL_google_tag_manager_1():
    return "<noscript><iframe src='https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX'"


def get_FAIL_google_tag_manager_2():
    return "<noscript><iframe src='https://www.googletagmanager.com/ns.html?id=GTM-MSMTR3'"


def get_FAIL_google_tag_manager_3():
    return "<noscript><iframe src='https://www.googletagmanager.com/ns.html?id=GTM-'"


def get_OK_sitemap():
    return "<div>sitemap.xmlBienvenidos a la web de <span>SEMIC</span></div>"


def get_FAIL_sitemap():
    return "<div>Bienvenidos a la web de <span>SEMIC</span></div>"
