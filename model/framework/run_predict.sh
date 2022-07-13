python $1/code/input_adapter.py $2
python $1/code/sascorer.py tmp_input.smi > tmp_output.csv
python $1/code/output_adapter.py $3
rm tmp_input.smi tmp_output.csv
