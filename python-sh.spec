Summary:	Subprocess replacement for python
Name:		python-sh
Version:	1.12.14
Release:	1
Source0:	https://files.pythonhosted.org/packages/7c/71/199d27d3e7e78bf448bcecae0105a1d5b29173ffd2bbadaa95a74c156770/sh-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.org/project/sh/
BuildArch:	noarch
BuildRequires:	python-distribute
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources

%description
sh is a full-fledged subprocess replacement for Python 2.6 - 3.6, PyPy and PyPy3
that allows you to call any program as if it were a function:

.. code:: python

from sh import ifconfig
print ifconfig("eth0")

sh is *not* a collection of system commands implemented in Python.

%prep
%autosetup -p1 -n sh-%{version}
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

%files
%{python_sitelib}/sh.py
%{python_sitelib}/__pycache__/*
%{python_sitelib}/*.egg-info
