from conans import ConanFile, tools, Meson
import os

class Rubberband(ConanFile):
    generators = "pkg_config"
    settings = "os", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    def source(self):
        git = tools.Git(folder="rubberband")
        git.clone("https://github.com/breakfastquay/rubberband.git", "default")

    def build(self):
        meson = Meson(self)
        meson.configure(source_folder="rubberband", build_folder="build")
        meson.build()
        meson.install()

    def package_info(self):
        self.cpp_info.libs = ["rubberband"]