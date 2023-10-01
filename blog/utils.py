from django.utils.text import slugify

def format_tag(tag):
    tag = slugify(tag)
    tag = tag.replace("-", "")
    tag = "#" + tag
    return tag

def format_body(body):

    body = body.split("</p>")[0]
    body = body.replace('<p class="mb-4 text-gray-700">', '')
    body = body.split(" ")[:18]
    body = " ".join(body).strip(".") + " ..."
    return body