/*
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 *
 */

var Announcement = function() {
  var announcement = {};

  announcement.callAnnouncementFrame = function(setting) {
    // Create From object
    var form = document.createElement("form");
    form.setAttribute("target", setting["target"]);
    form.setAttribute("action", setting["action"]);
    form.setAttribute("method", "POST");
    document.body.appendChild(form);

    // Set post parameters
    var parameters = {
      "token": setting["token"],
      "form_id": "user_login",
      "name": setting["name"],
      "pass": "dummy"
    }
    for (var paramKey in parameters) {
      var input = document.createElement("input");
      input.setAttribute('type', 'hidden');
      input.setAttribute('name', paramKey);
      input.setAttribute('value', parameters[paramKey]);
      form.appendChild(input);
    }
    $("#announceMents").one("load", function() {
      $(this).removeAttr('style');
    });
    form.submit();
  };

  return announcement;
}

var anouncement = new Announcement();
