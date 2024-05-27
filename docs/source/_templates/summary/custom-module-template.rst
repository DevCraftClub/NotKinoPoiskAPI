{{ fullname | escape | underline }}

.. automodule:: {{ fullname }}
	:members:
  
	{% block attributes %}
	{% if attributes %}
	.. rubric:: Атрибуты модуля

	.. autosummary::
		:toctree:
		{% for item in attributes %}
			{{ item }}
		{%- endfor %}
	{% endif %}
	{% endblock %}

	{% block functions %}
   {% if functions %}
   .. rubric:: {{ _('Функции') }}

   .. autosummary::
      :toctree:                         
   {% for item in functions %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block classes %}
   {% if classes %}
   .. rubric:: {{ _('Классы') }}

   .. autosummary::
      :toctree:                         
      :template: custom-class-template.rst
   {% for item in classes %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block exceptions %}
   {% if exceptions %}
   .. rubric:: {{ _('Исключения') }}

   .. autosummary::
      :toctree:                         
   {% for item in exceptions %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

{% block modules %}
{% if modules %}
.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom-module-template.rst
   :recursive:
{% for item in modules %}
   {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}