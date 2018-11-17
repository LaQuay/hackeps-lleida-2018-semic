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


def get_OK_TODO():
    return list(["<div>Bienvenidos a la web de <span>SEMIC</span></div>",
                 "<div>Bienvenidos a la web de <span>SEMIC</span></div>"])


def get_FAIL_HTML_TODO():
    return list(["<div>Bienvenidos a la web de <span>SEMIC</span></div>",
                 "<!-- TODO: Move this to an external JS file -->",
                 "<div>Bienvenidos a la web de <span>SEMIC</div></span>"])


def get_FAIL_JS_TODO():
    return list(["$(function(){",
                 "// TODO: Mode this to an external JS file",
                 "$('#subscribe_button').click(function() {"])


def get_OK_blank_url():
    return list([
        "<p style=\"font-size:10px;\" ><strong>Finalidades</strong>: Enviarle ... electrónicos. <strong>Legitimación</strong>: Consentimiento del interesado. <strong>Destinatarios</strong>: Las previstas legalmente. <strong>Derechos</strong>: Puede, suprimir sus datos y demás derechos en <a href=\"mailto:lopd@semic.es\">lopd@semic.es</a>, como se explica en la Política de Privacidad. <strong>Información Adicional</strong>: Puede ampliar la información en el enlace de <a href=\"https://www.semic.es/es/aviso-legal\">Avisos Legales</a></p>"])


def get_FAIL_blank_url():
    return list([
        "<p style=\"font-size:10px;\" ><strong>Finalidades</strong>: Enviarle ... electrónicos. <strong>Legitimación</strong>: Consentimiento del interesado. <strong>Destinatarios</strong>: Las previstas legalmente. <strong>Derechos</strong>: Puede, suprimir sus datos y demás derechos en <a href=\"mailto:lopd@semic.es\">lopd@semic.es</a>, como se explica en la Política de Privacidad. <strong>Información Adicional</strong>: Puede ampliar la información en el enlace de <a href=\"https://www.notsemic.es/es/aviso-legal\">Avisos Legales</a></p>"])


def get_OK_URL():
    return list(["<a href=\"https://www.semic.es/es\">",
                 "<a href=\"/es/soluciones/proveedor-de-tecnologia\">"])


def get_FAIL_URL():
    return list(["<a href=\"https://www.semic.es/es/aviso-legalnoexiste\">",
                 "<a href=\"/es/aviso-legalnoexiste2\">"])
