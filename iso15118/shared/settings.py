import os
from typing import Optional

import environs


class SettingKey:
    PKI_PATH = "PKI_PATH"
    MESSAGE_LOG_JSON = "MESSAGE_LOG_JSON"
    MESSAGE_LOG_EXI = "MESSAGE_LOG_EXI"
    ENABLE_TLS_1_3 = "ENABLE_TLS_1_3"


shared_settings = {}
SHARED_CWD = os.path.dirname(os.path.abspath(__file__))
JAR_FILE_PATH = SHARED_CWD + "/EXICodec.jar"

WORK_DIR = os.getcwd()


def load_shared_settings(env_path: Optional[str] = None):
    env = environs.Env(eager=False)
    env.read_env(path=env_path)  # read .env file, if it exists

def set_PKI_PATH(path: str) -> None:
    global PKI_Path
    PKI_Path = path

def get_PKI_PATH() -> str:
    return PKI_Path

MESSAGE_LOG_JSON = True
MESSAGE_LOG_EXI = False

V20_EVSE_SERVICES_CONFIG = SHARED_CWD + "/examples/secc/15118_20/service_config.json"

enabled_tls_1_3 = False

def enable_tls_1_3() -> None:
    global enabled_tls_1_3
    enabled_tls_1_3 = True

def is_tls_1_3_enabled() -> bool:
    return enabled_tls_1_3

shared_settings = None

ignoring_value_range = False

def set_ignoring_value_range(ignoring):
    global ignoring_value_range 
    ignoring_value_range = ignoring

def get_ignoring_value_range() -> bool:
    return ignoring_value_range
