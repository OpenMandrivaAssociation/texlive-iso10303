Name:		texlive-iso10303
Version:	15878
Release:	2
Summary:	Typesetting the STEP standards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/isostds/iso10303
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iso10303.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iso10303.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iso10303.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Class and package files building on iso for typesetting the ISO
10303 (STEP) standards. Standard documents prepared using these
packages have been published by ISO.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/iso10303/aicv1.sty
%{_texmfdistdir}/tex/latex/iso10303/apendint.tex
%{_texmfdistdir}/tex/latex/iso10303/apmpspec.tex
%{_texmfdistdir}/tex/latex/iso10303/apmptbl.tex
%{_texmfdistdir}/tex/latex/iso10303/apmptempl.tex
%{_texmfdistdir}/tex/latex/iso10303/apsstempl.tex
%{_texmfdistdir}/tex/latex/iso10303/apv12.sty
%{_texmfdistdir}/tex/latex/iso10303/atsv11.sty
%{_texmfdistdir}/tex/latex/iso10303/bpfap1.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap10.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap11.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap12.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap13.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap14.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap15.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap16.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap2.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap3.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap4.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap5.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap6.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap7.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap8.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfap9.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats1.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats10.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats11.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats12.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats14.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats2.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats3.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats4.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats5.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats6.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats7.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats8.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfats9.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfir1.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfir2.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfir3.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfs1.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfs2.tex
%{_texmfdistdir}/tex/latex/iso10303/bpfs3.tex
%{_texmfdistdir}/tex/latex/iso10303/irv12.sty
%{_texmfdistdir}/tex/latex/iso10303/stepman.tex
%{_texmfdistdir}/tex/latex/iso10303/stepv13.4ht
%{_texmfdistdir}/tex/latex/iso10303/stepv13.sty
%{_texmfdistdir}/tex/latex/iso10303/stppdlst.tex
%doc %{_texmfdistdir}/doc/latex/iso10303/README
%doc %{_texmfdistdir}/doc/latex/iso10303/step4ht.pdf
%doc %{_texmfdistdir}/doc/latex/iso10303/stepe.pdf
%doc %{_texmfdistdir}/doc/latex/iso10303/stepman.pdf
#- source
%doc %{_texmfdistdir}/source/latex/iso10303/step4ht.dtx
%doc %{_texmfdistdir}/source/latex/iso10303/step4ht.ins
%doc %{_texmfdistdir}/source/latex/iso10303/stepe.dtx
%doc %{_texmfdistdir}/source/latex/iso10303/stepe.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
