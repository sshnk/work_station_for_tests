To run tests you need:
1. Download .zip archive.
2.Unpack it.
3.Download Python ver. 3.7.3 or higher
4.You need to activate your virtual environment (1. Open cmd panel and make a directory for the environment (write "mkdir environment" - go to this dir "cd environment") 2. Run virtual environment write "python -m venv selenium_env")
5.Start script in vert.env (write in console "selenium_env/Scripts/activate.bat"
6.You need to install libraries from requirements - (write in console "pip install -r \path\to\requirements.txt")
7.run tests "pytest -v --tb=line --language=en -m need_review \path\to\test_product_page.py"


Summary.
1.Run vert.env. (activate.bat)
2.install requirements from requirements.txt ("pip install -r \path\to\requirements.txt")
3.run tests ("pytest -v --tb=line --language=en -m need_review \path\to\test_product_page.py")

If something go wrong, probably you must to update your chrome driver (https://sites.google.com/chromium.org/driver/home)
If something go wrong with imports - delete/write "." before packages ( like from ("."/or delete it)pages.product_page import ProductPage) or delete empty file "__init__.py"
