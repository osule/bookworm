def slugify(title):
    return title.lower().replace(' ', '-')


def slugify_with_date_now(title, now):
    return "{}-{}".format(slugify(title), now.date().isoformat())
