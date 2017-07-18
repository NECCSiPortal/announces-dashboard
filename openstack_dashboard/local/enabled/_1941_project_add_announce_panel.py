# The slug of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'Announcements'
# The slug of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'project'
# The slug of the panel group the PANEL is associated with.
PANEL_GROUP = 'announce_group'

# Python panel class of the PANEL to be added.
ADD_PANEL = \
    'nec_portal.dashboards.project.announcement.panel.AnnouncementPanel'

DEFAULT_PANEL = 'announcement'

# A list of scss files to be included in the compressed set of files
ADD_SCSS_FILES = ['nec_portal/announcement/announcement.scss']

# A list of js files to be included in the compressed set of files
ADD_JS_FILES = ['nec_portal/announcement/announcement.js']
