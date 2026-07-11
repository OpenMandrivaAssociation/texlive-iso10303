%global tl_name iso10303
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Typesetting the STEP standards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/isostds/iso10303
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iso10303.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iso10303.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iso10303.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Class and package files building on iso for typesetting the ISO 10303
(STEP) standards. Standard documents prepared using these packages have
been published by ISO.

