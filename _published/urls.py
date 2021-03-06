from django.conf.urls import patterns, url

from api_docs.views import IPythonNotebookPage


urlpatterns = patterns(
    '',
    url("graph-gmail-inbox-data/$",
        IPythonNotebookPage.as_view(
            lang='ipython-notebooks',
            notebook='gmail'),
        name='ipython-notebook-gmail'),
    url("markowitz-portfolio-optimization/$",
        IPythonNotebookPage.as_view(
            lang='ipython-notebooks',
            notebook='markowitz'),
        name='ipython-notebook-markowitz'),
    url("cartodb/$",
        IPythonNotebookPage.as_view(
            lang='ipython-notebooks',
            notebook='cartodb'),
        name='ipython-notebook-cartodb'),
    url("network-graphs/$",
        IPythonNotebookPage.as_view(
            lang='ipython-notebooks',
            notebook='networkx'),
        name='ipython-notebook-networkx'),
    url("subplots/$",
        IPythonNotebookPage.as_view(
            lang='ipython-notebooks',
            notebook='make_subplots'),
        name='ipython-notebook-make_subplots'),
    url("basemap-maps/$",
        IPythonNotebookPage.as_view(
            lang='ipython-notebooks',
            notebook='basemap'),
        name='ipython-notebook-basemap'),
    url("collaboration/$",
        IPythonNotebookPage.as_view(
            lang='ipython-notebooks',
            notebook='collaborate'),
        name='ipython-notebook-collaborate')
)
