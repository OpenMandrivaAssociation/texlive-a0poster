# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/a0poster
# catalog-date 2006-11-28 22:38:04 +0100
# catalog-license lppl
# catalog-version 1.22b
Name:		texlive-a0poster
Version:	1.22b
Release:	1
Summary:	Support for designing posters on large paper
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/a0poster
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a0poster.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a0poster.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides fonts in sizes of 12pt up to 107pt and also makes sure
that in math formulas the symbols appear in the right size. Can
also create a PostScript header file for dvips which ensures
that the poster will be printed in the right size. Supported
sizes are DIN A0, DIN A1, DIN A2 and DIN A3.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/a0poster/a0poster.cls
%{_texmfdistdir}/tex/latex/a0poster/a0size.sty
%doc %{_texmfdistdir}/doc/latex/a0poster/a0.pdf
%doc %{_texmfdistdir}/doc/latex/a0poster/a0.tex
%doc %{_texmfdistdir}/doc/latex/a0poster/a0_eng.pdf
%doc %{_texmfdistdir}/doc/latex/a0poster/a0_eng.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
