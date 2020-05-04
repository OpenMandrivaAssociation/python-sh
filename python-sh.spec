Summary:	Subprocess replacement for python
Name:		python-sh
Version:	1.13.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/c9/3b/2c9a22bf1c48ced7ff3a11d4a862682c21d825c35f9d025811ad9808d263/sh-1.13.1.tar.gz
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
