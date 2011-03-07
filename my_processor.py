def ajax_detect(request):
    """
    Templace context processor to detect Ajax requests
    
    The function sets the template variable root_template, which
    indicates which parent-template should be used
    """
    r = "index.html"
    if request.is_ajax():
        r = "ajax.html"
    return { 'root_template' : r }
