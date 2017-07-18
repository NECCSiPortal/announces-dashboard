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
from django.shortcuts import redirect

from horizon import exceptions
from horizon import tables

from nec_portal.dashboards.project.announcement \
    import tables as announcement_tables

from nec_portal.local import nec_portal_settings

ANNOUNCEMENT_SERVER = \
    getattr(nec_portal_settings, 'ANNOUNCEMENT_SERVER', '')


class IndexView(tables.DataTableView):
    table_class = announcement_tables.AnnouncementTable
    template_name = 'project/announcement/index.html'

    def get_data(self):
        return []


class DetailView(tables.DataTableView):
    table_class = announcement_tables.AnnouncementTable
    template_name = 'project/announcement/index.html'

    def get_data(self):
        return []

    def get(self, request):
        if not request.user.is_authenticated():
            raise exceptions.NotAuthenticated

        return redirect(ANNOUNCEMENT_SERVER + '/' + request.user.project_id)
