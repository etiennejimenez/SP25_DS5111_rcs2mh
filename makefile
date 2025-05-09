default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env

	. env/bin/activate; pip install -r requirements.txt
	bash -c "source env/bin/activate && pip install -r requirements.txt"

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=10000 'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	python -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')"

index.html:
	wget: http://example.com

title.txt:
	cat index.html | grep Example > title.txt

lint:
	. env/bin/activate; pylint bin/ || true
	. env/bin/activate; pylint tests/ || true

test: lint
	. env/bin/activate; pytest -vvx tests
	
gainers:
	. env/bin/activate; python main.py ${SRC}

clean:
	rm ygainers.* || true
	rm wsjgainers.* || true

final_git_push: lint test
	git push

