## In Microsoft Terminal, or MacOS Terminal:
CD to homework repository. 

`mkdir` 'lab7', and cd into it. 

Windows/MacOS: `echo # Lab 7 > README.md`

`pipenv shell`
## In VS Code:

CTRL+SHIFT+P > 'Create: New Jupyter Notebook'. If you use VS Code often for Jupyter, it will already be at the top. You may type any portion of that command and the option will appear (try typing: 'Jup'). 

Save notebook as 'shapely.ipynb' (.ipynb = ipython notebook). 



## In .py file:

Read about python Modules [here](https://docs.python.org/3/tutorial/modules.html)

`./shapely_module.py`
```Python
def fact(n):
   return 1 if n == 1 else n * fact(n-1)

if (__name__ == '__main__'):
    fact(n)
```

In `shapely_module.ipynb`, import this module and run `fact(n)` with some integer value.

`./shapely_module.ipynb`
```Python
import shapely_module

shapely_module.fact(5)
```

Now that modules are understood, let's begin using Shapely. 

`./shapely_module.py`
```Python
from shapely.geometry import Polygon

def polygon():
    return Polygon([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).minimum_clearance

if (__name__ == '__main__'):
    polygon()
```

Change the function call in Jupyter to reflect the new function you've written.

`./shapely_module.ipynb`
```Python
import shapely_module

shapely_module.polygon()
```

Re-run the cell. \
You should see an error 

`./shapely_module.ipynb`
```Python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In [5], line 1
----> 1 shapely_module.polygon

AttributeError: module 'shapely_module' has no attribute 'polygon'
```
This occurs because a module is loaded only once per interpreter session. This means you would need to either restart the interpreter/kernal (not efficient when using Jupter), or use 

```Python
import importlib
importlib.reload(shapely_module)
```  

in your Jupyter import cell. This is only an issue while prototyping if you use Jupyter for running code. If building modules is the goal, it is better to prototype in the manner in which the module will typically be run: imported into a `.py` file (such as `views.py`) for access to various functions or classes.

## Prototyping in in Jupyter Notebook or .py file:

## Build Django app

Terminal> `django-admin startproject FieldShaper`

Terminal> `django-admin startapp Fields`

Fields/views.py
```Python
from django.http import HttpResponse

def index(request):
    context={'plot_div': shapely_module.polygon()}
    url = "Fields/Fields.html"
    return render(request, url, context)
```

Fields/urls.py
```Python
from django.urls import path
from . import views

urlpatterns = [
    path('Fields', views.index),
]
```

FieldShaper/urls.py
```Python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('Fields/', include('Fields.urls')),
    path('admin/', admin.site.urls),
]
```

Fields/templates/Fields.html
```HTML
<body>
    {% autoescape off %}
        {{ plot_div }}
    {% endautoescape %}
</body>
```

View the page at http://127.0.0.1:8000/Fields/Fields

Register model to view in Admin portal:

Fields/admin.py
```Python
from django.contrib import admin
from .models import Field
# Register your models here.

admin.site.register(Field)
```

Forms:

Fields/forms.py
```Python
from django.forms import ModelForm
from .models import Field

class FieldForm(ModelForm):
    class Meta:
        model = Field
        fields = ['field_name'] # or '__all__' to display all fields
```

When constructing and testing models with forms, problems may occur when model is modified and migrated.
If the form was used and data stored in the database, migration will throw a warning because there is already one or more entries.
These entries will need their columns modified to account for the new columns you're adding to that model (SQL table). 
If you have nothing useful stored, just delete all entries. Otherwise, you'll need to specify default values in these columns for the existing entries. 

Note: when refreshing the HTML page where you've entered something in the form, a notice appears warning that your form submission will be repeated. 
This will cause the page to re-enter the data into your database.