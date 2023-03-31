Name:		texlive-ekaia
Version:	49594
Release:	2
Summary:	Article format for publishing the Basque Country Science and Technology Journal "Ekaia"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ekaia
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ekaia.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ekaia.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ekaia.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the article format for publishing the
Basque Country Science and Technology Journal "Ekaia" at the
University of the Basque Country.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ekaia
%{_texmfdistdir}/tex/latex/ekaia
%doc %{_texmfdistdir}/doc/latex/ekaia

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
