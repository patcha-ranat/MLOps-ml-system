.SILENT: venv install

GREEN=\033[0;32m
YELLOW=\033[0;33m
GREY=\033[0;30m
NC=\033[0m # No Color

venv:
	python -m venv pyenv
	echo "${YELLOW}Please, execute 'source pyenv/Scripts/activate' before 'make install'${NC}"
	echo "${GREY}For MacOS/Linux: 'source pyenv/script/bin/activate'${NC}"
	echo "${GREY}If dependency conflict between project, please run 'make clean' and manually install dependency for each project (Read 'README.md')${NC}"

install:
	pip install -r requirements.txt
	pip install -r mbti_ipip/requirements.txt

clean:
	rm -r pyenv
