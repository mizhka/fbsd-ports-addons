--- ./webapp/graphite/cli/urls.py.orig	2013-08-21 17:11:04.000000000 +0000
+++ ./webapp/graphite/cli/urls.py	2014-02-13 02:01:59.481111098 +0000
@@ -12,7 +12,7 @@
 See the License for the specific language governing permissions and
 limitations under the License."""
 
-from django.conf.urls.defaults import *
+from django.conf.urls import *
 
 urlpatterns = patterns('graphite.cli.views',
      (r'^autocomplete/?$', 'autocomplete'),
