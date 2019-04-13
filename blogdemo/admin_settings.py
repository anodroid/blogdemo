# django-suit config
SUIT_CONFIG = {
    'ADMIN_NAME': 'Infernoid·Infinity',
    'HEADER_DATE_FORMAT': '',
    'HEADER_TIME_FORMAT': 'H:i',
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'LIST_PER_PAGE': 20,
    'MENU_OPEN_FIRST_CHILD': True,
    'MENU': (
        # sites是默认原先的app和models
        # 'sites',
        '-',
        {'app': 'auth', 'label': u'权限管理', 'icon': 'icon-lock'},
        '-',
        {'app': 'duser', 'label': u'平台用户', 'icon': 'icon-user'},
        '-',
        {'app': 'dtheme', 'label': u'主题管理', 'icon': 'icon-tags'},
        '-',
        {'app': 'dpost', 'label': u'文章管理', 'icon': 'icon-edit'},
        '-',
        # 如果使用http这种绝对路径的话，菜单不会展开，且不会标记为active状态
        {'url': '/admin/theme/mysql', 'label': u'第三数据', 'icon': 'icon-lock'},
        '-',
        {'label': u'统计数据', 'icon': 'icon-tags', 'models': (
            {'url': '/admin/theme/data', 'label': u'第一数据'},
            {'url': '/admin/theme/show', 'label': u'第二数据'}
        )}
    )
}