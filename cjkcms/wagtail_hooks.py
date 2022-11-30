import mimetypes

from django.templatetags.static import static
from django.http.response import HttpResponse
from django.utils.html import format_html
from wagtail.admin.menu import MenuItem
from wagtail import hooks
from wagtailcache.cache import clear_cache

from cjkcms import __version__
from cjkcms.draftail import (
    register_inline_styling,
    register_block_feature,
    NewWindowExternalLinkHandler,
    DRAFTAIL_ICONS,
)


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" type="text/css" href="{}?v={}">',
        static("cjkcms/css/cjkcms-admin.css"),
        __version__,
    )


@hooks.register("insert_editor_css")
def editor_css():
    return format_html(
        '<link rel="stylesheet" type="text/css" href="{}?v={}">',
        static("cjkcms/css/cjkcms-editor.css"),
        __version__,
    )


@hooks.register("insert_editor_js")
def collapsible_js():
    return format_html(
        '<script src="{}?v={}"></script>',
        static("cjkcms/js/cjkcms-editor.js"),
        __version__,
    )


@hooks.register("register_icons")
def register_icons(icons):
    """
    Add custom SVG icons to the Wagtail admin.
    """
    # These SVG files should be in the django templates folder, and follow exact
    # specifications to work with Wagtail:
    # https://github.com/wagtail/wagtail/pull/6028
    icons.append("cjkcms/icons/align-left.svg")
    icons.append("cjkcms/icons/check-square-o.svg")
    icons.append("cjkcms/icons/columns.svg")
    icons.append("cjkcms/icons/desktop.svg")
    icons.append("cjkcms/icons/font.svg")
    icons.append("cjkcms/icons/google.svg")
    icons.append("cjkcms/icons/hand-pointer-o.svg")
    icons.append("cjkcms/icons/hashtag.svg")
    icons.append("cjkcms/icons/header.svg")
    icons.append("cjkcms/icons/list-alt.svg")
    icons.append("cjkcms/icons/map.svg")
    icons.append("cjkcms/icons/newspaper-o.svg")
    icons.append("cjkcms/icons/puzzle-piece.svg")
    icons.append("cjkcms/icons/recycle.svg")
    icons.append("cjkcms/icons/stop.svg")
    icons.append("cjkcms/icons/th-large.svg")
    icons.append("cjkcms/icons/universal-access.svg")
    icons.append("cjkcms/icons/usd.svg")
    icons.append("cjkcms/icons/window-maximize.svg")
    icons.append("cjkcms/icons/window-minimize.svg")
    return icons


def clear_wagtailcache(*args, **kwargs):
    clear_cache()


# Clear cache whenever pages/snippets are changed. Err on the side of clearing
# the cache vs not clearing the cache, as this usually leads to support requests
# when staff members make edits but do not see the changes.
hooks.register("after_delete_page", clear_wagtailcache)
hooks.register("after_move_page", clear_wagtailcache)
hooks.register("after_publish_page", clear_wagtailcache)
hooks.register("after_unpublish_page", clear_wagtailcache)
hooks.register("after_create_snippet", clear_wagtailcache)
hooks.register("after_edit_snippet", clear_wagtailcache)
hooks.register("after_delete_snippet", clear_wagtailcache)


@hooks.register("before_serve_document")
def serve_document_directly(document, request):
    """
    This hook prevents documents from being downloaded unless
    specified by an <a> tag with the download attribute.
    """
    content_type, content_encoding = mimetypes.guess_type(document.filename)
    response = HttpResponse(document.file.read(), content_type=content_type)
    response["Content-Disposition"] = 'inline;filename="{0}"'.format(document.filename)
    response["Content-Encoding"] = str(content_encoding)
    return response


class ImportExportMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_superuser


# @hooks.register("register_settings_menu_item")
# def register_import_export_menu_item():
#     return ImportExportMenuItem(
#         _("Import"),
#         reverse("import_index"),
#         classnames="icon icon-download",
#     )


@hooks.register("register_rich_text_features")
def register_underline_styling(features):
    register_inline_styling(
        features=features,
        feature_name="underline",
        type_="UNDERLINE",
        tag="u",
        description="Underline",
        label="U̲",
    )


@hooks.register("register_rich_text_features")
def register_larger_styling(features):
    register_inline_styling(
        features=features,
        feature_name="larger",
        type_="LARGER",
        tag="span",
        format='style="font-size:larger"',
        editor_style={"font-size": "larger"},
        description="Increase Font",
        icon=DRAFTAIL_ICONS.increase_font,
    )


@hooks.register("register_rich_text_features")
def register_smaller_styling(features):
    register_inline_styling(
        features=features,
        feature_name="smaller",
        type_="SMALLER",
        tag="span",
        format='style="font-size:smaller"',
        editor_style={"font-size": "smaller"},
        description="Decrease Font",
        icon=DRAFTAIL_ICONS.decrease_font,
    )


@hooks.register("register_rich_text_features")
def register_align_left_feature(features):
    register_block_feature(
        features=features,
        feature_name="left-align",
        type_="LEFT-ALIGN",
        description="Left align text",
        css_class="text-start",
        element="p",
        icon=DRAFTAIL_ICONS.left_align,
    )


@hooks.register("register_rich_text_features")
def register_align_centre_feature(features):
    register_block_feature(
        features=features,
        feature_name="centre-align",
        type_="CENTRE-ALIGN",
        description="Centre align text",
        css_class="text-center",
        element="p",
        icon=DRAFTAIL_ICONS.centre_align,
    )


@hooks.register("register_rich_text_features")
def register_align_right_feature(features):
    register_block_feature(
        features=features,
        feature_name="right-align",
        type_="RIGHT-ALIGN",
        description="Right align text",
        css_class="text-end",
        element="p",
        icon=DRAFTAIL_ICONS.right_align,
    )


@hooks.register("register_rich_text_features")
def register_external_link(features):
    features.register_link_type(NewWindowExternalLinkHandler)
