from conans import ConanFile, tools, Meson
import os

class Rubberband(ConanFile):
    name = "rubberband"
    version = "default"
    generators = "pkg_config"
    settings = "os", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    license = "GPL-2.0"

    def source(self):
        git = tools.Git(folder="rubberband")
        git.clone("https://github.com/breakfastquay/rubberband.git", "default")

    def _configure(self):
        self.meson = Meson(self)
        self.meson.configure(source_folder="rubberband", build_folder="build")

    def build(self):
        self._configure()
        self.meson.build()

    def package(self):
        self._configure()
        self.meson.install()

    def package_info(self):
        self.cpp_info.libs = ["rubberband"]