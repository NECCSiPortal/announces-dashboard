#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
#
#

"""
Views for managing Announcements.
"""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from horizon import tables

from nec_portal.dashboards.project.announcement \
    import tables as announcement_tables

ANNOUNCEMENT_SERVER = \
    getattr(settings, 'ANNOUNCEMENT_SERVER', '')
ANNOUNCEMENT_SERVER_LOGOUT = \
    getattr(settings, 'ANNOUNCEMENT_SERVER_LOGOUT', '')


class IndexView(tables.DataTableView):
    table_class = announcement_tables.AnnouncementTable
    template_name = 'project/announcement/index.html'
    page_title = _('Announcements')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        request = self.request
        project_id = request.user.project_id

        context["announcement_url"] = ANNOUNCEMENT_SERVER + '/' + project_id
        context["announcement_logout_url"] = ANNOUNCEMENT_SERVER_LOGOUT
        context["token"] = request.user.token.id
        context["name"] = request.user.username

        return context

    def get_data(self):
        return []
