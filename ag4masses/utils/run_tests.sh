# Copyright 2023 DeepMind Technologies Limited
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
# ==============================================================================

# Directory where output files go
TESTDIR=$HOME/ag4mtest
# Directory containing AG4Masses source files
AG4MDIR=$HOME/ag4masses
# Directory containing external libraries including ag_ckpt_vocab and meliad
AGLIB=$HOME/aglib

AGDIR=$AG4MDIR/alphageometry
DATA=$AGLIB/ag_ckpt_vocab
MELIAD_PATH=$AGLIB/meliad
export PYTHONPATH=$PYTHONPATH:$AGDIR:$AGLIB:$MELIAD_PATH

ERRFILE=$TESTDIR/test.log
# stdout and stderr are written to both ERRFILF and console
exec > >(tee $ERRFILE) 2>&1

cd $AGDIR

python problem_test.py
python geometry_test.py
python graph_utils_test.py
python numericals_test.py
python graph_test.py
python dd_test.py
python ar_test.py
python ddar_test.py
python trace_back_test.py
python alphageometry_test.py
python lm_inference_test.py --meliad_path=$MELIAD_PATH --data_path=$DATA
