PY_CHAPTER_01 += 00_part_one.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 01_intro_and_agreements.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 02_python_tooling_to_get_started.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 03_python_running_code.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 04_python_statements.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 05_python_comments.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 06_python_sequential_code.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 07_python_variables_and_types.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 08_python_expressions.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 09_input.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 10_python_conditional_flow.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 11_python_repetitive_flow.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 12_python_functions.md
PY_CHAPTER_01 += pandoc_page_break.txt
PY_CHAPTER_01 += 00_part_one_excercises.md
PY_CHAPTER_01 += pandoc_page_break.txt

PY_CHAPTER_02 += 200_part_two.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 201_console.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 202_lists.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 203_strings.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 204_exceptions.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 204_files.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 203_functions_part_2.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 205_objects_and_classes.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 205_objects_ex_basket.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 206_tkinter.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 207_gui_and_serial.md
PY_CHAPTER_02 += pandoc_page_break.txt
PY_CHAPTER_02 += 200_part_two_excercises.md

PY_CHAPTER_03 += 300_part_three_data.md
PY_CHAPTER_03 += 301_databases_intro.md
PY_CHAPTER_03 += 302_databases_sqlite_intro.md
PY_CHAPTER_03 += 303_databases_sql_intro.md
PY_CHAPTER_03 += 304_python_en_sql.md
PY_CHAPTER_03 += 306_modules.md
PY_CHAPTER_03 += 306_part_four_apis.md
PY_CHAPTER_03 += 309_dictionaries.md
PY_CHAPTER_03 += 307_http_and_rest.md
PY_CHAPTER_03 += 305_flask.md

PY_ANNEX += annex.md
PY_ANNEX += pandoc_page_break.txt
PY_ANNEX += tools_command_getting_started.md
PY_ANNEX += pandoc_page_break.txt
PY_ANNEX += tools_command_getting_started_windows.md
PY_ANNEX += pandoc_page_break.txt
PY_ANNEX += tools_command_getting_started_linux.md
PY_ANNEX += pandoc_page_break.txt
PY_ANNEX += test.md


PY_CHAPTERS += $(PY_CHAPTER_01) $(PY_CHAPTER_02) $(PY_CHAPTER_03) $(PY_ANNEX)
#PY_CHAPTERS += $(PY_CHAPTER_01) $(PY_CHAPTER_02) $(PY_ANNEX)
#PY_CHAPTERS = 00_part_one_excercises.md

pagebreak = pandoc_page_break.txt

all:
	pandoc title.txt $(PY_CHAPTERS) -o dist/py_cursus_epub_nl.epub --css base.css --epub-cover-image=front_page.jpg\

	pandoc frontpage.md -o dist/front_page_nl.html  --self-contained -s -c github-pandoc.css

	pandoc header.md -o dist/header_nl.html  --self-contained -s -c github-pandoc.css

	pandoc title.txt $(PY_CHAPTERS) -o dist/py_cursus_nl.html -B dist/header_nl.html  --self-contained -s --toc --toc-depth=2  -c github-pandoc.css

	wkhtmltopdf dist/py_cursus_nl.html dist/py_cursus_nl.pdf

	zip dist/py_cursus_nl.zip dist/py_cursus_nl.epub dist/py_cursus_nl.html dist/py_cursus_nl.pdf

clean:
	rm dist/cursus.epub
