#!/usr/bin/env python

# Copyright 2016 Daniel Nunes
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from os.path import abspath, dirname, join


if getattr(sys, 'frozen', False):
    cur_folder = sys._MEIPASS
else:
    cur_folder = join(dirname(abspath(__file__)), "..")


def get_version():
    import configparser

    config = configparser.ConfigParser()
    config.read(join(cur_folder, "setup.cfg"))

    return config.get('bumpversion', 'current_version') + "." + config.get('bumpversion', 'current_build')

__version__ = get_version()
