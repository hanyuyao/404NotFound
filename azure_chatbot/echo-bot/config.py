#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "ae57b40b-4f51-4681-a9eb-ed846a227dd6")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "ElizaHuangTaigidian2021")