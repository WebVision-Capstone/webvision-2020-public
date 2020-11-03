# Downloading and Formatting Data

Run the files in the following order:

```bash
# download the data
bash download.sh
# distribute the data over the image directories
python process_meta.py
# creat the validation and test sets
python make_validaion_and_test.py
```
