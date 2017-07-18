# Announcement service server's top url
ANNOUNCEMENT_SERVER = \
    'https://annoucement.example.com/?q=user/login&destination=top'
ANNOUNCEMENT_SERVER_LOGOUT = \
    'https://annoucement.example.com/?q=user/logout'

# Set force drupal logout
HORIZON_CONFIG['other_system_logout_url'] = ANNOUNCEMENT_SERVER_LOGOUT
