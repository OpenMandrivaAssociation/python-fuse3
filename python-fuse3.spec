%define  origname pyfuse3

Summary: Python 3 bindings for libfuse 3 with asynchronous API (Trio compatible)
Name: python-fuse3
Version: 2.0.0
Release: 1
Url: https://github.com/libfuse/pyfuse3/
Source: https://files.pythonhosted.org/packages/source/p/pyfuse3/%{origname}-%{version}.tar.gz
License: LGPL
Group: Development/Python

BuildRequires: pkgconfig(fuse3)
BuildRequires: python-devel
BuildRequires: python3egg(cython)
BuildRequires: python3egg(setuptools)

Provides: pyfuse3 = %version-%release

%description
This is a Python interface to FUSE3.

FUSE (Filesystem in USErspace) is a simple interface for userspace
programs to export a virtual filesystem to the linux kernel. FUSE3
also aims to provide a secure method for non privileged users to
create and mount their own filesystem implementations.

%prep
%setup -n %{origname}-%{version}

%build
%__python setup.py build

%install
%{__python} setup.py install --root $RPM_BUILD_ROOT

%files
%doc LICENSE Changes.* README.* examples
%{python_sitearch}/*
