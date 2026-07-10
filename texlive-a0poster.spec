%global tl_name a0poster
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.22b
Release:	%{tl_revision}.1
Summary:	Support for designing posters on large paper
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/a0poster
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/a0poster.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/a0poster.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides fonts in sizes of 12pt up to 107pt and also makes sure that in
math formulas the symbols appear in the right size. Can also create a
PostScript header file for dvips which ensures that the poster will be
printed in the right size. Supported sizes are DIN A0, DIN A1, DIN A2
and DIN A3.

