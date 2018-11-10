#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kirigami2
Version  : 5.52.0
Release  : 8
URL      : https://download.kde.org/stable/frameworks/5.52/kirigami2-5.52.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.52/kirigami2-5.52.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.52/kirigami2-5.52.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: kirigami2-data = %{version}-%{release}
Requires: kirigami2-lib = %{version}-%{release}
Requires: kirigami2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : git
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5QuickControls2)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools-dev

%description
Add here, with either a script that does a git checkout
or as git submodules the two projects:

%package abi
Summary: abi components for the kirigami2 package.
Group: Default

%description abi
abi components for the kirigami2 package.


%package data
Summary: data components for the kirigami2 package.
Group: Data

%description data
data components for the kirigami2 package.


%package dev
Summary: dev components for the kirigami2 package.
Group: Development
Requires: kirigami2-lib = %{version}-%{release}
Requires: kirigami2-data = %{version}-%{release}
Provides: kirigami2-devel = %{version}-%{release}

%description dev
dev components for the kirigami2 package.


%package lib
Summary: lib components for the kirigami2 package.
Group: Libraries
Requires: kirigami2-data = %{version}-%{release}
Requires: kirigami2-license = %{version}-%{release}

%description lib
lib components for the kirigami2 package.


%package license
Summary: license components for the kirigami2 package.
Group: Default

%description license
license components for the kirigami2 package.


%prep
%setup -q -n kirigami2-5.52.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541870505
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1541870505
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kirigami2
cp LICENSE.LGPL-2 %{buildroot}/usr/share/package-licenses/kirigami2/LICENSE.LGPL-2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files abi
%defattr(-,root,root,-)
/usr/share/abi/libKF5Kirigami2.so.5.52.0.abi

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ca/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/cs/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/da/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/de/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/el/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/es/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/eu/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/fi/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/fr/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/gl/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/hu/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ia/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/id/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/it/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ja/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ko/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/nl/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/nn/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/pl/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/pt/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ru/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sk/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sl/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sr/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sv/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/tr/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/uk/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/libkirigami2plugin_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Kirigami2/KirigamiPluginFactory
/usr/include/KF5/Kirigami2/PlatformTheme
/usr/include/KF5/Kirigami2/TabletModeWatcher
/usr/include/KF5/Kirigami2/kirigami2_export.h
/usr/include/KF5/Kirigami2/kirigamipluginfactory.h
/usr/include/KF5/Kirigami2/platformtheme.h
/usr/include/KF5/Kirigami2/tabletmodewatcher.h
/usr/lib64/cmake/KF5Kirigami2/KF5Kirigami2Config.cmake
/usr/lib64/cmake/KF5Kirigami2/KF5Kirigami2ConfigVersion.cmake
/usr/lib64/cmake/KF5Kirigami2/KF5Kirigami2Macros.cmake
/usr/lib64/cmake/KF5Kirigami2/KF5Kirigami2Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Kirigami2/KF5Kirigami2Targets.cmake
/usr/lib64/libKF5Kirigami2.so
/usr/lib64/qt5/mkspecs/modules/qt_Kirigami2.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Kirigami2.so.5
/usr/lib64/libKF5Kirigami2.so.5.52.0
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractApplicationItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractApplicationWindow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractCard.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractItemViewHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Action.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ActionToolBar.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ApplicationItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ApplicationWindow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/BasicListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Card.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/CardsGridView.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/CardsLayout.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/CardsListView.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ContextDrawer.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/FormLayout.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/GlobalDrawer.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Heading.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/InlineMessage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ItemViewHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Label.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ListItemDragHandle.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/OverlayDrawer.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/OverlaySheet.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Page.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/PageRow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ScrollablePage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Separator.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/SwipeListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Theme.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ToolBarApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Units.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/libkirigamiplugin.so
/usr/lib64/qt5/qml/org/kde/kirigami.2/plugins.qmltypes
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionIconGroup.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionMenuItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionMenuItemBase.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionMenuItemQt510.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionMenuItemQt59.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionsMenu.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/BannerImage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/CardsGridViewPrivate.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/CardsListViewPrivate.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/CornerShadow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/DefaultListItemBackground.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/EdgeShadow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/PageActionPropertyGroup.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/PrivateActionToolButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/RefreshableScrollView.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/SwipeItemEventFilter.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/AbstractPageHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/BreadcrumbControl.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/PageRowGlobalToolBarStyleGroup.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/PageRowGlobalToolBarUI.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/TabBarControl.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/TitlesPageHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/ToolBarPageHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/qmldir
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Material/AbstractListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Material/Label.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Material/SwipeListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Material/Theme.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop/AbstractApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop/AbstractListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop/ApplicationWindow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop/SwipeListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop/Theme.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop/Units.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/AbstractApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/AbstractCard.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/AbstractListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/ApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/InlineMessage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/OverlayDrawer.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/OverlaySheet.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/SwipeListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/BackButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/ContextIcon.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/ForwardButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/GenericDrawerIcon.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/IconPropertiesGroup.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/MenuIcon.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/PassiveNotification.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/ScrollView.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kirigami2/LICENSE.LGPL-2
