from KinoLife import settings


def Kinolife(request):
    """ context processor for the site templates """
    print(request.user)
    return {
            'site_name': settings.SITE_NAME,
            #'meta_keywords': settings.META_KEYWORDS,
            #'meta_description': settings.META_DESCRIPTION,
            'request': request,
            }