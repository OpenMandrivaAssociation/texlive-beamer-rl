Name:		texlive-beamer-rl
Version:	69254
Release:	1
Summary:	Right to left presentation with beamer and babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-rl
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-rl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-rl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class provides patches of some beamer templates and
commands for presentation from right to left. It requires Babel
with the LuaTeX engine.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/beamer-rl
%doc %{_texmfdistdir}/doc/lualatex/beamer-rl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
