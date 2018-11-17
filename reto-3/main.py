import re
import datetime

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

    # file = samples.get_OK_html_anidation()
    # file = samples.get_FAIL_html_anidation()

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
        file_output.write("Line " + str(sN.pop() + 1) + ": 1 - " + s.pop() + " HTML wrong nesting\n")
        return True

    return False


def check_h1_tags(file):
    print("H1 tags... ")


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

        if "// TODO:" in line:
            file_output.write("Line " + str(i + 1) + ": 5 - TODO found in JS code\n")
            errors = True

    return errors


def check_blank_in_external_urls(file):
    print("URL externals... ")


def check_js(file):
    print("JS... ")


def check_css(file):
    print("CSS... ")


def check_links_404(file):
    print("404... ")


if __name__ == "__main__":
    print("Tercer reto\n")

    now = datetime.datetime.now()

    file_output.write("File: " + file_input_ext + "\n")
    file_output.write("Date: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
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

    if check_blank_in_external_urls(file_input):
        print(" BLANK in EXTERNAL ERRORS")
        errors = True

    if check_js(file_input):
        print(" JS FAILS - ERRORS")
        errors = True

    if check_css(file_input):
        print(" CSS FAILS - ERRORS")
        errors = True

    if check_links_404(file_input):
        print(" SOME LINK IS 404 - ERRORS")
        errors = True
