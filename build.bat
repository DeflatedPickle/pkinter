rmdir /s /q "dist/" && ^
pip3 install wheel && ^
python setup.py sdist bdist_wheel && ^
twine upload dist/*