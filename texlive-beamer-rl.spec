%global tl_name beamer-rl
%global tl_revision 76587

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2
Release:	%{tl_revision}.1
Summary:	Right to left presentation with beamer and babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/beamer-rl
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-rl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-rl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class provides patches of some beamer templates and commands for
presentation from right to left. It requires Babel with the LuaTeX
engine.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/lualatex
%dir %{_datadir}/texmf-dist/tex/lualatex
%dir %{_datadir}/texmf-dist/doc/lualatex/beamer-rl
%dir %{_datadir}/texmf-dist/tex/lualatex/beamer-rl
%doc %{_datadir}/texmf-dist/doc/lualatex/beamer-rl/Example-of-use-ar.pdf
%doc %{_datadir}/texmf-dist/doc/lualatex/beamer-rl/Example-of-use-ar.tex
%doc %{_datadir}/texmf-dist/doc/lualatex/beamer-rl/Example-of-use-en.pdf
%doc %{_datadir}/texmf-dist/doc/lualatex/beamer-rl/Example-of-use-en.tex
%doc %{_datadir}/texmf-dist/doc/lualatex/beamer-rl/README.txt
%{_datadir}/texmf-dist/tex/lualatex/beamer-rl/beamer-rl.cls
%{_datadir}/texmf-dist/tex/lualatex/beamer-rl/pgfpages-rl.sty
%{_datadir}/texmf-dist/tex/lualatex/beamer-rl/translator-basic-dictionary-Arabic.dict
%{_datadir}/texmf-dist/tex/lualatex/beamer-rl/translator-bibliography-dictionary-Arabic.dict
%{_datadir}/texmf-dist/tex/lualatex/beamer-rl/translator-environment-dictionary-Arabic.dict
%{_datadir}/texmf-dist/tex/lualatex/beamer-rl/translator-numbers-dictionary-Arabic.dict
%{_datadir}/texmf-dist/tex/lualatex/beamer-rl/translator-theorem-dictionary-Arabic.dict
