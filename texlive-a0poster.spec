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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides fonts in sizes of 12pt up to 107pt and also makes sure that in
math formulas the symbols appear in the right size. Can also create a
PostScript header file for dvips which ensures that the poster will be
printed in the right size. Supported sizes are DIN A0, DIN A1, DIN A2
and DIN A3.

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
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/a0poster
%dir %{_datadir}/texmf-dist/tex/latex/a0poster
%doc %{_datadir}/texmf-dist/doc/latex/a0poster/a0.pdf
%doc %{_datadir}/texmf-dist/doc/latex/a0poster/a0.tex
%doc %{_datadir}/texmf-dist/doc/latex/a0poster/a0_eng.pdf
%doc %{_datadir}/texmf-dist/doc/latex/a0poster/a0_eng.tex
%{_datadir}/texmf-dist/tex/latex/a0poster/a0poster.cls
%{_datadir}/texmf-dist/tex/latex/a0poster/a0size.sty
