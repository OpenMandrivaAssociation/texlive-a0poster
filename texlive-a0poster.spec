Name:		texlive-a0poster
Version:	54071
Release:	2
Summary:	Support for designing posters on large paper
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/a0poster
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a0poster.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a0poster.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides fonts in sizes of 12pt up to 107pt and also makes sure
that in math formulas the symbols appear in the right size. Can
also create a PostScript header file for dvips which ensures
that the poster will be printed in the right size. Supported
sizes are DIN A0, DIN A1, DIN A2 and DIN A3.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/a0poster/a0poster.cls
%{_texmfdistdir}/tex/latex/a0poster/a0size.sty
%doc %{_texmfdistdir}/doc/latex/a0poster/a0.pdf
%doc %{_texmfdistdir}/doc/latex/a0poster/a0.tex
%doc %{_texmfdistdir}/doc/latex/a0poster/a0_eng.pdf
%doc %{_texmfdistdir}/doc/latex/a0poster/a0_eng.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
