from pprint import pprint

import subprocess
from edgetpu_compiler_log_parser import EdgeTPUCompilerLogParser

if __name__ == "__main__":
    model_path_1 = "tests/model/efficientnet-edgetpu-M_quant.tflite"
    model_path_2 = "tests/model/efficientnet-edgetpu-S_quant.tflite"

    cmd = "edgetpu_compiler "
    cmd += model_path_1 + " "
    cmd += model_path_2 + " "

    output = subprocess.check_output(cmd, shell=True)

    log_parser = EdgeTPUCompilerLogParser(output)
    pprint(log_parser.get_compile_infos())
