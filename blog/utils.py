from django.utils.text import slugify

def format_tag(tag):
    tag = slugify(tag)
    tag = tag.replace("-", "")
    tag = "#" + tag
    return tag
