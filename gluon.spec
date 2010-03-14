%define git  5493f448

Name:		gluon
Summary:	Gluon is a cross-platform free and open source 2D game engine from KDE
Group:		Graphical desktop/KDE
Version:	0.69.0
Release:    %mkrel 0.%git.1
License:	GPL
URL:		http://gluon.tuxfamily.org/
Source0:	http://gitorious.net/gluon/%name-%version.%git.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:	glew-devel 
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	openal-devel

%description
Gluon is a cross-platform free and open source 2D game engine from KDE. 
It aims to make life easier for game developers by providing a simple 
but powerful API to handle 2D objects, sounds and inputs.

%files
%defattr(-,root,root)
%_kde_bindir/gluoncreator
%_kde_applicationsdir/gluon-creator.desktop
%_kde_appsdir/gluoncreator/gluoncreatorui.rc
%_kde_datadir/config.kcfg/gluoncreatorsettings.kcfg
%_kde_iconsdir/hicolor/*/apps/gluon_creator.png
%_kde_services/*.desktop
%_kde_datadir/kde4/servicetypes/gluoncreator_plugin.desktop
%_kde_libdir/gluon
%_kde_libdir/kde4/*.so

#-----------------------------------------------------------------------------

%define libgluonaudio_major 0
%define libgluonaudio %mklibname gluonaudio %{libgluonaudio_major}

%package -n %libgluonaudio
Summary:    %name library
Group:      System/Libraries

%description -n %libgluonaudio
%name library.

%files -n %libgluonaudio
%defattr(-,root,root,-)
%_kde_libdir/libGluonAudio.so.%{libgluonaudio_major}*

#-----------------------------------------------------------------------------

%define libgluoncore_major 0
%define libgluoncore %mklibname gluoncore %{libgluoncore_major}

%package -n %libgluoncore
Summary:    %name library
Group:      System/Libraries

%description -n %libgluoncore
%name library.

%files -n %libgluoncore
%defattr(-,root,root,-)
%_kde_libdir/libGluonCore.so.%{libgluoncore_major}*

#-----------------------------------------------------------------------------

%define libgluoncreator_major 0
%define libgluoncreator %mklibname gluoncreator %{libgluoncreator_major}

%package -n %libgluoncreator
Summary:    %name library
Group:      System/Libraries

%description -n %libgluoncreator
%name library.

%files -n %libgluoncreator
%defattr(-,root,root,-)
%_kde_libdir/libGluonCreator.so.%{libgluoncreator_major}*

#-----------------------------------------------------------------------------

%define libgluonengine_major 0
%define libgluonengine %mklibname gluonengine %{libgluonengine_major}

%package -n %libgluonengine
Summary:    %name library
Group:      System/Libraries

%description -n %libgluonengine
%name library.

%files -n %libgluonengine
%defattr(-,root,root,-)
%_kde_libdir/libGluonEngine.so.%{libgluonengine_major}*

#-----------------------------------------------------------------------------

%define libgluoninput_major 0
%define libgluoninput %mklibname gluoninput %{libgluoninput_major}

%package -n %libgluoninput
Summary:    %name library
Group:      System/Libraries

%description -n %libgluoninput
%name library.

%files -n %libgluoninput
%defattr(-,root,root,-)
%_kde_libdir/libGluonInput.so.%{libgluoninput_major}*

#-----------------------------------------------------------------------------

%define libgluongraphics_major 0
%define libgluongraphics %mklibname gluongraphics %{libgluongraphics_major}

%package -n %libgluongraphics
Summary:    %name library
Group:      System/Libraries

%description -n %libgluongraphics
%name library.

%files -n %libgluongraphics
%defattr(-,root,root,-)
%_kde_libdir/libGluonGraphics.so.%{libgluongraphics_major}*

#-----------------------------------------------------------------------------

%package -n %libname-devel
Summary:	Headers files for %name
Group:		Development/KDE and Qt
Provides:	lib%name-devel = %version-%release
Provides:	%name-devel = %version-%release
Requires:   %libgluonaudio = %version-%release
Requires:   %libgluoncore = %version-%release
Requires:   %libgluoncreator = %version-%release
Requires:   %libgluonengine = %version-%release
Requires:   %libgluoninput = %version-%release
Requires:   %libgluongraphics = %version-%release

%description -n %libname-devel
Headers files needed to build %name.

%files -n %libname-devel
%defattr(-,root,root,-)
%_kde_datadir/gluon/cmake
%_kde_datadir/cmake/Modules/*.cmake
%_kde_includedir/gluon
%_kde_libdir/*.so

#-----------------------------------------------------------------------------
%prep
%setup -q -n %name

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build


%clean
rm -fr %buildroot


