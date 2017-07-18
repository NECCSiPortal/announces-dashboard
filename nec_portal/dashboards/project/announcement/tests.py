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

from django.core.urlresolvers import reverse

from openstack_dashboard.test import helpers as test

INDEX_URL = reverse("horizon:project:announcement:index")
ANNOUNCEMENT_URL = reverse("horizon:project:announcement:announcement")


class AnnouncementTest(test.TestCase):
    # A test which announcement index is existed.
    def test_display_index(self):
        res = self.client.get(INDEX_URL)

        self.assertTrue(res.status_code == 200)
        self.assertTemplateUsed(res, 'project/announcement/_index.html')

    # A test which announcement index error is existed.
    def test_display_error_index(self):
        res = self.client.get(INDEX_URL + "/xxx")

        self.assertEqual(res.status_code, 404)
        self.assertTemplateUsed(res, '404.html')

    # A test which announcement url is existed.
    def test_display_announcement(self):
        res = self.client.get(ANNOUNCEMENT_URL)

        # Redirect a announcement system url.
        self.assertTrue(res.status_code == 302)

    # A test which not authenticated user access announcement url.
    def test_display_not_authenticated_announcement(self):
        self.client.logout()
        res = self.client.get(ANNOUNCEMENT_URL)

        # Redirect a login page
        self.assertTrue(res.status_code == 302)
