import re
import datetime

import requests

from Stack import Stack
import samples

# Initialize vars
file_input = "reto3"
file_input_ext = file_input + ".html"
input_file = "./input/" + file_input + ".html"
output_file = "./output/" + file_input + "_output.txt"
errors = False

# Read files
file_input = open(input_file, "r").read()
file_input_lines = open(input_file, "r").readlines()
file_output = open(output_file, "w")


def check_not_html_wrong_anidation(file):
    print("HTML anidation... ")

    # file = samples.get_OK_html_nesting()
    # file = samples.get_FAIL_html_nesting()

    s = Stack()
    sN = Stack()

    for i, line in enumerate(file):
        file[i] = (line
                   .replace('<', ' <')
                   .replace('>', '> '))

    tags = []
    for line in file:
        for word in line.split():
            if re.search('<\S+>', word):
                tags.append(word)
    open_tags = [w for w in tags if "/" not in w]
    close_tags = [w for w in tags if "/" in w]

    for i, line in enumerate(file):
        for w in line.split():
            if w in open_tags:
                s.push(w)
                sN.push(i)
            elif not s.is_empty() and (w in close_tags) and (w.replace('/', '') == s.peek()):
                s.pop()
                sN.pop()

    if not s.is_empty():
        file_output.write("Line " + str(sN.peek() + 1) + ": 1 - " + s.peek() + " HTML wrong nesting\n")
        return True

    return False


def check_h1_tags(file):
    print("H1 tags... ")

    # file = samples.get_OK_h1_nesting_1()
    # file = samples.get_OK_h1_nesting_2()
    # file = samples.get_FAIL_h1_nesting_1()
    # file = samples.get_FAIL_h1_nesting_2()

    file = (file.replace('<', ' <')
            .replace('>', '> '))

    errors = False
    inside_section = re.findall('<section[a-zA-Z\-\s\"=]*>.*</section>', file, re.DOTALL)
    for case in inside_section:
        if case.count("<h1>") > case.count("<section>"):
            file_output.write("Line 0: " + "More than one <h1> allowed inside section tags\n")
            errors = True

    inside_article = re.findall('<article[a-zA-Z\-\s\"=]*>.*</article>', file, re.DOTALL)
    for item in inside_article:
        without_section = re.sub('<section>.+</section>', '', item)
        if without_section.count("<h1>") > 1:
            file_output.write("Line 0: " + "More than one <h1> allowed inside article tags\n")
            errors = True

    inside_divs = re.sub('<article[a-zA-Z\-\s\"=]*>.*</article>', '', file, re.DOTALL)
    if inside_divs.count("<h1>") > 1:
        file_output.write("Line 0: " + "More than one <h1> allowed inside div tags\n")
        errors = True

    return errors


def check_analytics(file):
    print("Analytics... ")

    # file = samples.get_OK_google_analytics()
    # file = samples.get_FAIL_google_analytics_1()
    # file = samples.get_FAIL_google_analytics_2()
    # file = samples.get_FAIL_google_analytics_3()
    # file = samples.get_OK_google_tag_manager()
    # file = samples.get_FAIL_google_tag_manager_1()
    # file = samples.get_FAIL_google_tag_manager_2()
    # file = samples.get_FAIL_google_tag_manager_3()

    # Check Google Analytics
    google_analytics = re.findall(r"(UA-[0-9]{7}-1)", file)

    # Check Tag Manager
    google_tag_manager = re.findall(r"(GTM-[a-zA-Z0-9]{7})", file)

    errors = False
    if google_analytics is None or not google_analytics:
        file_output.write("Line 0: 3 - Google Analytics not found\n")
        errors = True

    if google_tag_manager is None or not google_tag_manager or google_tag_manager == list(["GTM-XXXXXXX"]):
        file_output.write("Line 0: 3 - Google TagManager not found\n")
        errors = True

    return errors


def check_sitemap(file):
    print("Sitemap... ")

    # file = samples.get_OK_sitemap()
    # file = samples.get_FAIL_sitemap()

    if "sitemap.xml" not in file:
        file_output.write("Line 0: 4 - Sitemap.xml not found\n")
        return True

    return False


