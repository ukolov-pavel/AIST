for	%%i in (Test*.*) do (
	@echo %%i-%date:~-10%-%time::=.%
	del C:\TeamCity\buildAgent\work\62c61fe4a818ba30\report\*.* /Q
	py.test %%i --alluredir C:\TeamCity\buildAgent\work\62c61fe4a818ba30\report
	cd C:\Users\ukolovp\allure-commandline\bin
	allure generate C:\TeamCity\buildAgent\work\62c61fe4a818ba30\report -o C:\TeamCity\buildAgent\work\62c61fe4a818ba30\results\%%i-%date:~-10%-%time::=.%\
	cd C:\TeamCity\buildAgent\work\62c61fe4a818ba30
	rmdir C:\TeamCity\buildAgent\work\62c61fe4a818ba30\.cache /Q /S
	rmdir C:\TeamCity\buildAgent\work\62c61fe4a818ba30\__pycache__ /Q /S
	del C:\TeamCity\buildAgent\work\62c61fe4a818ba30\geckodriver.log
	)
@pause