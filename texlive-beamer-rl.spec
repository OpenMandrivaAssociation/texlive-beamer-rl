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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class provides patches of some beamer templates and commands for
presentation from right to left. It requires Babel with the LuaTeX
engine.