def check_todo(file):
    print("TODO messages... ")

    # file = samples.get_OK_TODO()
    # file = samples.get_FAIL_HTML_TODO()
    # file = samples.get_FAIL_JS_TODO()

    errors = False
    for i, line in enumerate(file):
        if "<!-- TODO:" in line:
            file_output.write("Line " + str(i + 1) + ": 5 - TODO found in HTML code\n")
            errors = True

        if "/* TODO:" in line:
            file_output.write("Line " + str(i + 1) + ": 5 - TODO found in JS code\n")
            errors = True

        if "// TODO:" in line:
            file_output.write("Line " + str(i + 1) + ": 5 - TODO found in JS code\n")
            errors = True

    return errors


def check_blank_in_external_urls(file):
    print("URL externals... ")

    # file = samples.get_OK_blank_url()
    # file = samples.get_FAIL_blank_url()

    errors = False
    for i, line in enumerate(file):
        result = re.findall('<a(.*?)>', line)
        for match in result:
            match = match.replace("'", "\"")

            if 'href=' not in match:
                continue

            if 'href="tel:' in match:
                continue

            if 'href=""' in match:
                continue

            if 'href="#' in match:
                continue

            if 'href="/' in match:
                continue

            if 'mailto' in match:
                continue

            if "www.semic.es" not in match and "target=\"_blank\"" not in match:
                file_output.write("Line " + str(i + 1) + ": 6 - target='_blank' not found\n")
                errors = True

    return errors


def check_js(file):
    print("JS... ")

    count = 0
    for i, line in enumerate(file):
        result = re.findall('<script(.*?)>', line)
        for match in result:
            match = match.replace("'", "\"")
            if "type=\"text/javascript\"" in match:
                count += 1

    if count > 5:
        file_output.write("Line 0: 7 - More than 5 .js scripts\n")
        return True

    return False


def check_css(file):
    print("CSS... ")

    count = 0
    for i, line in enumerate(file):
        result = re.findall('<link(.*?)>', line)
        for match in result:
            match = match.replace("'", "\"")
            if "rel=\"stylesheet\"" in match:
                count += 1

    if count > 5:
        file_output.write("Line 0: 7 - More than 5 .css scripts\n")
        return True

    return False


def check_links_404(file):
    print("CHECK URLs 404... ")

    # file = samples.get_OK_URL()
    # file = samples.get_FAIL_URL()

    errors = False
    for i, line in enumerate(file):
        result = re.findall('<a(.*?)>', line)
        for match in result:
            match = match.replace("'", "\"").strip()

            if 'href=' not in match:
                continue

            if 'href="tel:' in match:
                continue

            if 'href=""' in match:
                continue

            # La ruta # es sobre el html ya existente por tanto no dara 404
            if 'href="#' in match:
                continue

            if 'mailto' in match:
                continue

            url = re.findall('href="(.*?)"', match)[0]

            if 'href="/' in match:
                url = "https://www.semic.es" + url

            print("CHECK URLs: " + url)
            r = requests.get(url)
            status_code = r.status_code

            if status_code == 404:
                file_output.write("Line " + str(i + 1) + ": 9 - URL returning 404 NOT FOUND " + url + "\n")
                errors = True

    return errors


if __name__ == "__main__":
    print("Tercer reto\n")

    now = datetime.datetime.now()

    file_output.write("File: " + file_input_ext + "\n")
    file_output.write("Date: " + now.strftime("%Y-%m-%d") + "\n")
    file_output.write("List of errors:" + "\n")

    if check_not_html_wrong_anidation(file_input_lines.copy()):
        print(" HTML TAGS with ERRORS")
        errors = True

    if check_h1_tags(file_input):
        print(" H1 TAGS ERRORS")
        errors = True

    if check_analytics(file_input):
        print(" ANALYTICS ERROR")
        errors = True

    if check_sitemap(file_input):
        print(" SITEMAP ERRORS")
        errors = True

    if check_todo(file_input_lines):
        print(" TODO ERRORS")
        errors = True

    if check_blank_in_external_urls(file_input_lines):
        print(" BLANK in EXTERNAL ERRORS")
        errors = True

    # Consideramos 'cargar js' como la carga de <script type='text/javascript'>
    if check_js(file_input_lines):
        print(" JS FAILS - ERRORS")
        errors = True

    # Consideramos 'cargar css' como la carga de <link rel="stylesheet">
    if check_css(file_input_lines):
        print(" CSS FAILS - ERRORS")
        errors = True

    # Long test as it checks more than 150 sites
    if check_links_404(file_input_lines):
        print(" SOME LINK IS 404 - ERRORS")
        errors = True
