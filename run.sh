rm -rf result
mkdir result
cd testcases/
pytest --alluredir=../result
allure serve ../result